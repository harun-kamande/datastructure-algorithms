
def binarysearch(list,target):
    
    start=0
    end=len(list)-1

    while start<= end:
        midpoint=(start+end)//2

        if list[midpoint]==target:
            print(f"Target was found {target}")
            return

        elif list[midpoint]>target:
            end=list[midpoint]-1


        elif list[midpoint] <target:
            start=list[midpoint]+1       

        else:
            print(f"{target} was never found")
            break
            
        
        
binarysearch(list=list,target=1)