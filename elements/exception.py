class CrawlingError(Exception):
    def __init__(self, location: str, message: str):
        """印出錯誤訊息

        Parameters
        ----------
        + `location` (str) : 發生位置
        + `message` (str) : 錯誤訊息 
        """  
        err = f"Error in {location}: {message}"
        super().__init__("\n" + "\n".join(["*"*len(err), err, "*"*len(err)]))


class GPUInitError(CrawlingError):
    def __init__(self, message: str):
        """印出錯誤訊息

        Parameters
        ----------
        + `message` (str) : 錯誤訊息 
        """  
        super().__init__("GPU", message)
