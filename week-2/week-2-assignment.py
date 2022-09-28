#要求一: 函式與流程控制
def calculate(min, max, step):
    minnum=min
    maxnum=max
    stepnum=step
    sum=0
    if minnum>0:
        for i in range(minnum, maxnum+stepnum, stepnum):
            sum+=i
        print(sum)
    else:
        for i in range(minnum, maxnum, stepnum):
            sum+=i
        print(sum)

calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0


#要求二: Python 字典與列表
def avg(data):
    sum = 0
    p = 0
    mydata = data["employees"]
    for i in range(len(mydata)):
        if mydata[i]["manager"]==False:
            sum+=mydata[i]["salary"]
            p+=1
    print(sum/p)
avg({
        "employees":[   #this a list
            {
                "name":"John",
                "salary":30000,
                "manager":False
            },
            {
                "name":"Bob",
                "salary":60000,
                "manager":True
            },
            {
                "name":"Jenny",
                "salary":50000,
                "manager":False
            },
            {
                "name":"Tony",
                "salary":40000,
                "manager":False
            }
        ]
}) # 呼叫 avg 函式

#要求三：完成以下函式，最後能印出程式中註解所描述的結果。
def func(a):
    #a=a
    def mul(b,c):
        result=(b*c)+a
        print(result)
    return mul
func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果


#要求四：
def maxProduct(nums):
    list=nums
    product=[]
    newlist2=[]
    length=len(list)
    if length==4:
        iii=list[1:length]
        newlist=iii
        jjj=list[0]
        newlist2.append(jjj)
        for i in newlist:
            for j in newlist2:
                num=i*j
            product.append(num)
        
        iii=list[2:length]
        newlist=iii
        jjj=list[1]
        newlist2.append(jjj)
        for i in newlist:
            for j in newlist2:
                num=i*j
            product.append(num)

        iii=list[3:length]
        newlist=iii
        jjj=list[2]
        newlist2.append(jjj)
        for i in newlist:
            for j in newlist2:
                num=i*j
            product.append(num)

        result=max(product)
        print(result)
    elif length==3:
        iii=list[1:length]
        newlist=iii
        jjj=list[0]
        newlist2.append(jjj)
        for i in newlist:
            for j in newlist2:
                num=i*j
            product.append(num)
        
        iii=list[2:length]
        newlist=iii
        jjj=list[1]
        newlist2.append(jjj)
        for i in newlist:
            for j in newlist2:
                num=i*j
            product.append(num)
        result=max(product)
        print(result)
    else:
        iii=list[1:length]
        newlist=iii
        jjj=list[0]
        newlist2.append(jjj)
        for i in newlist:
            for j in newlist2:
                num=i*j
            product.append(num)
        result=max(product)
        print(result)
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10


#要求五：
def twoSum(nums, target):
    list=nums
    t=target
    r=[]
    length=len(list) #---4
    n=0
    m=1
    for m in range(length):
        iii=list[n]
        jjj=list[m]
        if iii + jjj != t: 
            #沒有配對
            continue
        else: 
            r.append(list.index(iii))
            r.append(list.index(jjj))
            return r
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

