import copy
import xlrd
wb = xlrd.open_workbook(filename=r"E:\python1\day7\每月销售情况.xlsx",encoding_override=True)

clothes = ['羽绒服','牛仔裤','风衣','皮草','T恤','马甲','小西装','皮衣','衬衫','休闲裤','卫衣','棉衣','铅笔裤']
price = []
c = []
nums = []
for i in range(len(clothes)):
    nums.append(0)
    price.append(0)

total_sum = 0
for i in range(0,12):
    y = i
    st = wb.sheets()[i]
    rows = st.nrows
    cols = st.ncols
    sum = 0
    csum = 0

    for a in range(1,rows):
        data = st.row_values(a)
        sum = sum+data[2]*data[4]

        cloth_sum = data[4]*csum
        for i in range(len(clothes)):
            if data[1] == clothes[i]:
                nums[i] = nums[i] + data[4]
                price[i] = price[i]+data[2]*data[4]
    c.append(copy.deepcopy(nums))


    total_sum = sum + total_sum
    total_csum = total_csum + cloth_sum
    print(y+1,"月")
    for i in range(len(clothes)):
        f = nums[i] / total_csum
        p = price[i] / sum
        print(clothes[i],"数量占比：{:.2%}".format(f))

for i in range(len(clothes)):
    f = nums[i] / total_csum
    p = price[i] / total_sum
    print(clothes[i],"的总数量占比为:{:.2%,总销售额占比:{:.2%}}".format(f,p))
d = clothes[nums.index(max(nums))]
g = clothes[nums.index(min(nums))]
print("全年销售总额:",round(total_sum,1),"最畅销的衣服是:",d,"销售数量最低的是:",g)

q=[]
quarter1 = list(map(lambda x, y: x - y, c[3], c[0]))#第一季度
q1=clothes[quarter1.index(max(quarter1))]
q.append(q1)
quarter2 = list(map(lambda x, y: x - y, c[6], c[3]))
q2=clothes[quarter2.index(max(quarter2))]
q.append(q2)
quarter3 = list(map(lambda x, y: x - y, c[9], c[6]))
q3=clothes[quarter3.index(max(quarter3))]
q.append(q3)
quarter4 = list(map(lambda x, y, z: x - y + z, c[11], c[9],c[0]))
q4=clothes[quarter4.index(max(quarter4))]
q.append(q4)
for i in range(1,5):
    print(i, "季度最畅销的是：", q[i - 1])