# standard library
import inspect
import re

# local library
from .company import MFR, OEM
from .exception import GPUInitError
from parameters.constants import MFR_TABLE, OEM_TABLE, PREFIX_TABLE, MFR_INFO


class GPU:
    def __init__(
        self,
        mfr: MFR,
        oem: OEM | None,
        prefix: str,
        name: str,
        suffix: str | None,
        vram: int | None,
        gddr: int | None,
        price: int,
    ):
        """GPU 資訊

        Parameters
        ----------
        + `mfr`    (MFR)        : 製造商
        + `oem`    (OEM | None) : 如果沒有 OEM，就表示是公版卡
        + `prefix` (str)        : 例如 "RTX 3060 Ti" 的 prefix 為 RTX
        + `name`   (str)        : 例如 "RTX 3060 Ti" 的 name 為 3060
        + `suffix` (str | None) : 例如 "RTX 3060 Ti" 的 suffix 為 Ti
        + `vram`   (int | None) : 單位 GB
        + `gddr`   (int | None) : GDDR
        + `price`  (int)        : 新台幣 (NT Dollars)
        """
        self.manufacturer = mfr
        self.oem = oem
        self.prefix = prefix
        self.name = name
        self.suffix = suffix
        self.vram = vram
        self.gddr = gddr
        self.price = price

    @classmethod
    def parse(cls, text: str, price: int) -> "GPU":
        """GPU 的工廠方法，分析文字取得 GPU 資訊

        Parameters
        ----------
        + `text`  (str) : 文字
        + `price` (int) : 價格

        Returns
        -------
        + (GPU) : GPU 資訊
        
        Exceptions
        ----------
        + `GPUInitError` :
            若非目標顯卡，或者格式不正確，引發該錯誤。例如 "GTX1660S"。
        """

        if "+" in text:
            raise GPUInitError("綑綁銷售，夾帶私貨")
        if "DIY" in text:
            raise GPUInitError("套裝機")

        # 先轉大寫
        text = text.upper()

        # 嘗試找出製造商，要不然先設為 None
        for m in MFR_TABLE:
            if (m.name.upper() in text or m.value in text):
                mfr = m.name
                break
        else:
            mfr = None

        # 嘗試找出OEM，要不然設為 None
        for o in OEM_TABLE:
            if (o.name.upper() in text or o.value in text):
                oem = o.value
                break
        else:
            oem = None

        # 嘗試找出 prefix
        # 並找出 prefix 後一個的 index
        for p in PREFIX_TABLE:
            p_index = text.find(p.upper())
            if p_index != -1:
                prefix = p
                p_index += len(p)
                break
        else:
            raise GPUInitError("不可能沒有 prefix")

        # 如果找不到製造商，利用 prefix 判斷製造商
        if mfr is None:
            for m, info in MFR_INFO.items():
                if prefix in info.keys():
                    mfr = m

        # 製造商和 prefix 必然都有，嘗試找出 name
        for n in MFR_INFO[mfr][prefix].keys():
            n_index = text.find(n.upper(), p_index)
            if n_index != -1:
                name = n
                n_index += len(name)
                break
        else:
            raise GPUInitError("不可能沒有 name")

        # 嘗試找出 suffix
        for s in MFR_INFO[mfr][prefix][name]:
            # 先試試看有沒有辦法找到後綴
            if s is not None and text.find(s.upper(), n_index) != -1:
                suffix = s
                break
        else:
            if None in MFR_INFO[mfr][prefix][name]:
                # 它沒有後綴
                suffix = None
            else:
                # 否則這個顯卡必然有後綴
                # 如存在 RX 7900 XT / RX 7900 XTX 兩顯卡
                # 但並未存在 RX 7900 這張顯卡
                raise GPUInitError("不可能沒有 suffix")

        vram = re.search("(\d+)GB", text)
        if vram is not None:
            vram = int(vram.group(1))
        gddr = re.search("G?DDR(\d+)", text)
        if gddr is not None:
            gddr = int(gddr.group(1))

        return cls(mfr, oem, prefix, name, suffix, vram, gddr, price)

    @classmethod
    def getattrs(cls) -> tuple[str]:
        """獲得這個類別實例的所有屬性

        Parameters
        ----------
        ...

        Returns
        -------
        (tuple[str]) : instance attributes
        """
        return tuple(attr for attr in inspect.signature(cls.__init__).parameters.keys() if attr != 'self')

    def __str__(self):
        return "\n".join(
            [
                f"Manufacturer : {self.manufacturer}",
                f"OEM          : {self.oem}",
                f"Prefix       : {self.prefix}",
                f"Name         : {self.name}",
                f"Suffix       : {self.suffix}",
                f"VRAM         : {self.vram} GB",
                f"GDDR         : {self.gddr}",
                f"Price        : ${self.price}",
            ]
        )
