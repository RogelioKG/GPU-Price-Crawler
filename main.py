# standard library
from pathlib import Path
import random
import time

# third party library
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement  # 網頁元素，find 回傳的資料結構
from selenium.webdriver.support.ui import WebDriverWait  # 掛機
from selenium.webdriver.support import expected_conditions as EC  # 預期元素
from selenium.common.exceptions import NoSuchElementException  # Exception 找不到元素
from tqdm import tqdm

# local library
from constants import (
    PCHOME_URL,
    HEIGHT,
    NEXT_BLOCKS,
    EXPECTED_BLOCKS,
    SCRIPT_DIR,
    SLEEP,
)
from init_webdriver import *
from crawling_functions import *
from accessor import *

# 收集到的資料
results = []

# 遺失的資料
lost_results = 0


def deal_with_block(block: WebElement, pbar: tqdm) -> None:
    global lost_results
    global results

    # 忽略滾動監控
    if block.get_attribute("id") != "ScrollNav":
        result = fetch_info(block)
        if result:
            results.append(result)
            pbar.update(1)
        else:
            lost_results += 1

    pbar.set_description(f"獲得: {len(results)} 損失: {lost_results} ")


if __name__ == "__main__":
    # 設定 Options
    options = Options()
    set_options(options)

    # 創建 Driver 實例
    driver = get_driver("Chrome", options=options)
    driver.get(PCHOME_URL)

    print(
        "--------------------------------------------------------------- Web crawling starts ----------------------------------------------------------------"
    )
    try:
        # 試圖等待第一個頭筆資料刷新出來
        beginning_block: WebElement = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "col3f"))
        )
    except Exception:
        print_error("main program", "Cannot find the element.")
        driver.quit()
        exit()
    with tqdm(total=EXPECTED_BLOCKS, colour="green", unit=" records") as pbar:
        while True:
            if len(results) >= EXPECTED_BLOCKS:
                break
            else:
                deal_with_block(beginning_block, pbar)
            # 1.5 倍滾動距離，確保觸發 <div id="ScrollNav"></div> 讓資料繼續刷新
            driver.execute_script(f"window.scrollBy(0, {1.5 * NEXT_BLOCKS * HEIGHT})")
            try:
                # 頭筆資料後再挖 n 筆資料出來
                blocks = beginning_block.find_elements(
                    By.XPATH, f"following-sibling::*[position() <= {NEXT_BLOCKS}]"
                )
                # 下個頭筆資料
                beginning_block = blocks[-1].find_element(
                    By.XPATH, "following-sibling::*[1]"
                )
                # 處理每個 blocks
                for block in blocks:
                    if len(results) >= EXPECTED_BLOCKS:
                        break
                    else:
                        deal_with_block(block, pbar)
            except IndexError:
                print_error("main program", "blocks are empty.")
                break
            except NoSuchElementException:
                print_error("main program", "找不到下個頭筆資料")
                break
            # 休息
            time.sleep(random.uniform(1, 3) * SLEEP)
    print(
        "---------------------------------------------------------------- Web crawling ends -----------------------------------------------------------------"
    )

    driver.close()
    driver.quit()

    # 爬到五個不符合標準的就停下來

    file = Csv(SCRIPT_DIR / "results.csv")
    file.writerow(("title", "description", "value"), mode="at")
    file.writerows(results, mode="at")
