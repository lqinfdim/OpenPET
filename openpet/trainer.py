import torch
import numpy as np
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader

import os
import time
from typing import Dict, List, Optional, Tuple


__all__ = ["Trainer"]

class Trainer:
    
    def __init__(
        self,
        model : nn.Module,
        optimizer: optim.Optimizer,
        data_loader : DataLoader,
        max_epochs : int
    ) -> None:
        
        self.model = model
        self.optimizer = optimizer
        self.data_loader = data_loader
        
        self._hook = []