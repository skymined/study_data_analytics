# BMI = 체중(kg) / 신장(m)^2

import pandas as pd

data = pd.read_csv("C:\Develops\study_data_analytics\docs\quests\DDA\datas\SpineSurgeryList.csv")

spine_data = pd.DataFrame(data)
pass


# BMI 적용하기
def cal_bmi (df) :
    weight = df['체중']
    height = df['신장']
    bmi = weight / (height*0.01)**2
    return bmi

spine_data['BMI'] = spine_data[['체중', '신장']].apply(cal_bmi, axis=1)
spine_data[['체중', '신장', 'BMI']]

#
#         체중   신장        BMI
# 0     60.3  163  22.695623
# 1     71.7  171  24.520365
# 2     77.1  178  24.334049
# 3     74.2  174  24.507861
# 4     80.7  183  24.097465
# ...    ...  ...        ...
# 1889  64.0  157  25.964542
# 1890  59.0  157  23.936062
# 1891  70.0  167  25.099502
# 1892  77.0  177  24.577867
# 1893  49.0  168  17.361111

# [1894 rows x 3 columns]

# 수술시간 -> 시분 표시하고 컬럼 생성하기
def cal_time(x):
    try : 
        hour = int(x//60)
        min = int(x%60)
        if hour == 0:
            surgery_time = f"{min}분"
        else :
            surgery_time = f"{hour}시간 {min}분"
    except :
        surgery_time = 'None'
    return surgery_time

spine_data['수술시간_시분'] = spine_data['수술시간'].apply(cal_time)
pass

#       수술시간  수술시간_시분
# 0     68.0   1시간 8분
# 1     31.0      31분
# 2     78.0  1시간 18분
# 3     73.0  1시간 13분
# 4     29.0      29분
# ...    ...      ...
# 1889  80.0  1시간 20분
# 1890  20.0      20분
# 1891  50.0      50분
# 1892  25.0      25분
# 1893  45.0      45분
