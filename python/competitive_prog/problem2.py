import sys

# Return true or false if there are 2 numbers whose sum is equal to target.
# can epeat? 

a = [2,11,5,6,3,7]
tg1 = 9
tg2 = 7
tg3 = 19

def sumEqualTG(array, tg):
    data = {}
    # O(n)
    for item in array:
        tg_num = tg - item 

        if data.get(tg_num):
            return True 
        
        data[item] = True
    return False

# print('Res 1: ', sumEqualTG(a, tg1))
# print('Res 2: ', sumEqualTG(a, tg2))
# print('Res 2: ', sumEqualTG(a, tg3))

def readFromSTDIN():
    for line in sys.stdin:
        a, tg = list(line.strip().split(' '))
        a = list(map(int, a.split(',')))
        tg = int(tg)
        print(a, "", tg, "",sumEqualTG(a, tg))

readFromSTDIN()
# python problem2.py < data.txt > prueba.txt
