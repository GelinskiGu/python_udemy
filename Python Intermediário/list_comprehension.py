l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [variavel for variavel in l1]

ex2 = [v * 2 for v in l1]


l3 = list(range(100))
ex3 = [v for v in l3 if v % 10 == 0 if v % 3 == 0]

ex4 = [v if v % 3 == 0 else 0 for v in l3]
print(ex4)
