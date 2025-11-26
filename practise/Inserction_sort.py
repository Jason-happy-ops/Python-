import array


def Inserction_sort(arr):
    for i in range(1,len(arr)):
        scan_number=arr[i]      #用循环扫描元组中的每一个元素
        j=i-1       #代表已排序区间的最后一个数，将正在被扫描的元素依次向前比较
        
        while j>=0 and arr[j]>scan_number:
            arr[j+1]=arr[j]
            arr[j]=scan_number
            j-=1


    return arr
    


a=Inserction_sort([23,13,2,56,28])
print(a)


