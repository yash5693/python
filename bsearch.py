def bsearch(l,low,high,item):
    flag=0
    if (high>=low):
        mid=(high+low)//2
        if l[mid]==item:
            print("search successfull")
        elif l[mid]>item:
            bsearch(l,low,mid-1,item)
        else:
            bsearch(l,mid+1,high,item)
    else:
        print("Search unsuccessfull")

l=[10,20,30,40,50,60,70,80,90,100]
item=int(input("Enteran item to search"))
t=bsearch(l,0,len(l)-1,item)