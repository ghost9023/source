# import pandas as pd
# emp = pd.DataFrame.from_csv("d:/data/ttt_data2.csv")
# result = emp[['ename', 'sal']][emp['sal'] >= 3000].sort_values('sal',ascending=True)
# print(result)

# import pandas as pd
# ttt = pd.DataFrame.from_csv("d:/data/ttt_data2.csv")
# result=ttt['learning_order']ttt[['c1','c3','c7','c9']==1 and ['c2','c4','c9']==2 and ['c5']+['c6']+['c8']==1].max()
# print(result)
#

import pandas as pd
t_dt = pd.DataFrame.from_csv("d:\data\mit_t.csv")
result1 = t_dt[(t_dt['PLAYER'] == 1) &
               (t_dt['C1'] == 1) &
               (t_dt['C2'] == 2) &
               (t_dt['C3'] == 1) &
               (t_dt['C4'] == 2) &
               (t_dt['C7'] == 1) &
               (t_dt['C9'] == 2) &
               (t_dt['C5'] + t_dt['C6'] + t_dt['C8'] == 1)]
result2 = result1.groupby(['C5', 'C6', 'C8'])['LEARNING_ORDER'].max()
print(result2)



