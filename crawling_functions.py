# standard library
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException


def print_error(location: str, message: str) -> None:
    """印出錯誤訊息

    Parameters
    ----------
    + `location` (str) : 發生位置
    + `message` (str) : 錯誤訊息 
    """
    error_message = f"Error in {location}: {message}"
    print("*" * len(error_message))
    print(error_message)
    print("*" * len(error_message))


def fetch_info(block: WebElement) -> tuple[str, str, int] | bool:
    """從一筆資料中抓取標題、敘述與價格

    Parameters
    ----------
    + `block` (WebElement) : 一筆資料

    Returns
    -------
    + (tuple[str, str, int] | bool)
        - 1. 找得到符合特定元素的資料，回傳 tuple
            - title (str) : 標題
            - desc (str) : 敘述
            - price (int) : 價格
        - 2. 找不到符合特定元素的資料，回傳 False
    """
    try:
        title_element = block.find_element(By.CLASS_NAME, "prod_name")
        title = title_element.text
        desc_element = block.find_element(By.CLASS_NAME, "nick")
        desc = desc_element.text
        price_element = block.find_element(By.CLASS_NAME, "value")
        price = int(price_element.text)

    except NoSuchElementException:
        return False

    return title, desc, price


# 一個你想抓的顯示卡，滿足三個條件
# 1. title 中沒有 "+" (有 "+" 表示夾帶私貨)
# 2. prefix 與 name 不為空

# 標題抓 img title="..."
# 說明抓 span class="nick" ...
# 價格抓 class="value"

