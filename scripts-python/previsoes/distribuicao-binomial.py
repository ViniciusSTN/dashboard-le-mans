import pandas as pd
from scipy.stats import binom 

resultado = round((binom.pmf(3,10,0.2087) * 100), 2) 

dados = [{
    'Numero de sucessos desejado': 3,
    'Numero de realizações': 10,
    'Probabilidade de sucesso em uma tentativa': 0.2087,
    'Resultado': resultado
}]

distribuicao_binomial = pd.DataFrame(dados)
