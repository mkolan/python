def my_range(start,stop,step):
    if stop <= start:
        raise RuntimeError("start must be smaller than stop")
    else:
        i = start
        while i < stop:
            yield i
            i += step


for k in my_range(10,30,3):
    print(k)