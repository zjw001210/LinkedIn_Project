import pandas as pd


filename=['0_15735', '15735_31500', '31500_47250', '47250_63000', '63000_79000', 
    '79000_95000', '95000_110750','110750_122500', '122500_138235', '138235_154000',
    '154000_170000', '170000_185735', '185735_','overdata']
    
for s in range(len(filename)):
    print('s=',filename[s])
    filepath_index='data_analysis_result_demo/{}_da.xlsx'.format(filename[s])
    filepath_all='jobhopping_result/{}_jh_gap_all.xlsx'.format(filename[s])
    index_file=pd.read_excel(filepath_index)
    index_lst=index_file['Unnamed: 0']
    #print(index_lst)

    df_all=pd.read_excel(filepath_all)
    #print(list(df_all))
    #print(df_all.columns)
    
    #df_all=df_all.drop('Unnamed: 0', axis = 1)
    obj = df_all.reindex(index_lst)
    obj.to_excel('data_analysis_all/{}_da_all.xlsx'.format(filename[s]))
    