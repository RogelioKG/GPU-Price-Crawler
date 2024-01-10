# standard library
from pathlib import Path

# local library
from package.components.utils import CSV
from package.components.gpu import GPU

def main() -> None:
    title, desc, price, link = (
        "微星 GeForce RTX 4060 Ti VENTUS 2X BLACK 16G OC 顯示卡", 
        "16gb gddr6 torx fan 4.0 dlss 3", 
        "14990", 
        "https://24h.pchome.com.tw/prod/DRADLA-A900GJ7G3"
    )
    gpu = GPU.parse(title + desc, int(price), link)
    file = CSV(Path(__file__).parent / "results.csv")
    file.writerow(gpu.jsonify().keys(), "at")
    file.writerow(gpu.jsonify().values(), "at")
    file.writerow(gpu.jsonify().values(), "at")
