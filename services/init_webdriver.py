# third party library
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager


def get_driver(browser: str, options: Options = Options()):
    """找出最新的 webdriver 版本並安裝，再也不用擔心版本問題！
    webdriver 將安裝在 "C:\\Users\\username\\.wdm" 這個目錄裡。

    Parameters
    ----------
    + `browser` (str) : 瀏覽器名稱 {"Chrome", "Edge", "Firefox", "IE"}
    + `options` (Options) : 選項

    Returns
    -------
    + `driver` (WebDriver) : WebDriver 實例
    """
    if browser == "Chrome":
        
        driver_path = ChromeDriverManager().install()
        driver = webdriver.Chrome(service=Service(driver_path), options=options)

    elif browser == "Edge":
        
        driver_path = EdgeChromiumDriverManager().install()
        driver = webdriver.Edge(service=Service(driver_path), options=options)

    elif browser == "Firefox":
        
        driver_path = GeckoDriverManager().install()
        driver = webdriver.Firefox(service=Service(driver_path), options=options)

    elif browser == "IE":
        
        driver_path = IEDriverManager().install()
        driver = webdriver.Ie(service=Service(driver_path), options=options)

    return driver


def set_options(options: Options) -> Options:
    """設定選項

    Parameters
    ----------
    `options` (Options) : 選項實例

    Returns
    -------
    (Options) : 選項實例
    """
    # 禁止錯誤日誌輸出到 console
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # INFO = 0 / WARNING = 1 / LOG_ERROR = 2 / LOG_FATAL = 3 (default is 0)
    options.add_argument("log-level=3")
    # 後臺運行
    options.add_argument("--headless")
    # 關閉 GPU 避免某些系統或是網頁出錯
    options.add_argument("--disable-gpu")
    # 禁用瀏覽器通知
    options.add_argument("--disable-notifications")


if __name__ == '__main__':
    url = "https://pypi.org/project/webdriver-manager/"
    driver = get_driver(browser="Chrome")
    driver.get(url)