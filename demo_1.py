import csv
# 房型、入住时间、入住类型、评分、评论、评论时间
header = ['房型','入住时间','入住类型','评分','评论','评论时间']

data = ['1','2','3','4','5','6']
data1 = ['1','2','3','4','5','6']
with open('comment_data/demo.csv','w',encoding='utf-8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
    writer.writerow(data1)

