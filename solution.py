import pandas as pd
import numpy as np
from scipy.stats import ks_2samp
from scipy.stats import anderson_ksamp
chat_id = 285100540 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    p = 0.02
    res = anderson_ksamp(x, y)
    pval = res.pvalue
    if pval >= p:
        return False
    else:
        return True
