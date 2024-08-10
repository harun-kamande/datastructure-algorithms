def search(list,target):
    
    for i in list:
        if i==target:
            print("Target found ")
            break
        else:
            print(f"{target} was never found in the list")
            break
    
list=[1,2,3,4,5,6,7,8,9,10]

search(list=list,target=1)