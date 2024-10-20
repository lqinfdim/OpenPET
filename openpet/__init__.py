
__version__ = "0.0.1"

class GlobalSetting:
    def __init__(self):
        self.axis_order = [0,1,2]


global_setting = GlobalSetting()

from .pet_configs import BasePETConfig
from .utils import logging
from .utils.saving_loading_utils import SaveLoadMixin
from .basemodel import PETBase
from .auto_pet import AutoPETConfig, AutoPETModel
from .utils.structure_mapping import CommonStructureMap
from .pet_models.lora import LoraModel
from .pet_models.bitfit import BitFitModel
from .pet_models.compacter import CompacterModel
from .pet_models.adapter import AdapterModel
from .pet_models.prefix import PrefixModel
from .pet_models.soft_prompt import SoftPromptModel
from .pet_models.low_rank_adapter import LowRankAdapterModel
from .pet_models.parallel_adapter import ParallelAdapterModel


from .general import list_pet_method



def set_axis_order(axis_order=[0,1,2]):
    setattr(global_setting, "axis_order", axis_order)