# standard library
from enum import Enum, auto
import re


class Manufacturer(Enum):
    NVIDIA = "NVIDIA"
    AMD    = "AMD"
    Intel  = "INTEL"


class OEM(Enum):
    ASUS     = "華碩"
    MSI      = "微星"
    GIGABYTE = "技嘉"
    ZOTAC    = "索泰"
    INNO3D   = "映眾"
    SPARKLE  = "撼與"
    ASROCK   = "華擎"


# price 或許要獨立於 GPU 之外 (用 list[int] 儲存)
class GPU:
    def __init__(
        self,
        mfr: Manufacturer,
        oem: OEM | None,
        prefix: str,
        name: str,
        suffix: str | None,
        price: int,
        vram: int | None,
        gddr: int | None,
    ):
        """GPU 資訊，以下僅提須注意的參數

        Parameters
        ----------
        + `oem`    (str)        : 如果沒有 OEM，就表示是公版卡
        + `prefix` (str)        : 例如 -- RTX 3060 Ti 的 prefix 為 RTX
        + `name`   (str)        : 例如 -- RTX 3060 Ti 的 name 為 3060
        + `suffix` (str | None) : 例如 -- RTX 3060 Ti 的 suffix 為 Ti
        + `price`  (int)        : 新台幣 (NT Dollars)
        + `vram`   (int | None) : 單位 GB
        """
        self.manufacturer = mfr
        self.oem = oem
        self.prefix = prefix
        self.name = name
        self.suffix = suffix
        self.price = price
        self.vram = vram
        self.gddr = gddr

    @classmethod
    def parse(cls, title: str, desc: str, price: int) -> "GPU":
        """GPU 的工廠方法，分析標題、敘述與價格取得 GPU 資訊

        Parameters
        ----------
        + `title` (str) : 標題
        + `desc`  (str) : 敘述
        + `price` (int) : 價格

        Returns
        -------
        + (GPU) : GPU 資訊
        """
        # 先全轉大寫
        title = title.upper()
        desc = desc.upper()

        prefix = None
        name = None
        suffix = None

        # mfr: 先找製造商，找不到就利用顯卡名稱判斷
        mfr = [mfr.value in title + desc for mfr in Manufacturer]
        oem = None

        vram = None
        gddr = None

        return cls(mfr, oem, prefix, name, suffix, price, vram, gddr)

    def __str__(self):
        return "\n".join(
            [
                f"Manufacturer : {self.manufacturer}",
                f"OEM          : {self.oem}",
                f"Prefix       : {self.prefix}",
                f"Name         : {self.name}",
                f"Price        : NT${self.price}",
                f"VRAM         : {self.vram} GB",
                f"GDDR         : {self.gddr}",
            ]
        )

if __name__ == "__main__":
    title, desc, price = (
        'ZOTAC 索泰 GAMING GeForce GTX 1650 AMP Core GDDR6 顯示卡',
        '基於嶄新的 nvidia turing™ gpu 架構打造 配備快速 gddr6 記憶體 預設超頻加速 體積小巧 支援 4k 影像 70 毫米雙風扇 firestorm 程式',
        '3990'
    )
    # print(GPU.parse(title, desc, int(price)))