def solution(money):
    count = money//5500
    remoney = money%5500
    return [count, remoney]