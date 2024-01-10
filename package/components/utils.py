# standard library
import csv
from functools import cache
from pathlib import Path
from typing import Iterable, Any

def cached_class_property(func):
    """快取類別屬性裝飾器，只要存取一次後就會 cache 起來。"""
    # 這裡之所以不使用 cached_property，是因為我們需要的是類別層級的快取，
    # 而不是實例層級的快取 (導致每次創建實例都要重新快取一次，有和沒有一樣)。
    return classmethod(property(cache(func)))

class CSV:
    """CSV 讀寫簡易介面"""

    def __init__(self, filepath: Path):
        """
        Parameters
        ----------
        + `filepath` (Path) : 檔案路徑
        """
        self.filepath = filepath

    def read(self) -> list[tuple[str]]:
        with open(self.filepath, mode="r", encoding="utf-8") as csv_file:
            rows = csv.reader(csv_file)
            return [tuple(row) for row in rows]

    def writerow(self, row: Iterable[Any], mode: str) -> None:
        with open(self.filepath, mode=mode, encoding="utf-8", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(row)

    def writerows(self, row: Iterable[Iterable[Any]], mode: str) -> None:
        with open(self.filepath, mode=mode, encoding="utf-8", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(row)
