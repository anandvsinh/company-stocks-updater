import csv
f=open("mtv_stock.csv","a",newline="")

w=csv.writer(f)
rec=[]
while True:
    s=int(input("Enter S.No.: "))
    n=input("Enter name of the item: ")
    q=int(input("Enter stock available: "))
    p=float(input("Enter Price of the item: "))

    ch=input("Want to add more items ? (y/n)")
    if ch=='n':
        print("Thank you for using our program !")
        break
    lst=[s,n,q,p]
    rec.append(lst)

for i in rec:
    w.writerow(i)
f.close()