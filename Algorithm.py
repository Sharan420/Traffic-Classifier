#TRIAL 1 very excited
def road(data):
    #val=[['oc',"oc"],['amb','noc']]
    val=data
    R = len(val)
    C = len(val[0])  
    matrix= [] 
    for i in range(R):# A for loop for row entries 
        a =[] 
        for j in range(C):# A for loop for column entries 
             if val[i][j]=='oc': 
                 a.append(1)
             elif val[i][j]=="noc":
                 a.append(0)
             else :
                 a.append(2)
        matrix.append(a) 
    for i in range(R): 
        for j in range(C): 
            print(matrix[i][j], end = " ") 
        print()
    return matrix
def nt(dit,j):#dit is a dict of syntax{road name as r :[num of car,area covered]}
    import math as m
    global n
    global p
    global ma
    ma=0
    p=0
    e=0
    a=dit
    for i in a:
        if i[0:2]=="r"+str(j+1):
            ma=a[i][0]/a[i][1]
        else:
            p+=a[i][0]/a[i][1]
            e+=1
    p/=e
    p*=10
    ma*=10
    p=(m.log((100-p**2),10))*(m.atan(p**(2*(p**p))))
    ma=(m.log((100-ma**2),10))*(m.atan(ma**(2*(ma**ma))))
    if p<=ma:
        print("run green light code till achieves maxima for road "+str(j+1))
        n=1#case 1
    else:
        print("run green light untill p=m for road"+str(j+1))
        n=2#case 2
    print(p,ma,n)
    
def fd(m):
    q=m
    for i in q:
        for j in i:
            if j==2:
                return "green corridoor"
            else:
                pass
    return "normal code"
def gc(i):
    print("green for road"+str(i+1)+"default red rest")
def odr(queue):#maintaining the cycle for q
    q=queue
    b=q.index(1)
    a=q.pop(b)
    if b==len(q):
        q.insert(0,a)
    else:
        q.insert(b+1,a)
    return q
def devq():#devloping q
    q=open("tria1_1_data.text","a+")
    m=data#given by yollo
    m=write(m)
    m=len(m)
    a=[]
    for i in range(m):
        if i==0:
            a.append(1)
        else:
            a.append(0)
    return a
a=1 # detrmines the wrking
m=0
n=0
ma=0
p=0
queue=devq()
# logic ()_>
while a:# round robin for identification
    q=open("tria1_1_data.text","r")
    rawdata=eval(q.read())#data=[[data road 1],[data road 2]]
    q.close()
    for data in rawdata:
        b=road(data)
        i=rawdata.index(data)#index of the road
        if fd(b)=="green corridoor":
            gc(i)
            m+=1
            break
        elif fd(b)=="normal code":
            if m>0:
                print("red for road"+str(i+1))
                m=0
            else:
                pass
#then continue with a queue
    if m>0:
        break
    else:
        f=open("trial_1_dit.text","r")
        dit=eval(f.read())
        f.close()
        i=queue.index(1)
        if n==1:
            if ma==3.109:
                print("red for road"+str(i+1))
                queue=odr(queue)
            else:
                pass
        if n==2:
            if ma==p:
                print("red for road"+str(i+1))
                queue=odr(queue)
            else:
                pass
        if n==1 or n==2 or n==0:
            print("comparsion code for road"+str(i+1))
            nt(dit,j=i)
            break
        else:
            pass
                
            
            
           
    
    
    
