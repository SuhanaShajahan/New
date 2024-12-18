def array(arr):
    for i in range(len(arr)):
        count=0
        for j in range(len(arr)):
            if arr[i]==arr[j]:
                count+=1
        if count==1:
            print("The single element is:",arr[i])
arr=[1,3,3,2,1]
array(arr)