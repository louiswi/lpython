def get_int(num,min,default):
    while True:
        line = input(num)
        if not line and default is not None:
            return default
        i = int(line)
        if i < min:
            print('must be >=',min)
        else:
            return i

