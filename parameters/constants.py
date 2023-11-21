# standard library
from pathlib import Path
import sys

# local library
from elements.company import MFR, OEM


# PChome 顯卡
PCHOME_URL = "https://ecshweb.pchome.com.tw/search/v3.3/?q=%E9%A1%AF%E7%A4%BA%E5%8D%A1"

# 執行腳本所在目錄
SCRIPT_DIR = Path(sys.path[0])

# 一筆資料高度為 194
HEIGHT = 194

# 要抓的顯卡
MFR_INFO: dict[str, dict[str, dict[str, list[str | None]]]]
MFR_INFO =  {
                MFR.NVIDIA.name:
                {
                    "GTX":
                    {
                        "1050": ["Ti"],
                        "1650": ["Ti", None],
                        "1660": ["Super"],
                    },
                    "RTX":
                    {
                        "3050": [None],
                        "3060": ["Ti", None],
                        "3070": [None],
                        "4060": ["Ti", None],
                        "4070": ["Ti", None],
                        "4080": [None],
                        "4090": [None],
                    },
                },
                MFR.AMD.name:
                {
                    "RX":
                    {
                        "6400": [None],
                        "6500": ["XT"],
                        "6600": [None],
                        "6650": ["XT"],
                        "7600": [None],
                        "7700": ["XT"],
                        "7800": ["XT"],
                        "7900": ["XT", "XTX"],
                    }
                },
                MFR.Intel.name:
                {
                    "Arc":
                    {
                        "A750": [None],
                        "A770": [None],
                    }
                }
            }

# 製造商表
MFR_TABLE = set(MFR)

# OEM 表
OEM_TABLE = set(OEM)

# 前綴表
PREFIX_TABLE: set[str] = set()
for info in MFR_INFO.values():
    for prefix in info.keys():
        PREFIX_TABLE.add(prefix)
