def sum_array(arr):
    if not arr:         #如果数组为空值即False
        return 0 

    return arr[0]+sum_array(arr[1:])


def sum_list(list):
    if not list:
        return 0

    return list[0]+sum_list(list[1:])


def way_num(n):
    if n<=2:
        return n 
    else:
        return way_num(n-1)+way_num(n-2)
    
def way_num2(n, memo=None):
    if n in memo:
        return memo[n]
    if n<=2:
        return n
    else:
        memo[n] = way_num2(n-1, memo) + way_num2(n-2, memo)
        print(memo)
        return memo[n]
if __name__ == "__main__":
    a=way_num2(5, {})
    print(a)
