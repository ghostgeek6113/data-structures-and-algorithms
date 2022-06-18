# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    coins = 0
    while money:
        if money % 10 != 0 and money % 5 != 0:
            money = money - 1
            coins += 1
        elif money % 10 == 0:
            money = money - 10
            coins += 1
        elif money % 5 == 0:
            money = money - 5
            coins += 1
    return coins


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
