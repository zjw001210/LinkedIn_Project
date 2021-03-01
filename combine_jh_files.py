import pandas as pd

filename=['0_15735', '15735_31500', '31500_47250', '47250_63000', '63000_79000', 
    '79000_95000','95000_110750', '110750_122500', '122500_138235', '138235_154000',
    '154000_170000', '170000_185735', '185735_','overdata']

title=['index','gap','jhlast_time','jhnext_time','id','name','last_company','next_company',
        'last_job','next_job','last_dsp','next_dsp','boolean_result']

for s in range(len(filename)):
    DF=pd.DataFrame([],columns=title)
    for gap in range(24): #
        print('s=',s,'gap=',gap)
        filepath_jobhopping='jobhopping_result/{}/{}_jh_gap{}.xlsx'.format(filename[s],filename[s],gap)
        df=pd.read_excel(filepath_jobhopping)
        DF=DF.append(df,ignore_index=True)
    df=DF
    df.drop(['index'], axis=1,inplace=True)
    id = df.pop('id')      #pop出一个Series
    df.insert(0,'id',id)    #把id这一列插入到index=0的列
    df.to_excel('jobhopping_result/{}_jh_gap_all.xlsx'.format(filename[s]))
