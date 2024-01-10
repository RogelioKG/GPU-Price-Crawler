# local library
from package.parameters.variables import MFR_INFO
from package.components.company import MFR

def main() -> None:
    print(MFR_INFO[MFR.NVIDIA.name]["GTX"])
    # {'1050': ['Ti'], '1650': [''], '1660': ['Super']}

    print(MFR_INFO[MFR.NVIDIA.name]["GTX"]["1660"])
    # ['Super']

    print(MFR_INFO[MFR.NVIDIA.name].keys())
    # dict_keys(['GTX', 'RTX'])

    print(MFR_INFO[MFR.NVIDIA.name]["GTX"].keys())
    # dict_keys(['1050', '1650', '1660'])

    print("" in MFR_INFO[MFR.NVIDIA.name]["GTX"]["1660"])
    # False (RTX GTX 1660 是否有可能無後綴)

    print("" in MFR_INFO[MFR.NVIDIA.name]["RTX"]["4070"])
    # True (RTX 4070 是否有可能無後綴)
    
    print([*MFR_INFO.keys()])
    # ['NVIDIA', 'AMD', 'Intel']
