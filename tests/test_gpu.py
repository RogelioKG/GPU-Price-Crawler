# standard library

# local library
from components.gpu import GPU

def main() -> None:
    title, desc, price = ("Intel Arc A750 8G 顯示卡", "Intel Arc A750 8G 顯示卡 pci-e 4.0 8gb gddr6 dp hdmi", "6990")
    print(GPU.parse(title + desc, int(price)))
    print(GPU.getattrs())
