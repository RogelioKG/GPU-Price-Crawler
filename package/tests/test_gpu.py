# local library
from package.components.gpu import GPU

def main() -> None:
    title, desc, price = ("Intel Arc A750 8G 顯示卡", "Intel Arc A750 8G 顯示卡 pci-e 4.0 8gb gddr6 dp hdmi", "6990")
    gpu = GPU.parse(title + desc, int(price))
    print(gpu)
    print(gpu.jsonify())

def test_cached_speed(times: int):
    for _ in range(times):
        a = GPU.columns

def test_no_cached_speed(times: int):
    for _ in range(times):
        a = GPU.columns()
