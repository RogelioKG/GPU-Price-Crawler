# standard library
from pathlib import Path
import sys


PCHOME_URL = "https://ecshweb.pchome.com.tw/search/v3.3/?q=%E9%A1%AF%E7%A4%BA%E5%8D%A1"

# 一筆資料高度為 194
HEIGHT = 194

# 頭筆資料之後再抓 10 筆資料
NEXT_BLOCKS = 10

# 要抓 50 筆資料
EXPECTED_BLOCKS = 50

# 執行腳本所在目錄
SCRIPT_DIR = Path(sys.path[0])

# 抓完一輪 (頭筆資料 + 後 10 筆資料) 的最短休息時間 (s)
SLEEP = 0.5
