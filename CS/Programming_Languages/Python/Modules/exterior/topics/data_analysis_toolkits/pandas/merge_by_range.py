"""Best way to join / merge by range in pandas
https://stackoverflow.com/questions/44367672/best-way-to-join-merge-by-range-in-pandas
"""

import pandas as pd
import numpy as np

A = pd.DataFrame(dict(
    A_id=range(10),
    A_value=range(5, 105, 10)
))
B = pd.DataFrame(dict(
    B_id=range(5),
    B_low=[0, 30, 30, 46, 84],
    B_high=[10, 40, 50, 54, 84]
))

print(f"A:\n{A}\n")
print(f"B:\n{B}\n")

a = A.A_value.values
print(f"{type(a)}")
print(f"{len(a)}")
bh = B.B_high.values
bl = B.B_low.values

i, j = np.where((a[:, None] >= bl) & (a[:, None] <= bh))
print(f"i:\n{i}\n")
print(f"j:\n{j}\n")

res = pd.concat([
    A.loc[i, :].reset_index(drop=True),
    B.loc[j, :].reset_index(drop=True)
], axis=1)

print(f"res:\n{res}\n")
print(f"type(res): {type(res)}")

