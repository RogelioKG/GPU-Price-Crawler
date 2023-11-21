# standard library
import random
import time

# third party library
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement  # 網頁元素，find 回傳的資料結構
from selenium.webdriver.support.ui import WebDriverWait  # 掛機
from selenium.webdriver.support import expected_conditions as EC  # 預期元素
from selenium.common.exceptions import NoSuchElementException  # Exceptio n 找不到元素
from tqdm import tqdm # 進度條 (酷)

# local library
from components.accessor import CSV
from components.exception import CrawlingError, GPUInitError
from components.gpu import GPU
from parameters.variables import NEXT_BLOCKS, EXPECTED_RECORDS, SLEEP
from parameters.constants import PCHOME_URL, HEIGHT, SCRIPT_DIR
from services.crawling_functions import fetch_info
from services.init_webdriver import get_driver, set_options

# 正確資料緩衝區
correct_records_buffer = []

# 正確資料累積量
# (抓到且正確的資料)
correct_records_count = 0

# 錯誤資料累積量
# (抓到但不正確的資料 & 無法抓到的資料)
# (一旦 correct_records_buffer 有新添資料，清零)
wrong_records_count = 0


def try_converting_to_record(block: WebElement, pbar: tqdm) -> None:
    global correct_records_count
    global wrong_records_count

    # 忽略滾動監控
    if block.get_attribute("id") != "ScrollNav":
        result = fetch_info(block)
        if result:
            try:
                title, desc, price = result
                gpu = GPU.parse(title + desc, int(price))
                correct_records_buffer.append(vars(gpu).values())
                pbar.update(1)
                correct_records_count += 1
                wrong_records_count = 0
            except GPUInitError:
                wrong_records_count += 1
        else:
            wrong_records_count += 1

    pbar.set_description(f"已獲得: {correct_records_count} 不可用: {wrong_records_count} ")


def can_stop_crawling() -> bool:
    global correct_records_count
    global wrong_records_count
    # 已經抓到需要數量筆的資料 或者 錯誤資料累積量 > 10
    return (correct_records_count >= EXPECTED_RECORDS) or wrong_records_count > 10


if __name__ == "__main__":

    # 設定 Options
    options = Options()
    set_options(options)

    # 創建 Driver 實例 (如果需更新/重新安裝，第一次執行會失敗)
    driver = get_driver("Chrome", options=options)
    driver.get(PCHOME_URL)
    
    # csv 檔案路徑
    file = CSV(SCRIPT_DIR / "results.csv")
    file.writerow(GPU.getattrs(), mode="wt")

    print(
        "---------------------------------------------- Web crawling starts -----------------------------------------------"
    )
    try:
        # 試圖等待第一個頭區塊刷新出來
        beginning_block: WebElement = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "col3f"))
        )
    except Exception:
        raise CrawlingError(
            "main program", "Cannot find the element with class='col3f'."
        )

    with tqdm(total=EXPECTED_RECORDS, colour="green", unit=" records") as pbar:
        while True:
            if can_stop_crawling():
                break
            else:
                try_converting_to_record(beginning_block, pbar)
            # 2 倍滾動距離，確保觸發 <div id="ScrollNav"></div> 讓資料繼續刷新
            driver.execute_script(f"window.scrollBy(0, {1.5 * NEXT_BLOCKS * HEIGHT})")
            try:
                # 頭區塊後再挖 n 個區塊出來
                blocks = beginning_block.find_elements(
                    By.XPATH, f"following-sibling::*[position() <= {NEXT_BLOCKS}]"
                )
                # 下個頭區塊
                beginning_block = blocks[-1].find_element(
                    By.XPATH, "following-sibling::*[1]"
                )
                # 處理每個區塊
                for block in blocks:
                    if can_stop_crawling():
                        break
                    else:
                        try_converting_to_record(block, pbar)
            except IndexError:
                raise CrawlingError("main program", "blocks are empty.")
            except NoSuchElementException:
                raise CrawlingError("main program", "找不到下個頭筆資料")

            # 休息，並在這段期間將資料寫入
            file.writerows(correct_records_buffer, mode="at")
            correct_records_buffer.clear()
            time.sleep(random.uniform(1, 3) * SLEEP)
    print(
        "----------------------------------------------- Web crawling ends ------------------------------------------------"
    )

    driver.close()
    driver.quit()
