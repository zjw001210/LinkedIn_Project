import pandas as pd

filename=['0_15735', '15735_31500', '31500_47250', '47250_63000', '63000_79000', 
    '79000_95000','95000_110750', '110750_122500', '122500_138235', '138235_154000',
    '154000_170000', '170000_185735', '185735_','overdata']

title=['id','生产/成本','稳定','舒适','驾驶','安全','未知技术','非技术','支持','未知',
        '存疑','name','job','description']

DF=pd.DataFrame([],columns=title)
for s in range(len(filename)):
    print('s=',filename[s])
    filepath_classify='data_analysis_classify/{}_classify.xlsx'.format(filename[s])
    df=pd.read_excel(filepath_classify)
    DF=DF.append(df,ignore_index=True)    

DF.to_excel('data_analysis_classify/data_classify_combined.xlsx')
