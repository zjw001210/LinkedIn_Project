import pandas as pd

# 
filename=['0_15735', '15735_31500', '31500_47250', '47250_63000', '63000_79000', 
    '79000_95000', '95000_110750','110750_122500', '122500_138235', '138235_154000',
    '154000_170000', '170000_185735', '185735_']


for i in range(len(filename[:1])):
    filepath_index='dataindex/{}dataindex.txt'.format(filename[i])
    filepath_all='data_all/{}data_all.xlsx'.format(filename[i])
    with open(filepath_index,'r',encoding='utf-8-sig') as f_index:
        index = f_index.readlines()
        index_list=[]
        for j in range(len(index)):
            index_list.append(int(index[j][:-1]))
    #print(index_list)


    df_all=pd.read_excel(filepath_all)
    #print(list(df_all))
    #print(df_all.columns)
    
    df_all=df_all.drop('Unnamed: 0', axis = 1)
    obj = df_all.reindex(index_list)
    obj.to_excel('select_result/{}_index.xlsx'.format(filename[i]))
    