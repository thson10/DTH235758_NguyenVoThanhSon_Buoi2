for i in range(1,11):
    for j in range(2,10):
        line = "{0} x {1:>2} = {2:>2}" .format(j,i,j*i)
        print(line, end="\t")
    print()