# standard library
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException


def fetch_info(block: WebElement) -> tuple[str, str, int]:
    """從一筆資料中抓取標題、敘述與價格

    Parameters
    ----------
    + `block` (WebElement) : 一塊網頁元素

    Returns
    -------
    + (tuple[str, str, int])
        - title (str) : 標題
        -  desc (str) : 敘述
        - price (int) : 價格

    Exceptions
    ----------
    + `NoSuchElementException` : 
        若是無法抓到的資料，引發該錯誤。
    """

    title_element = block.find_element(By.CLASS_NAME, "prod_name")
    title = title_element.text
    desc_element = block.find_element(By.CLASS_NAME, "nick")
    desc = desc_element.text
    price_element = block.find_element(By.CLASS_NAME, "value")
    price = int(price_element.text)

    return title, desc, price
