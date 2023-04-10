import pandas as pd
import numpy as np


chat_id = 706100023 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
from scipy.stats import f

# Входные данные
data1 = x
data2 = y

# Вычисление дисперсий
var1 = np.var(data1, ddof=1)
var2 = np.var(data2, ddof=1)

# Вычисление статистического показателя
f_stat = var1 / var2

# Вычисление критического значения
alpha = 0.08
df1 = len(data1) - 1
df2 = len(data2) - 1
critical_value = f.ppf(1 - alpha, df1, df2)

# Проверка гипотезы
if f_stat > critical_value:
    rez = 1 #Выборки неоднородны - да отклонить гипотезу однородности - да
else:
    rez = 0 #Выборки однородны - да отклонить гипотезу однородности - да
return bool(rez)
