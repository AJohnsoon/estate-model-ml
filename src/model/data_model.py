import pandas as pd
import numpy as np

# Lib graphic
import matplotlib.pyplot as plt
import seaborn as sns

# Ignore Warning
import warnings
warnings.filterwarnings('ignore')

def Config():
    # Configuracoes panda
    pd.set_option('display.max_rows', 200)
    pd.set_option('display.max_colum', 100)

    # Configuracoes Matplotlib
    plt.rcParams['figure.figsize'] = (15,6)
    plt.style.use('seaborn-darkgrid')

def DataAnalysis(base_path):
    Config()    
    try:
        data = pd.read_csv(base_path)
        data.drop( columns=['fire insurance (R$)', 'total (R$)'], inplace=True)
        data.loc[ data['floor'] == '301']
        data.iloc[ 2562, 5] = 30

        data['floor'] = data['floor'].apply( lambda line_id : 0 if line_id == '-' else line_id)
        data['floor'] = pd.to_numeric( data['floor'] )

        # categorical_column  = data.columns[ data.dtypes == object ]
        numeric_column = data.columns[ data.dtypes != object ]

        # for Column in categorical_column:
        #     Analise = data[Column].value_counts( normalize=True ) * 100
        #     print(Analise)

        for Column in numeric_column:
            Analise = data[Column].value_counts( normalize=True ) * 100
            print(Analise)

    #   Grid Info
        Fig, Line = plt.subplots(figsize=(3, 8))
        backgroud_color = '#f5f5f5'
        Fig.set_facecolor(backgroud_color)
        sns.color_palette('flare', len(numeric_column) * 2)
        plt.suptitle('Numeric Variables', fontsize=22, color='#404040', fontweight=100)

        rows = 7
        column = 2 #(boxplot, distplot)
        position = 1 
        for c in numeric_column:
            base_date = data
            plt.subplots(rows, column)
            sns.boxplot( data=base_date, y=c )
            position += 1

            plt.subplots(rows, column)
            sns.displot( data=base_date, y=c)
            position += 1
            
            plt.subplots_adjust( top=1.15, hspace=0.3)
            plt.show()
    except:
        print('Error reading file')

