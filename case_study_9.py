import random
import ru_local


def sell(d):
    a = [1, 2, 3]
    aa = random.choice(a)
    if aa == 1:
        print(ru_local.THE_BELGIAN_KING_WILL_BUYS_GRAIN_AT_10_D_E_FOR_GARNETS)
        print(ru_local.HOW_MUCH_GRAIN_TO_SELL)
        s = int(input())
        d['grain'] -= s
        d['money'] += s*10
    elif aa == 2:
        print(ru_local.QUEEN_OF_DENMARK_BUYS_GRAIN_14_D_E_FOR_GARNETS)
        print(ru_local.HOW_MUCH_GRAIN_TO_SELL)
        s = int(input())
        d['grain'] -= s
        d['money'] += s * 14
    else:
        print(ru_local.COMMERCIAL_UNION_BUYS_GRAIN_FOR_21_D_E_FOR_GARNETS)
        print(ru_local.HOW_MUCH_GRAIN_TO_SELL)
        s = int(input())
        d['grain'] -= s
        d['money'] += s * 21
    return d


def buy(d):
    print(ru_local.IN_THE_STATE_NEXT_DOOR_A_LARGE_SUPPLY_OF_GRAIN_SOME_OF_WHICH_THEY_SELL)
    print(ru_local.HOW_MUCH_GRAIN_TO_BUY)
    s = int(input())
    d['grain'] += s
    d['money'] -= s * 10
    return d


def sow(d):
    print(ru_local.HOW_MUCH_GRAIN_TO_ALLOCATE_FOR_SOWING)
    s = int(input())
    d['grain'] -= s
    i = random.randint(s-50, s+50)
    d['grain'] += i
    return d


def give(d):
    print(ru_local.HOW_MUCH_GRAIN_TO_DISTRIBUTE_TO_SUBJECTS)
    s = int(input())
    d['grain'] -= s
    if s < 250:
        d['smoot'] += 8
    if 250<s<500:
        d['smoot'] -= 5
    if 500<s<1000:
        d['smoot'] -= 3
    return d


def thief(d):
    if d['money'] >= 100:
        i = random.randint(100, 1000)
        print(ru_local.THIEF_1, i, ru_local.THIEF_2)
        d['money'] -= i
    else:
        print(ru_local.THIEF_3)
        d['money'] = 0
    return d


def flood(d):
    if d['grain'] >= 250:
        i = random.randint(250, d['grain'])
        print(ru_local.FLOOD_1, i, ru_local.FLOOD_2)
        d['grain'] -= i
    else:
        print(ru_local.FLOOD_3)
        d['grain'] = 0
    return d


def inheritance(d):
    i = random.randint(1000, 10000)
    g = random.randint(10, 100)
    print(ru_local.INHERITANCE_1,
          ru_local.INHERITANCE_2,
          ru_local.INHERITANCE_3, i,
          ru_local.INHERITANCE_4, g, ru_local.INHERITANCE_5)
    d['money'] += i
    d['the_land'] += g
    return d


def princess(d):
    # money - деньги из казны
    if d['money'] >= 500:
        i = random.randint(500, 1000)
        print(ru_local.PRINCESS_1,
              ru_local.PRINCESS_2, i, ru_local.PRINCESS_3)
        d['money'] -= i
    else:
        print(ru_local.PRINCESS_4,
              ru_local.PRINCESS_5, d['money'], ru_local.PRINCESS_3)
        d['money'] = 0
    return d


def rats(d):
    # количество зерна
    if d['grain'] >= 250:
        i = random.randint(250, 1000)
        print(ru_local.RATS_1, i, ru_local.RATS_2)
        d['grain'] -= i
    else:
        print(ru_local.RATS_3)
        d['grain'] = 0
    return d


def princess_dress(d):
    # money - деньги из казны
    if d['money'] >= 500:
        i = random.randint(500, 1000)
        print(ru_local.PRINCESS_DRESS_1,
              ru_local.PRINCESS_DRESS_2, i, ru_local.PRINCESS_DRESS_3)
        d['money'] -= i
    else:
        print(ru_local.PRINCESS_DRESS_4,
              ru_local.PRINCESS_DRESS_5)
        d['money'] = 0
    return d


def holiday(d):
    # money - деньги из казны
    if d['money'] >= 500:
        i = random.randint(500, 1000)
        print(ru_local.HOLIDAY_1, i,
              ru_local.HOLIDAY_2)
        d['money'] -= i
    elif d['money'] < 500:
        i = d['money']
        print(ru_local.HOLIDAY_3, i,
              ru_local.HOLIDAY_4)
        d['money'] = 0
    return d


def princess_HB(d):
    # money - деньги из казны
    if d['money'] < 500:
        i = random.randint(1000)
        print(ru_local.princess_HB_1,
              ru_local.princess_HB_2, i, ru_local.princess_HB_3)
        d['money'] -= i

    elif d['money'] >= 500:
        i = d['money']
        print(ru_local.princess_HB_4,
              ru_local.princess_HB_5, i, ru_local.princess_HB_3)
        d['money'] = 0
    return d


def war(d):
    a = [1, 2]
    sc = random.choice(a)
    d['money'] -= 500
    d['people'] -= 20
    if sc == 1:
        s = ru_local.WAR_1
    else:
        s = ru_local.WAR_2
    print(s, ru_local.WAR_3)
    yn = int(input())
    if yn == 1:
        if sc == 1:
            b = [1, 1, 1, 1, 0]
            v = random.choice(b)
            if v == 0:
                d['money'] -= 1000
                d['the_land'] *= 0.9
            else:
                d['money'] += 1000
                d['the_land'] *= 1.10
        else:
            c = [1, 0, 0, 0, 0]
            v = random.choice(c)
            if v == 0:
                d['money'] -= 1000
                d['the_land'] *= 0.9
            else:
                d['money'] += 5000
                d['the_land'] *= 1.50
    return d


def side_rebellion(d):
    print(ru_local.SIDE_REBELLION)
    yn = int(input())
    if yn == 1:
        d['money'] -= 200
        d['people'] -= 20
    a = [1, 0]
    v = random.choice(a)
    if v == 1:
        d['money'] -= 400
        d['people'] -= 40
    return d


def investition(d):
    print(ru_local.INVESTITION_1)
    print(ru_local.INVESTITION_2)
    s = int(input())
    a = [1, 1, 1, 1, 0]
    v = random.choice(a)
    if v == 1:
        d['money'] += 0.3*s
    else:
        d['money'] -= s
    return d


def expropriation(d):
    print(ru_local.EXPROPRIATION)
    yn = int(input())
    if yn == 1:
        d['money'] -= 500
        d['people'] -= 50
        a = [1, 0]
        v = random.choice(a)
        if v == 1:
            d['the_land'] += 100
        else:
            d['money'] -= 500
    return d


def magic(d):
    print(ru_local.MAGIC_1)
    print(ru_local.MAGIC_2)
    print(ru_local.MAGIC_3)
    yn = int(input())
    if yn == 1:
        d['money'] -= 500
    a = [1, 0]
    v = random.choice(a)
    if v == 1:
        d['grain'] += 1000
    return d


def print_d(d):
    s = ''
    a = list(d.keys())
    for i in a:
        z = str(d[i])
        s += i + ':' + ' ' + z + ';  '
    s = s[0:-1]
    s = s[0:-1]
    print(s)
    return d


def main():
    d = {'money': 5000, 'people': 100, 'the_land': 120, 'grain': 10000, 'smoot': 5, 'year': 0}
    while d['money'] > 0 and d['people'] > 49 and d['the_land'] > 49 and d['grain'] > 0 and d['smoot'] < 25:
        print_d(d)
        sell(d)
        buy(d)
        sow(d)
        give(d)
        list_def1 = [1,2,3,4,5]
        r1 = random.choice(list_def1)
        if r1 == 1:
            war(d)
        elif r1 == 2:
            side_rebellion(d)
        elif r1 == 3:
            investition(d)
        elif r1 == 4:
            expropriation(d)
        else:
            magic(d)
        list_def2 = [1, 2, 3, 4, 5, 6]
        r2 = random.choice(list_def2)
        if r2 == 1:
            thief(d)
        elif r2 == 2:
            flood(d)
        elif r2 == 3:
            inheritance(d)
        elif r2 == 4:
            princess(d)
        elif r2 == 5:
            princess_dress(d)
        elif r2 == 6:
            holiday(d)
        else:
            princess_HB(d)
        d['year'] += 1
    print(ru_local.YOU_DID_NOT_COPE_WITH_TASKS_OF_RULER_SO_YOU_OVERTHREW)


if __name__ == "__main__":
    main()