import datetime
ch=0
while ch!=-1:
    print("These are choices:-")
    print("Enter 1 for monitoring daily resturant food leftover")
    print ("Enter 2 for supermarket expiration products")
    print("Enter 3 for Tax reduction")
    print("Enter 4 for Food Recycling ")
    print("Enter 5 for Volunteering")
    print("Enter -1 to exit")
    ch=int(input("Enter choice= "))
    d={1:['deco'],2:['animal_shelter'],3:['ngo','discount']}
    if ch==1:
        #monitoring 0
        left=False
        restu=int(input("Enter no.="))
        if restu==0:
            chkhpnt=1
            left=True 
            if chkhpnt==1:
                if left==True:
                    qul=int(input("enter quality(1/2/3): "))
                    for i in d:
                        if qul==i:
                           h=d[i]
                           print(h)
    if ch==2:
        #supermarkets expiration products
        a=input("Enter the commodity")
        n=int(input("Enter the commodities to calculate"))
        d2={"Expired":"deco","Equal":"animal_shel"}
        d3={}
        exp=0
        c=0
        k=int(input("Enter expiry date"))
        f=int(input("Enter the expiry month"))
        date1=datetime.datetime(2023,3,k)
        for i in (0,n):
            e=int(input("Enter the day"))
            b=int(input("Enter the month"))
            date2=datetime.datetime(2023,b,e)
            if date1<date2==True:
                exp=1
            elif date1!=date2==False:
                exp=2
            if exp==1:
                d3[i]=["Expired"]
            elif exp==2:
                d3[i]=["Equal"]
            else:
                d3[i]=["No change"]
        for j in d3:
            for k in d2:
                if d3[j]==k:
                    d3[j].append(k)
                    print(a)
                    print(d3)
    if ch==3:
         #Tax reduction
         a=[]
         f=int(input("Enter no. of inputs="))
         for i in range(0,f):
             print("Enter choice:")
             print("ch1=ngo")
             print("ch2=discount")
             print("ch3=deco")
             print("ch4=animal_shel")
             g=input("Enter Distributions=")
             a.append(g)
         for j in d:
             if a==d[j]:
                 star=j
             if star>=3:
                 tax=tax-10*tax/100
             elif star==2: 
                 tax=tax-20*tax/100
             elif star==1:
                 tax=tax-30*tax/100
    if ch==4:
         #Food Recycling
         bacteria=0
         d4={1:["Fertilisers"],2:["animal_shel"],3:["deco"]}
         h=int(input("Enter bacterial growth(1/2/3)"))
         if bacteria==1:
             qual=10
             l=1
         elif bacteria==2:
             qual=30
             l=2
         elif bacteria==3:
             qual=40
             l=3
         m=int(input("Enter the bacteria"))
         for i in d4:
             if i==l:
                print("Use is",d4[l])
    if ch==5:
         #Volunteering 
         a=False
         lst=[]
         r=""
         q=""
         print("The NGOs are situated in a linear order of address")
         ngo=["Dholabhata","Pratama","Satida","Fahatinah","Ghuru"]
         ng={"Dholabhata":20,"Pratama":30,"Satida":10,"Fahatinah":40,"Ghuru":50}
         o=int(input("Enter helpline no."))
         print("helpline no.",o)
         k=input("Enter the location")
         quan=int(input("Enter leftover"))
         lst=len(ngo)
         i=0
         j=0
         s=""
         for i in range(0,ln):
             if ngo[i]==k:
                 r=ngo[i+1]
                 q=ngo[i+2]
             if ng[r]<ng[q]==True:
                 s=r
             else:
                 s=q
         print("Ngo is",s)
