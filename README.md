# GPU-Price-Crawler
Last Update: 2024/1/20

![crawler-short](package/tests/crawler-short.gif)

## Brief

PChome 爬蟲，爬下顯卡的製造商、OEM、價格等等資訊，並整理於 CSV 檔。

可自訂想要爬的顯卡 (*constants.py*)、要抓的目標數量與爬蟲速度 (*variables.py*) 等等。

腳本於 *main.py*。結果會直接產出在頂層目錄。

*test_entry.py* 與 *tests* 僅作為單元測試之用途。

## Murmuring

+ 嘗試使用 EAFP 的設計風格 (Easier to Ask Forgiveness Than Permission，請求寬恕比請求許可更容易)

## Run Script

+ 建立虛擬環境
   ```bash
   pip install -r requirements.txt
   ```

+ 執行腳本
   ```bash
   run.bat
   ```

## To-do
+ [ ] pytest / unittest 單元測試 (純練習)
+ [ ] CPU 價格爬蟲
+ [ ] 跨網站爬蟲
+ [ ] 異步編程 (async)
+ [ ] 後端資料庫系統
+ [ ] 前端 UI


## Note

+ `2024/1/10`
  + 新增 NVIDIA 顯卡 RTX 4070 Super & RTX 4070 Ti Super & RTX 4080 Super
  + GPU 新增 link 屬性

+ `2024/1/20`
  + colorama (CLI 色彩文字)
  + 水平分隔線與終端機等寬
  + 例外的重構 (in *exception.py*)
