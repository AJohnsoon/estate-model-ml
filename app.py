import pandas as pd
import matplotlib.pyplot as plt
import grid_model

# Ignore Warning
import warnings
warnings.filterwarnings('ignore')

def Config():
    # Configuracoes pandas
    pd.set_option('display.max_rows', 200)
    pd.set_option('display.max_colum', 100)

    # Configuracoes Matplotlib
    plt.rcParams['figure.figsize'] = (15,6)
    plt.style.use('seaborn-darkgrid')

def data_analysis(base_path):
    Config()    
    try:
        data = pd.read_csv(base_path)
        grid_model.grid(data)
        plt.subplots_adjust(top=1.15, hspace=0.3)
        plt.show()
    except:
        print('Error on reading or loading file in BASE_PATH')