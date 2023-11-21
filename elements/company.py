# standard library
from enum import Enum


class MFR(Enum):
    """製造商名稱

    + name  是英文名稱
    + value 是中文名稱
    """
    NVIDIA = "輝達"
    AMD    = "超微"
    Intel  = "英特爾"


class OEM(Enum):
    """OEM名稱

    + name  是英文名稱
    + value 是中文名稱
    """
    ASUS     = "華碩"
    MSI      = "微星"
    GIGABYTE = "技嘉"
    ZOTAC    = "索泰"
    INNO3D   = "映眾"
    SPARKLE  = "撼與"
    ASROCK   = "華擎"
    