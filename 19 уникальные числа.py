mas=[]
cnt=0
cnt2=0
cnt3=0
cup=0

print("введи 10 чисел")
while cnt<10:
                 cup=int(input(""))
                 mas.append(cup)
                 cnt=cnt+1
                
cnt2=0
prd=9

while cnt2<=prd:
         cnt=0
         while cnt<prd: 
                if mas[cnt]==mas[cnt2] and cnt!=cnt2:
                    
                                  print("-",cnt2)
                                  print("-",cnt)
                                  
                                  del(mas[cnt])
                                  del(mas[cnt2])
                                  
                                  prd-=2
                                  cnt2=-1
                                  print("=",cnt2)
                                  print("=",cnt)
                                  
                                  print(mas)
                                  break
                cnt+=1
         cnt2+=1


         
print(mas)
