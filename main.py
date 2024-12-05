def SquaredValues(beg,end):
    lst = []
    for i in range(beg,end+1):
        lst.append(i**2)
        lst_even = []
        lst_odd = []
        for i in lst:
         if i%2==0:
          lst_even.append(i)   
        else:
         lst_odd.append(i)    
    
    print("HERE IS A LIST OF EVEN SQUARES WITHIN A SPECIFIED RANGE",lst_even)
    print("HERE IS A LIST OF ODD SQUARES WITHIN A SPECIFIED RANGE",lst_odd)
     
beg=int(input("ENTER STARTING RANGE :"))
end=int(input("ENTER END RANGE :"))
SquaredValues(beg,end)