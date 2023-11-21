# standard library
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException


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
