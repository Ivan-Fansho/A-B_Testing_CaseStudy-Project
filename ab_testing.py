import numpy as np
import pandas as pd


# Simulating Click Data for A/B Testing

N_A = 10000
N_B = 10000

# Generating Click Data
click_A = pd.Series(np.random.binomial(1,0.2,size = N_A))
click_B = pd.Series(np.random.binomial(1,0.5,size = N_B))


# Generate Group Identifier
con_id = pd.Series(np.repeat("A", N_A))
exp_id = pd.Series(np.repeat("B", N_B))

df_A = pd.concat([click_A,con_id],axis = 1)
df_B = pd.concat([click_B,exp_id],axis = 1)

df_A.columns = ["click", "group"]
df_B.columns = ["click", "group"]


df_ab_test = pd.concat([df_A, df_B], axis=0).reset_index(drop=True)
print(df_ab_test)
df_ab_test.to_csv("ab_test_data.csv", index=False)
