# GPU-Price-Crawler

![crawler-short](package/tests/crawler-short.gif)

## Brief

小作業，PChome 爬蟲，爬下顯卡製造商、OEM、價格等等的資訊，並整理成 CSV 格式表格。

可以自訂想要爬的顯卡 (*constants.py*)、要抓的目標數量與爬蟲速度 (*variables.py*) 等等。

腳本在 *main.py*，直接執行即可。結果會直接產出在頂層目錄。

*test_entry.py* 與 *tests* 僅作為單元測試之用途。

## Murmuring

+ 嘗試使用 EAFP 的設計風格 (Easier to Ask Forgiveness Than Permission，請求寬恕比請求許可更容易)

## Run Script

```bash
py main.py
```

