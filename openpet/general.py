from .pet_models.adapter import AdapterModel
from .pet_models.lora import LoraModel
from .pet_models.bitfit import BitFitModel


PEF_MODELS = {
    "adapter" : AdapterModel,
    "lora" : LoraModel,
    "bitfit" : BitFitModel   
}


def init_pet_model(model, pet_method):
    
    if pet_method not in PEF_MODELS.keys():
        raise ValueError("Unsupported PET method,\
                         call function list_pet_method() to list current available PET methods")
        
    pet_class = get_pet_class_by_name(pet_method)
    pet_module = pet_class(model)
    
    return pet_module
    
        
def get_pet_class_by_name(pet_name):
    return PEF_MODELS[pet_name]


def list_supported_models(pet_method = None):
    pass



def list_pet_method():
    
    print("Current Supported Method")
    print("---------------------------------")
    sp = list(PEF_MODELS.keys())
    
    for each in sp:
        print(f"{str(each)}")
