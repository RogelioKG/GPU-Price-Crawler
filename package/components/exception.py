# third party library
import colorama

# local library
from package.components.utils import make_hr_message

class SimpleError(Exception):
    def __init__(self, location: str, message: str):
        """這純粹是寫給自己看的，其在發生錯誤時，指出錯誤發生的位置並"簡單"描述錯誤之所以造成的可能原因。

        Parameters
        ----------
        + `location` (str) : 發生位置
        + `message` (str) : 錯誤發生的可能原因
        """
        err = f"Error in {location}:\n\t{message}"
        hr_stars = make_hr_message("", hr_char="*", color=colorama.Fore.YELLOW)
        super().__init__("\n" + "\n".join([hr_stars, err, hr_stars]))

class CrawlingError(SimpleError):
    def __init__(self, message: str):
        """錯誤源於爬蟲過程

        Parameters
        ----------
        + `message` (str) : 錯誤發生的可能原因
        """
        super().__init__("Web Crawling", message)


class GPUInfoInitError(SimpleError):
    def __init__(self, message: str):
        """錯誤源於 GPU 實例初始化

        Parameters
        ----------
        + `message` (str) : 錯誤發生的可能原因
        """
        super().__init__("GPU Info Initialization", message)
