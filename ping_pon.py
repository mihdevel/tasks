def service(score):
    
    nbrs = score.split(':')
    sum = int(nbrs[0]) + int(nbrs[1])
    print (sum % 5)
    res = "first"
    for i in range(sum + 1):
        if i < 41 and i % 5 == 0 and i != 0:
            if res == "first":
                res = "second"
            else:
                res = "first"
        if i > 40:
            if (i % 2) == 0:
                if res == "first":
                    res = "second"
                else:
                    res = "first"
    return res
