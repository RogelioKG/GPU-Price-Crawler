# standard library
from pathlib import Path

# local library
from elements.accessor import Csv
from elements.gpu import GPU

def main() -> None:
    title, desc, price = ("Intel Arc A750 8G 顯示卡", "Intel Arc A750 8G 顯示卡 pci-e 4.0 8gb gddr6 dp hdmi", "6990")
    g = GPU.parse(title + desc, int(price))
    print(g)
    Csv(Path(__file__).parent / "results.csv").writerow(vars(g).values(), "wt")