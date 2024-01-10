# local library
from package.components.company import MFR

##############################################
# 使用者可修改以下變數
##############################################


# 頭區塊之後再抓 10 個區塊
##############################################
NEXT_BLOCKS = 10


# 要抓 200 筆資料 (一個可抓到且格式正確的區塊，才是一筆正確的資料)
##############################################
EXPECTED_RECORDS = 200


# 抓完一輪 (頭區塊 + 後 10 個區塊) 的最短休息時間 (s)
##############################################
SLEEP = 1


# 要抓的顯卡
##############################################
MFR_INFO: dict[str, dict[str, dict[str, list[str]]]]
# CAUTION:
    # 沒有後綴的顯卡，一定要加上空字元 ""
# LAST UPDATE:
    # (2024/01/31) GeForce RTX 4080 Super
    # (2024/01/24) GeForce RTX 4070 Ti Super
    # (2024/01/07) GeForce RTX 4070 Super
MFR_INFO = {
    MFR.NVIDIA.name: {
        "GTX": {
            "1050": ["Ti"],
            "1650": ["Ti", ""],
            "1660": ["Super"],
        },
        "RTX": {
            "3050": [""],
            "3060": ["Ti", ""],
            "3070": [""],
            "4060": ["Ti", ""],
            "4070": ["Ti Super", "Ti", "Super", ""],
            "4080": ["Super", ""],
            "4090": [""],
        },
    },
    MFR.AMD.name: {
        "RX": {
            "6400": [""],
            "6500": ["XT"],
            "6600": [""],
            "6650": ["XT"],
            "7600": [""],
            "7700": ["XT"],
            "7800": ["XT"],
            "7900": ["XTX", "XT"],
        }
    },
    MFR.Intel.name: {
        "Arc": {
            "A750": [""],
            "A770": [""],
        }
    },
}
# 後綴一定要確保長字數在前面
for info in MFR_INFO.values():
    for pair in info.values():
        for suffix_list in pair.values():
            suffix_list.sort(key=len, reverse=True)
