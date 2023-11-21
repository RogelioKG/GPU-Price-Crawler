# standard library
from pathlib import Path
from typing import Iterable, Any

# third party library
import csv


class Csv():
    def __init__(self, filepath: Path):
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
