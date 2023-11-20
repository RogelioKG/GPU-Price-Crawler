# third party library
from dataclasses import dataclass


@dataclass(frozen=True)
class Manufacturer:
    """製造商資訊

    Parameters
    ----------
    + `chinese_name` (str)            : 中文名稱
    + `english_name` (str)            : 英文名稱
    + `series` (...) : {前綴 (prefix): {名稱 (name): 後綴 (suffix)}}
    """

    chinese_name: str
    english_name: str
    series: dict[str, dict[str, str | None]]


NVIDIA = Manufacturer(
    "輝達",
    "NVIDIA",
    {
        "GTX":
        {
            "10": {"50", "Ti"},
            "16": {"50", "Ti"},
        },
        
        "RTX": {"1050": ["Ti"]},
    },
)


AMD = Manufacturer("超微", "AMD", {"": [""]})
INTEL = Manufacturer("英特爾", "Intel", {"": [""]})
