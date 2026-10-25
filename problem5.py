n = 2*3*5*7* 2*2*3 *11*13*17*19 *2
print(n, all([n % i == 0 for i in range(1,20+1)]))
