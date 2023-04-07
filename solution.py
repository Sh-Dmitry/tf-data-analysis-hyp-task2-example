import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 285100540 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    p = 0.02
    res = ks_2samp(x, y)
    pval = res[1]
    if pval >= p:
        return False
    else:
        return True
