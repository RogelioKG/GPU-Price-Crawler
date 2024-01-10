# standard library
from pathlib import Path
import sys

# local library
from package.components.company import MFR, OEM
from package.parameters.variables import MFR_INFO

########################################################
# 使用者不應修改以下常數
########################################################


# PChome 顯卡
##############################################
PCHOME_URL = "https://ecshweb.pchome.com.tw/search/v3.3/?q=%E9%A1%AF%E7%A4%BA%E5%8D%A1"


# 執行腳本所在目錄
##############################################
SCRIPT_DIR = Path(sys.path[0])


# 一筆資料高度為 194
##############################################
HEIGHT = 194


# 製造商表
##############################################
MFR_TABLE = set(MFR)


# OEM 表
##############################################
OEM_TABLE = set(OEM)


# 前綴表
##############################################
PREFIX_TABLE: set[str] = set()
for info in MFR_INFO.values():
    for prefix in info.keys():
        PREFIX_TABLE.add(prefix)
