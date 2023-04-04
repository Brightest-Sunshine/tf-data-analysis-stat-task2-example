import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 453878141

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    n = len(x)
    var = np.var(x)
    left = np.sqrt((n - 1) * var / (12 * chi2.ppf(1 - alpha / 2, n - 1)))
    right = np.sqrt((n - 1) * var / (12 * chi2.ppf(alpha / 2, n - 1)))
    return left, right
