# Libs necessárias
import pandas as pd
import numpy as np

# Lib grafica
import matplotlib.pyplot as plt
import seaborn as sns

# Avisos
import warnings
warnings.filterwarnings('ignore')

def Config():
    # Configuracoes panda
    pd.set_option('display.max_rows', 200)
    pd.set_option('display.max_colum', 100)

    # Configuracoes Matplotlib
    plt.rcParams['figure.figsize'] = (15,6)
    plt.style.use('seaborn-darkgrid')

def ReadingData(path):
    Config()
    
    data = pd.read_csv(path)
    data.drop( columns=['fire insurance (R$)', 'total (R$)'], inplace=True)
    return data

def ShowColums(base_path):
    Colunas_Categoricas = base_path.columns[ base_path.dtypes == object ]
    Colunas_Numericas = base_path.columns[ base_path.dtypes != object ]
    print(Colunas_Categoricas, Colunas_Numericas, sep="\n")

