cup=0
cnt=0
cnt2=0
cupmas=[]
mas=[]
name=""
clovo=""

name=input(" давай фамилию ")
cup=int(input(" давай очки "))
mas.append([name,cup])
clovo=input("будут еще спортсмены? ")

cnt+=1

while clovo!="нет":
    
                name=input(" давай фамилию ")
                cup=int(input(" давай очки "))
                mas.append([name,cup])
                clovo=input("будут еще спортсмены? ")
                
                cnt+=1
print(mas)

cup=int(input("тогда давай число очков, я скажу кто набрал столько или больше "))

cnt2=0
while cnt2<+cnt:
            if mas[cnt2][1]>=cup:
                                print(mas[cnt2])
            cnt2+=1
