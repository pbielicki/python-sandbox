def array():
    "array test"
    arr = [1, 2, 3, 4]
    print arr[-1]
    print arr[-3]
    
    "slicing"
    print arr[2:4]
    print arr[:3]
    print arr[1:]
    
    "last two elements"
    print arr[-2:]
    
    "no exception here"
    print arr[2:10]
    
    "step / increment"
    print arr[::2]
    "reversing array"
    print arr[::-1]
    
array()