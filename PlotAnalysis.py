from cProfile import label
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("snap-0-20220318104904.txt")
sampling = 99
df.drop(index=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], axis=0, inplace=True)
df.columns = ['a']
new = df['a'].str.split("\t", expand=True)
df.drop(columns=["a"],inplace=True)
df["red"] = new[0]
df["ir"] = new[1]
print(df.head)

df["red"] = df["red"].astype(int)
df["ir"] = df["ir"].astype(int)

x = np.linspace(0, df.shape[0]/sampling, df.shape[0])
fig, ax = plt.subplots(figsize=(15,5))
lns1 = ax.plot(x, df.red, color='green', linewidth=1.0, label="red") 
ax.set_ylabel("red", fontsize = 15, weight = "bold")
ax2 = ax.twinx()
ax2.set_ylabel("ir", fontsize = 15, weight = "bold")
lns2 = ax2.plot(x, df.ir, color='red', linewidth=1.0, label = "ir") 
ax.set_xlabel("sec")
plt.title("TomasZavodnik - snap2", fontsize = 15, weight = "bold")
lns = lns1 + lns2
labs = ["red", "ir"]
ax.legend(lns, labs, loc=0)
plt.show()