# third party library
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


def fetch_info(block: WebElement) -> tuple[str, str, int, str]:
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
        -  link (str) : 連結

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
    link = title_element.find_element(By.TAG_NAME, "a").get_attribute("href")

    return title, desc, price, link
