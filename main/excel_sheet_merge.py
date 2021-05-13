import pandas as pd

# data = pd.read_excel("20190815113700024.xls",None)
#
# sheet_list = list(data.keys())
# new_data = pd.ExcelWriter("new_20190815113700024.xls")
# start_row = 0
# for sheet_name in sheet_list:
#     sheet = data.get(sheet_name)
#     shape = sheet.shape
#     print(shape)
#     sheet.to_excel(new_data,startrow=start_row)
#     start_row += (shape[0] + 2)
# new_data.save()
# print(sheet_list)
#
from pandas import DataFrame

# a = [{"id":"1","s":"b"}]
a = [{"English":"b","math":89,'chinese':99},{"English":"a",'math':90,'chinese':98},{"English":"a","math":89,'chinese':99}]
b = DataFrame(a)
print(b)
# print(list(b.columns))
#   English  chinese  math  a   b
# 0       b       99    89  none 1
# 1       a       98    90  1   none
# 2       a       99    89  1   none
c = b.pivot(columns='English',values=['math'])

print(c)
def main(db,col):
    print("--------------")
    columns = list(db.columns)
    new_db = db.reset_index()
    if col in columns:
        one_col = list(set(db[col]))
        for line in one_col:
            tem = DataFrame([{col:line,line:1}])
            new_db = new_db.merge(tem,how='left',on=[col])
        print(new_db)
    else:
        print("错误")

# main(b,"English")



