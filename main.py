# standard library
import random
import time

# third party library
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement  # 網頁元素，find 回傳的資料結構
from selenium.webdriver.support.ui import WebDriverWait  # 掛機
from selenium.webdriver.support import expected_conditions as EC  # 預期元素
from selenium.common.exceptions import NoSuchElementException  # 找不到元素 Exception
from tqdm import tqdm  # 進度條 (酷)

# local library
from package.components.utils import CSV
from package.components.gpu import GPU
from package.components.exception import CrawlingError, GPUInitError
from package.parameters.variables import NEXT_BLOCKS, EXPECTED_RECORDS, SLEEP
from package.parameters.constants import PCHOME_URL, HEIGHT, SCRIPT_DIR
from package.services.crawling_functions import fetch_info
from package.services.init_webdriver import get_driver, set_options


# 正確資料緩衝區
correct_records_buffer = []

# 正確資料累積量
# (抓到且正確的資料)
total_correct_records = 0

# 錯誤資料累積量
# (抓到但不正確的資料 & 無法抓到的資料)
# (一旦 correct_records_buffer 有新添資料，清 0)
wrong_records_counter = 0


def try_converting_to_record(block: WebElement, pbar: tqdm) -> None:
    """試圖將 block 轉成一筆正確的 record 並附加進 correct_records_buffer

    Parameters
    ----------
    + `block` (WebElement) : 網頁元素
    + `pbar` (tqdm) : 進度條 (會更新進度條敘述)
    """
    global correct_records_buffer
    global total_correct_records
    global wrong_records_counter

    # 忽略滾動監控
    if block.get_attribute("id") != "ScrollNav":
        try:
            title, desc, price, link = fetch_info(block)
        except NoSuchElementException:
            # 無法抓到的資料
            wrong_records_counter += 1
        else:
            try:
                gpu = GPU.parse(title + desc, int(price), link)
                correct_records_buffer.append(gpu.jsonify().values())
                pbar.update(1)
                # 抓到且正確的資料
                total_correct_records += 1
                # 清 0
                wrong_records_counter = 0
            except GPUInitError:
                # 抓到但不正確的資料
                wrong_records_counter += 1

        pbar.set_description(
            f"已獲得: {total_correct_records} 不可用: {wrong_records_counter} "
        )


def can_stop_crawling() -> bool:
    """(已經抓到需要數量筆的資料) or (錯誤資料累積量 > 20)，停止爬蟲

    Returns
    -------
    (bool) : 是否要停止爬蟲
    """
    global total_correct_records
    global wrong_records_counter

    return (total_correct_records >= EXPECTED_RECORDS) or (wrong_records_counter > 20)


if __name__ == "__main__":
    # csv 檔案路徑
    file = CSV(SCRIPT_DIR / "results.csv")
    # 先寫入欄位名稱
    file.writerow(GPU.columns, mode="wt")

    # 設定 Options
    options = Options()
    set_options(options)

    # 創建 Driver 實例 (如果需更新/重新安裝，第一次執行有可能會失敗)
    driver = get_driver("Chrome", options=options)

    print("---------------------------------------------- Web crawling starts -----------------------------------------------")
    # 加載網頁
    driver.get(PCHOME_URL)
    try:
        # 試圖等待第一個頭區塊刷新出來
        beginning_block: WebElement = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "col3f"))
        )
    except Exception:
        raise CrawlingError("main.py", "Cannot find the element with class='col3f'.")
    with tqdm(total=EXPECTED_RECORDS, colour="green", unit=" records") as pbar:
        while True:
            if can_stop_crawling():
                break
            else:
                try_converting_to_record(beginning_block, pbar)
            # 1.5 倍滾動距離，確保觸發 <div id="ScrollNav"></div> 讓資料繼續刷新
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
            except NoSuchElementException:
                raise CrawlingError("main.py", "Cannot find the next beginning block.")
            except IndexError:
                raise CrawlingError("main.py", "Blocks are empty.")
            else:
                # 處理每個區塊
                for block in blocks:
                    if can_stop_crawling():
                        break
                    else:
                        try_converting_to_record(block, pbar)
                # 將資料寫入並休息
                file.writerows(correct_records_buffer, mode="at")
                correct_records_buffer.clear()
                time.sleep(random.uniform(1, 3) * SLEEP)
    print("----------------------------------------------- Web crawling ends ------------------------------------------------")
    
    # Driver 實例關閉
    driver.close()
    driver.quit()
