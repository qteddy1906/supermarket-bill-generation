from datetime import datetime
name=input("Enter your name:")

lists='''
         Rice       Rs 20/kg
         Sugar      Rs 30/kg
         Salt       Rs 10/kg
         Oil        Rs 160/L
         Paneer     Rs 100/kg
         Butter     Rs 110/kg
         Maggi      Rs 50/kg
         Horlicks   Rs 100/kg
         Colgate    Rs60/each
         Cheese     Rs210/kg'''

price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

items={'Rice':20, 'Sugar':30,'Salt':10, 'Oil':160,'Paneer':100,'Butter':110,'Maggi':50,'Horlicks':100,'Colgate':60,'Cheese':210}
option=int(input("for list of items press 1:"))

if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if u want to buy press 1 and 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter the quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("Sorry your entered item is not available")
    else:
        print("you entered wrong number")
    inp=input("can i bill the items(yes/no):")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","Rao Supermarket",32*"=")
            print(28*" ","vijayawada")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'quantity',5*" ",'price')
            for i in range(len(pricelist)):
                print(i,8*' ',2*" ",ilist[i],8*' ',qlist[i],10*' ',plist[i])
            print(75*"-")
            print('TotalAmount:',28*" ",'Rs:',totalprice)
            print("Gst Amount:",29*" ",'Rs:',gst)
            print(75*"-")
            print(28*" ",'finalAmount:','Rs:',finalamount)
            print(75*"-")
            print(25*" ","Thanks for visting")
            print(75*"-")