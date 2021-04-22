def coding(tx,stp): # tx-сама строка которую шифруем(поток)  stp-шаг скоторым меняем символ
            sumv='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
            cnt=0
            stp2=0
            tx2=''
            while cnt<len(tx):
                          try:
                            stp2=sumv.index(tx[cnt])+stp
                            if stp2>=len(sumv):  # если новый индекс больше чем sumv то мы вычитаем cumv чтобы корректно символ поменять
                                          stp2=stp2-33
                            tx2=tx2+sumv[stp2]
                          except:
                              tx2=tx2+tx[cnt]
                          cnt+=1
            return(tx2)

potok=""" """
pr=open('исходный текст.txt',encoding='utf-8')
potok=pr.read()
st=int(input('а дай ка мне шаг: '))
potok=coding(potok,st)
pr=open('зашифрованный текст.txt','w')
pr.write(potok)
