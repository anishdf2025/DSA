arr1= [1, 5, 9, 10, 15, 20]
arr2 =  [2, 3, 8, 13]

def sort(a,b):
    i=len(arr1)-1
    j=0
    
    while i>=0 and j<len(arr2):
        if arr1[i]>arr2[j]:
            arr1[i],arr2[j]=arr2[j],arr1[i]
            i-=1
            j+=1
        else:
            break
    arr1.sort()
    arr2.sort()
    return arr1,arr2
c,d=sort(arr1,arr2)
print(c,d)
            
            