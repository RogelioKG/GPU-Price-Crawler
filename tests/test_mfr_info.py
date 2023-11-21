from parameters.constants import MFR_INFO
from elements.company import MFR

def main() -> None:
    print(MFR_INFO[MFR.NVIDIA.name]["GTX"])
    # {'1050': ['Ti'], '1650': [None], '1660': ['Super']}

    print(MFR_INFO[MFR.NVIDIA.name]["GTX"]["1660"])
    # ['Super']

    print(MFR_INFO[MFR.NVIDIA.name].keys())
    # dict_keys(['GTX', 'RTX'])

    print(MFR_INFO[MFR.NVIDIA.name]["GTX"].keys())
    # dict_keys(['1050', '1650', '1660'])

    print(None in MFR_INFO[MFR.NVIDIA.name]["GTX"]["1660"])
    # False (RTX GTX 1660 是否有可能無後綴)

    print(None in MFR_INFO[MFR.NVIDIA.name]["RTX"]["4070"])
    # True (RTX 4070 是否有可能無後綴)
    
    print([*MFR_INFO.keys()])
    # ['NVIDIA', 'AMD', 'Intel']