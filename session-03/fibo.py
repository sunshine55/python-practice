def fibo():
    f0=0; f1=1; yield f0; yield f1
    while True:
        print 'Next is being created...'
        next = f0+f1
        yield next
        f0 = f1; f1 = next

def old_fibo(order=0):
    if order==0:
        return [0]
    elif order==1:
        return [0, 1]
    else:
        result = [0, 1]
        n = 1
        while n < order:
            result.append(result[n] + result[n-1])
            n += 1
        return result