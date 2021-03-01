'''
import re

s = '2018/7/None-2018/7/None'
r = re.split("-",s)
print(r)

'''
import os;

def rename():
    i=0
    path="D:\CS_zjw\CS_projects\LINKEDIN_files\zjw_misson\Profile_Format_final\Profile_Format_all\Format_data_all\data_analysis_2"
    filelist=os.listdir(path)#该文件夹下所有的文件（包括文件夹）
    for files in filelist:#遍历所有文件
        Olddir=os.path.join(path,files)#原来的文件路径
        file=os.path.splitext(files)[0]#文件名
        filetype=os.path.splitext(files)[1]#文件扩展名
        Newdir=os.path.join(path,filename[i]+'_classify'+filetype)#新的文件路径
        os.rename(Olddir,Newdir)#重命名
        i=i+1

filename=['0_15735', '15735_31500', '31500_47250', '47250_63000', '63000_79000', 
    '79000_95000', '95000_110750','110750_122500', '122500_138235', '138235_154000',
    '154000_170000', '170000_185735', '185735_','overdata']
'''
for i in range(len(filename)):
    name=filename[i]
    rename()
'''
rename()