import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 938988157 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    freedom = 1
    s = x.var(ddof=1)
    firstChi = chi2.ppf(alpha/2, 1)
    secondChi = chi2.ppf(1 - alpha/2, 1)
    return s / firstChi, s / secondChi
