import random
class Node:
   def __init__(self, value, next):
       self.__value=value
       self.__next=next
   def SetValue(self, value):
       self.__value=value
   def SetNext(self, next):
       self.__next=next
   def GetValue(self):
       return self.__value
   def GetNext(self):
       return self.__next
class Queu:
   def __init__(self):
       self.__first=None
       self.__last=None
   def Insert(self, x):
       temp=Node(x, None)
       if(self.__first==None):
           self.__first=temp
       else:
           self.__last.SetNext(temp)
       self.__last=temp
   def Remove(self):
       x=self.__first.GetValue()
       temp=self.__first
       self.__first=self.__first.GetNext()
       temp.SetNext(None)
       return x
   def Head(self):
       return self.__first.GetValue()
   def IsEmpty(self):
       return self.__first==None
class Stack:
   def __init__(self):
       self.__head=None
   def Push(self, x):
       temp=Node(x, None)
       temp.SetNext(self.__head)
       self.__head=temp
   def Pop(self):
       x=self.__head.GetValue()
       temp=self.__head
       self.__head=self.__head.GetNext()
       temp.SetNext(None)
       return x
   def Top(self):
       return self.__head.GetValue()
   def IsEmpty(self):
       return self.__head==None
   


def radixSort(arr):
    Queues=[None]*10
    for i in range(10):
        Queues[i]=Queu()
    maxDig=0
    for num in arr:
        d=0    
        while (num>0):
           num//=10
           d+=1
        if (d>maxDig):
            maxDig=d
    k=1        
    for i in range(maxDig):
        for num in arr:
            n=num//k
            place=n%10
            Queues[place].Insert(num)
        k*=10    
        c=0
        for i in range(10):
            while(not Queues[i].IsEmpty()):
                arr[c]=Queues[i].Remove()
                c+=1
    print(arr)
    return (arr)
                
test=[1,3,2,6,55,77,2,1,0]

radixSort(test)

arr=[None]*1000000
for i in range(1000000):
     arr[i]=random.randint(0,10000)
radixSort(arr)
