
import pandas as pd

data = {
    'IssuerGroup': ['Ggl', 'Sup'],
    'Triparty': [9.5, 11.1],
    'Bilateral': [11, 13],
    'Swp': [1.5, 1.5],
    'Issuer': ['Jj', 'Sf']
}

df = pd.DataFrame(data)
print(df)
output = df.melt(id_vars=['IssuerGroup', 'Issuer'], value_vars=['Triparty', 'Bilateral', 'Swp'],
                 var_name='InterestType', value_name='SpreadBPS')

print(output)

