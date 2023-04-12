import pandas as pd
import numpy as np
from scipy.stats import ks_2samp
from scipy.stats import cramervonmises_2samp
from scipy.stats import anderson_ksamp

chat_id = 285100540 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    p = 0.02
    test_stat, _ , p_value = anderson_ksamp([x, y])
  
    return p_value < p
      
