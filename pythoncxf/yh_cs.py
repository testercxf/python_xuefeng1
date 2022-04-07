import time


#循环代码优化测试
start = time.time()
for i in range(10000):
    result = []
    for m in range(10000):
        result.append(i*1000+m*100)
end = time.time()
print("一共耗时：%f"%(end-start))


start2 = time.time()
for i in range(10000):
    result = []
    c = i*1000
    for m in range(10000):
        result.append(c+m*100)
end2 = time.time()
print("一共耗时：%f"%(end2-start2))
