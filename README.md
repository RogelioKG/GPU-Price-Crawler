# GPU-Price-Crawler
<!-- Badges -->
![Version: 0.2.0](https://img.shields.io/badge/version-0.2.0-blue)
[![Python: 3.11.4](https://img.shields.io/badge/python-3.11.4-blue)](https://www.python.org/downloads/release/python-3114/ "More details about Python 3.11.4")
![Last Update: 2024/1/20](https://img.shields.io/badge/last%20update-2024/1/20-darkgreen)
[![Licence: MIT](https://img.shields.io/github/license/RogelioKG/GPU-Price-Crawler)](./LICENSE)


## Brief
PChome 爬蟲，爬下顯卡的製造商、OEM、價格等等資訊，並整理於 CSV 檔。
+ `variables.py`：自訂想要爬的顯卡、要抓的總數量與爬蟲速度等等。
+ `main.py`：執行腳本入口。結果會直接產出在頂層目錄。
<!-- GIF -->
![crawler-short](package/tests/crawler-short.gif)


## Run Script
+ 建立虛擬環境
   ```bat
   pip install -r requirements.txt
   ```
+ 執行腳本
   ```bat
   run.bat
   ```


## Changelog
> See notable changes to this project in [CHANGELOG.md](./CHANGELOG.md).
