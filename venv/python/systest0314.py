# 1.接收用户输入一个年份，判断是否是闰年(判断闰年的方法是该年能被4整除并且不能被100整除，或者是可以被400整除)
# year=input("请输入一个年份：")
# year = int(year)
# if((year%4==0 and year%100!=0) or year%400==0):
#     print("输入的数是闰年")
# else:
#     print("输入的数不是闰年")
# 2.接收用户输入一组整数，输入负数时结束输入，输出这组数字的和：格式--您输入的数字之和是：xxxx
#
# 3.一个5位数，判断它是不是回文数。如，12321是回文数，个位与万位相同，十位与千位相同
#
# 4.接收用户输入的数字，计算该数字的阶乘
#
# 5.给定一个字符串 target = 'hello huice'，从中找出第一个不重复的字符,输出它是第几位
#
# 6.去除上一题中的重复字符，得到一个新的字符串
#
# 7. 员工工资表，查询结果集如下：((1, 'zhangsan', 3000), (2, 'lisi', 2500), (3, 'tiantian', 20000))
# 	(1)计算员工的平均工资
# 	(2)输出工资最高的员工姓名

# 作业：
# 1.用python实现冒泡排序
# [50,20,30,10]
#
# 升序：谁大谁交换到后面
# 降序：谁大谁交换到前面
#
# 以升序为例
# 第1趟：
# [20,50,30,10]
# [20,30,50,10]
# [20,30,10,50]
# 第2趟：
# [20,30,10,50]
# [20,10,30,50]
# 第3趟：
# [10,20,30,50]
# list=[50,20,30,10]
# for i in  range(1,len(list)):
#     for j in range(1,len(list)-i+1):
#         if list[j-1]>list[j]:
#             list[j-1],list[j]=list[j],list[j-1]
# print(list)

# 3.列表合并(用你能想到所有方法实现)
# [1, 2, 3, 5, 6] [0, 2, 5, 7]
# 要求得到结果：[0, 1, 2, 3, 5, 6, 7]
# list1=[1, 2, 3, 5, 6]
# list2=[0, 2, 5, 7]
# list=list1+list2
# print(list)
# print(sorted(list))

# 5.编写一组数据，记录组内每个人的语文成绩
# 	data = {
# 	     'ZhaoLiYing': 60,
# 	     'FengShaoFeng': 75,
# 	     'TianLaoShi': 99,
# 	     'TangYan': 88,
# 	     'LuoJin': 35,
# 	     'LiuLaoShi': 100
# 	}
# 	a.算出平均分
# 	b.再找出学霸
# data = {
# 	'ZhaoLiYing': 60,
# 	'FengShaoFeng': 75,
# 	'TianLaoShi': 99,
# 	'TangYan': 88,
# 	'LuoJin': 35,
# 	'LiuLaoShi': 100
# 	}
# sum=0
# list0=[]
# for value in data.values():
#     sum=sum+value
#     list0.append(value)
# length=len(list0)
# print(length)
# avg=sum/length
# print(avg)
#
# def fun(x):
#     return x[1]
# data1 = sorted(data.items(),key=fun,reverse=True)
# print(data1)
# print('学霸是%s'%data1[0][0])
#
# data2=sorted(data.keys())
# print(data2)
# data3=sorted(data.values(),reverse=True)
# print(data3)
# data4=sorted(data.items(),key=lambda x:x[1],reverse=True)
# print(data4)
# data5=sorted(data.items(),key=lambda  x:x[0],reverse=True)
# print(data5)

# 6.编写一组数据，记录组内每个人的语文成绩、数学成绩、英语成绩
data = {
    'ZhaoLiYing': [60, 68, 45],
    'FengShaoFeng': [10, 28, 5],
    'TianLaoShi': [44, 86, 73],
    'TangYan': [99, 95, 95],
    'LuoJin': [98, 65, 100],
    'LiuLaoShi': [77, 97, 65]
}
# a.找到平均分不足60分的人
# list1=[]
# list2=[]
# for key,value in data.items():
#     sum=0
#     avg=0
#     for i in value:
#         sum=sum+i
#     avg=sum/len(value)
#     if avg<60:
#         list2.append(key)
# print(list2)
# b.找出各科的最高分 c.算出各科的平均分，再找出各科的学霸

#7.二分查找
def search(list,item):
    low = 0
    high = len(list)-1
    while low<=high:
        mid = int((low + high) / 2)
        if list[mid]<item:
            low=mid+1
        elif list[mid]>item:
            high=mid-1
        else:
            return mid
    return None
list = [1,3,6,7,10,20]
print(search(list,10))
print(search(list,-1))




















