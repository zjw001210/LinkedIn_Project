import pandas as pd

def Result(): 
    global return_data
    global index
    DF=pd.DataFrame([],columns=pd_list)
    for index in range(len(return_txt)):
        return_data=eval(return_txt[index])
        Company_origin()
        Experience()
        DF=DF.append(frame_each,ignore_index=True)
        #Viewed()
    #df_viewed=pd.DataFrame({'viewed_name':viewed_name,'viewed_link':viewed_link,'viewed_summary':viewed_summary,'viewed_location':viewed_location})
    df_origin=pd.DataFrame({'full_name':full_name,'boolean_result':boolean_result,'experience':experience})
    Result_frame=pd.concat([df_origin,DF],axis=1)
    Result_frame.to_excel('{}_all.xlsx'.format(filename[u][:-4]))
    #df_viewed.to_excel('Viewed{}.xlsx'.format(filename[u][:-4]))

def Viewed():
    profile_view=return_data['people_also_viewed']
    for i in range(len(profile_view)):
        view=profile_view[i]
        viewed_link.append(view['link'])
        viewed_name.append(view['name'])
        viewed_summary.append(view['summary'])
        viewed_location.append(view['location'])
   
#判断这个人的公司是否是我们需要的
def Company_origin():
    global profile_exp
    global cpy_obj
    #get: return_data
    ##get_column: full_name
    full_name.append(return_data['full_name'])
    ##get_column: url_result
    #url_name=return_data['public_identifier']
    #if url_name==None:
    #    url_name='None'
    #url_all='https://www.linkedin.com/in/'+url_name
    #url_result.append(url_all)
    ##get_column: experience
    profile_exp=return_data['experiences']
    if profile_exp==[]:
        profile_exp=[{'starts_at': None, 'ends_at': None, 'company': None, 'company_linkedin_profile_url': None, 
        'title': None, 'company_urn': None,'description': None, 'location': None, 'employment_type': None, 'media': []}]
    experience.append(profile_exp)
    ##get_column: boolean_result
    cpy_obj=[] #创建访问对象object公司名称列表cpy_obj,通过循环将这个人所有的公司放在cpy_obj
    for i in range(len(profile_exp)):
        exp=profile_exp[i]
        cpy_obj.append(exp['company'])
    boolean_result.append('False') # 布尔判断
    for j in range(len(cpy_org)):
        for t in range(len(cpy_obj)):
            if cpy_obj[t]==None:
                continue
            elif cpy_org[j] in cpy_obj[t]:
                boolean_result[index]='True'

def Generate(title,num):
    global tit_name
    tit_name=title + '_' + str(num)

def Experience():
    global frame_each
    exp_len=len(profile_exp)
    #print('exp_len: ',exp_len)
    dic={}
    for i in range(len(titleName)):
        for num in range(1,exp_len +1): 
            ls=[]   
            title=titleName[i]
            Generate(title,num)
            if title=='company':
                cpy = profile_exp[num-1]['company']
                ls.append(cpy)
                dic[tit_name]=ls
            elif title=='job':
                job = profile_exp[num-1]['title']
                ls.append(job)
                dic[tit_name]=ls
            elif title=='duration':
                start=str(profile_exp[num-1]['starts_at'])
                end=str(profile_exp[num-1]['ends_at'])
                #print(type(start),start)
                dur='None-None'
                if start=='None':
                    if end=='None':
                        dur=start +'-'+ end
                    elif end != 'None':
                        end=eval(end)
                        ymd_end=str(end['year'])+'/'+ str(end['month'])+'/'+ str(end['day'])
                        dur=start +'-'+ ymd_end
                elif start != 'None':
                    start=eval(start)
                    ymd_start=str(start['year'])+'/'+ str(start['month'])+'/'+ str(start['day'])
                    if end=='None':
                        dur=ymd_start +'-'+ end
                    elif end != 'None':
                        end=eval(end)
                        ymd_end=str(end['year'])+'/'+ str(end['month'])+'/'+ str(end['day'])
                        dur=ymd_start +'-'+ ymd_end
                ls.append(dur)
                dic[tit_name]=ls
            elif title=='description':
                des = profile_exp[num-1]['description']
                ls.append(des)
                dic[tit_name]=ls 
            #print(num)
    frame_each=pd.DataFrame(dic)

###函数之外
###view
viewed_link=[]
viewed_name=[]
viewed_summary=[]
viewed_location=[]

titleName=['company','job','duration','description']
pd_list=[]
for j in range(len(titleName)):
    for p in range(1,13): 
        tt=titleName[j]+'_'+str(p)
        pd_list.append(tt)

#创建原始origin公司名称列表cpy_org,读取company_name.txt文件
cpy_org = []
with open(r'company_name_plus.txt', 'r',encoding='utf-8') as f:
    for j in f.readlines():
        cpy_org.append((j.strip("\n")))

#读取返回内容return.txt文件

filename=[ '0_15735data.txt','15735_31500data.txt','31500_47250data.txt',
'47250_63000data.txt','63000_79000data.txt''79000_95000data.txt',
'95000_110750data.txt','110750_122500data.txt','122500_138235data.txt',
'138235_154000data.txt',    '154000_170000data.txt','170000_185735data.txt',
'185735_data.txt']

for u in range(len(filename)):
    file='all_Data\\' + filename[u]
    try:
        f2 = open(file, 'r',encoding='gbk')
        return_txt = f2.readlines()
    except:
        f2 = open(file, 'r',encoding='utf-8')
        return_txt = f2.readlines()
    f2.close()
    print(filename[u][:-4])
    ###experience
    full_name=[]
    # url_result=[]
    boolean_result=[]
    experience=[]
    Result()

'''
for index in range(len(return_txt[1:12])):
    print('index: ',index)
    return_data=eval(return_txt[index])
    profile_exp=return_data['experiences']
    print(profile_exp==[])
'''

