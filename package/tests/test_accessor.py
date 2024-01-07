# standard library
from pathlib import Path

# local library
from package.components.accessor import CSV
from package.components.gpu import GPU

def main() -> None:
    title, desc, price = ("Intel Arc A750 8G 顯示卡", "Intel Arc A750 8G 顯示卡 pci-e 4.0 8gb gddr6 dp hdmi", "6990")
    g = GPU.parse(title + desc, int(price))
    file = CSV(Path(__file__).parent / "results.csv")
    file.writerow(vars(g).keys(), "at")
    file.writerow(vars(g).values(), "at")
    file.writerow(vars(g).values(), "at")
