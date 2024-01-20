# standard library
import csv
import shutil
from functools import cache
from pathlib import Path
from typing import Iterable, Any

# third party library
import colorama


def cached_class_property(func):
    """快取類別屬性裝飾器，只要存取一次後就會 cache 起來。"""
    # 這裡之所以不使用 cached_property，是因為我們需要的是類別層級的快取，
    # 而不是實例層級的快取 (導致每次創建實例都要重新快取一次，有和沒有一樣)。
    return classmethod(property(cache(func)))


def make_hr_message(
    message: str,
    *,
    hr_char: str = "=",
    color: str = colorama.Fore.WHITE,
    weight: str = colorama.Style.BRIGHT
) -> str:
    """產生水平線分隔訊息 (與終端機齊寬)

    Parameters
    ----------
    `message` (str) : 訊息
    `hr_char` (str) : 水平線字元，預設為 -
    `color` (str) : 指定顏色 (ANSI escape sequences)，例如 `Fore.GREEN + Back.BLUE` 代表綠字藍底
    `weight` (str) : 字體重量 (ANSI escape sequences)，例如 `Style.BRIGHT` 代表粗體

    Returns
    -------
    (str) : 水平線分隔訊息
    """
    assert len(hr_char) == 1
    terminal_width, _ = shutil.get_terminal_size()
    half_width = (terminal_width - len(message)) // 2
    if 2 * half_width + len(message) == terminal_width - 1:
        return f"{weight}{color}{hr_char * (half_width + 1)}{message}{hr_char * half_width}{colorama.Style.RESET_ALL}"
    else:
        return f"{weight}{color}{hr_char * half_width}{message}{hr_char * half_width}{colorama.Style.RESET_ALL}"


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
