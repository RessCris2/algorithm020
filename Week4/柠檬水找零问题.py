# 贪心策略 经典找零问题
def lemonadeChange(bills):
    change = dict()

    change.setdefault(5,0)
    change.setdefault(10,0)
    change.setdefault(20,0)

    for x in bills:
        if x == 5:
            change[5] +=1
        if x == 10:
            change[10] += 1
            if change[5] > 0:
                change[5] -= 1
            else:
                return False
        if x == 20:
            if change[10] > 0 :
                if change[5] >0 :
                    change[10] -= 1 
                    change[5] -= 1
                else:
                    return False
            elif change[5] >=3 :
                change[5] -= 3
            else:
                return False
    return True
        