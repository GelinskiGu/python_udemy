import time


def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)


g = gera()

for v in g:
    print(v)

"""
l1 = [x for x in range(1000)]
l2 = (x for x in range(1000))    isso é um gerador

"""
