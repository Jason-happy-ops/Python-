def sum_array(arr):
    if not arr:         #如果数组为空值即False
        return 0 

    return arr[0]+sum_array(arr[1:])


def sum_list(list):
    if not list:
        return 0

    return list[0]+sum_list(list[1:])

if __name__=="__main__":
    sum1=sum_array([1,2,3,4])
    print(sum1)

    sum2=sum_list([3,4,5,6])
    print(sum2)