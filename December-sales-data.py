'''
12月衣服销售数据
1.计算12月销售总金额
2.计算每种衣服的销售占比（件数）
3.每种衣服的销售额占比
'''

print("---日期---服装名城---价格/件---库存数量---销售量/日---")
print("---1号----羽绒服-----253.6----500-------10-------")  # 253.6 * 10
print("---2号----牛仔裤-----86.3-----600-------60-------")  # 86.3 * 60
print("---3号----风衣-------96.8-----335-------43-------")  # 96.8 * 43
print("---4号----皮草-------135.9----855-------63-------")  # 135.9 * 63
print("---5号----T恤--------65.8-----632-------63-------")  # 65.8 * 63
print("---6号----衬衫-------49.3-----562-------120-------")  # 49.3 * 120
print("---7号----牛仔裤------86.3----600--------72-------")  # .3 * 72
print("---8号----羽绒服------253.6---500--------69-------")  # 253.6 * 69
print("---9号----牛仔裤------86.3----600--------35-------")  # 86.3 * 35
print("---10号---羽绒服------253.6---500--------140-------")  # 253.6 * 140
print("---11号---牛仔裤------86.3----600--------90-------")  # 86.6 * 90
print("---12号---皮草-------135.9----855--------24-------")  # 135.9 * 24
print("---13号---T血--------65.8-----632--------45-------")  # 65.8 * 45
print("---14号---风衣--------96.8----335--------25-------")  # 96.8 * 25
print("---15号---牛仔裤------86.3-----600--------60-------")  # 86.3 * 60
print("---16号---T血--------65.8-----632--------129-------")  # 65.8 * 129
print("---17号---羽绒服------253.6----500--------10-------")  # 253.6 * 10
print("---18号---风衣--------96.8-----335--------43-------")  # 96.8 * 43
print("---19号---T血---------65.8-----632--------63-------")  # 65.8 * 63
print("---20号---牛仔裤-------86.3-----600--------60-------")  # 86.3 * 60
print("---21号---皮草--------135.9-----855--------63-------")  # 135.9 * 63
print("---22号---风衣---------96.8-----335--------60-------")  # 96.8 * 60
print("---23号---T血----------65.8-----632--------58-------")  # 65.8 * 58
print("---24号---牛仔裤--------86.3-----600-------140-------")  # 86.3 * 140
print("---25号---T血----------65.8-----632--------48-------")  # 65.8 * 48
print("---26号---风衣----------96.8-----335--------43-------")  # 96.8 * 43
print("---27号---皮草---------135.9-----855--------57-------")  # 135.9 * 57
print("---28号---羽绒服--------253.6----500--------10-------")  # 253.6 * 10
print("---29号---T血-----------65.8----632--------63-------")  # 65.8 * 63
print("---30号---风衣----------96.8-----335-------78-------")  # 96.8 * 78
print("----------------------------------------------------")
print("----------------------------------------------------")
print("----------------------------------------------------")
print("12月总金额￥",(253.6 * 10 + 86.3 * 60 + 96.8 * 43 + 135.9 * 63 + 65.8 * 63 + 49.3 * 120 + 86.3 * 72 + 253.6 * 69 +
                 86.3 * 35 + 253.6 * 140 + 86.6 * 90 + 135.9 * 24 + 65.8 * 45 + 96.8 * 25 + 86.3 * 60 + 65.8 * 129 +
                 253.6 * 10 + 96.8 * 43 + 65.8 * 63 + 86.3 * 60 + 135.9 * 63 + 96.8 * 60 + 65.8 * 58 + 86.3 * 140 +
                 65.8 * 48 + 96.8 * 43 + 135.9 * 57 + 253.6 * 10 + 65.8 * 63 + 96.8 * 78))
print("----------------------------------------------------")
print("----------------------------------------------------")
print("----------------------------------------------------")
print("12月总销售件数：",(10 + 60 + 43 + 63 + 63 +
                       120 + 72 + 69 + 35 + 140 +
                       90 + 24 + 45 + 25 + 60 +
                       129 + 10 + 43 + 63 + 60 +
                       63 + 60 + 58 + 140 + 48 +
                       43 + 57 + 10 + 63 + 78))
print("                                       ")
print('羽绒服销售件数占比: {:.2f}%'.format((10 + 69 + 140 + 10 + 10)/1844*100))
print('牛仔裤销售件数占比: {:.2f}%'.format((60 + 72 + 35 + 90 + 60 + 60 + 140)/1844*100))
print('风衣销售件数占比: {:.2f}%'.format(int((43 + 25 + 43 + 60 + 43 + 78)/1844*100)))
print('皮草销售件数占比: {:.2f}%'.format(int((63 + 24 + 63 + 57)/1844*100)))
print('T恤销售件数占比: {:.2f}%'.format(int((63 + 45 + 129 + 63 + 58 + 48 + 63)/1844*100)))
print('衬衫销售件数占比: {:.2f}%'.format(int(120)/1844*100))

print("----------------------------------------------------")
print("----------------------------------------------------")
print("----------------------------------------------------")
print('羽绒服销售额占比: {:.2f}%'.format(int(10 + 69 + 140 + 10 + 10) * 253.6/198427*100))
print('牛仔裤销售额占比: {:.2f}%'.format(int(60 + 72 + 35 + 90 + 60 + 60 + 140) * 86.3/198427*100))
print('风衣销售额占比: {:.2f}%'.format(int(43 + 25 + 43 + 60 + 43 + 78) * 96.8/198427*100))
print('皮草销售额占比: {:.2f}%'.format(int(43 + 25 + 43 + 60 + 43 + 78) * 135.9/198427*100))
print('T恤销售额占比: {:.2f}%'.format(int(63 + 45 + 129 + 63 + 58 + 48 + 63) * 65.8/198427*100))
print('衬衫销售额占比: {:.2f}%'.format(int(120) * 49.3/198427*100))
