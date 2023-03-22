import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def grid(data):
    # Grid Info
    numeric_column = data_column(data)
    Fig, Line = plt.subplots(figsize=(3, 8))
    backgroud_color = '#f5f5f5'
    Fig.set_facecolor(backgroud_color)
    color_palette = sns.color_palette('flare', len(numeric_column) * 2)
    plt.suptitle('Numeric Variables', fontsize=22, color='#404040', fontweight=100)

    rows = 7
    columns = 2 #(boxplot, displot)
    position = 1 

    for column in numeric_column:
        try:
            base_data = data
            # base_data.loc[base_data['area'] <= 500]['area'].describe()

            plt.subplots(rows, columns)
            plt.title(f'{column}'.upper(), loc='left', fontsize=14, fontweight=200)
            sns.boxplot(data=base_data, y=column, showmeans=True, saturation=0.5, linewidth=1, color=color_palette[position] ,width=0.25)
            position += 1

            plt.subplots(rows, columns)
            plt.title(f'{column}'.upper(), loc='left', fontsize=14, fontweight=200)
            sns.displot(data=base_data[column], color=color_palette[position -1])
            position += 1

        except:
            print("[Error]: Parameter null or empty!")

def data_column(data):
    try:
        data.drop( columns=['fire insurance (R$)', 'total (R$)'], inplace=True)
        data.loc[ data['floor'] == '301']
        data.iloc[ 2562, 5] = 30
        data['floor'] = data['floor'].apply( lambda line_id : 0 if line_id == '-' else line_id)
        data['floor'] = pd.to_numeric( data['floor'] )

        numeric_column = data.columns[ data.dtypes != object ]
        
        for Column in numeric_column:
            Analise = data[Column].value_counts( normalize=True ) * 100
            print(Analise)
        
        return numeric_column

        # categorical_column  = data.columns[ data.dtypes == object ]

        # for Column in categorical_column:
        #     Analise = data[Column].value_counts( normalize=True ) * 100
        #     print(Analise)
    except:
        print("[Error] Problem to reading row or column data from database")