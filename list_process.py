if __name__ == "__main__":
    list1 = [2, 3, 5, 6, 8]
    
    print [3*x for x in list1]
    print [x / 3.0 for x in list1 if x > 3]
    
    v1 = (1, 2, 3)
    v2 = ('a', 'z')
    print [(a, b) for a in v1 for b in v2 if (a % 2) == 0]