def solution(sides):
    answer = 0
    
    for i in range(0, len(sides)):
        for j in range(0, len(sides) - 1 - i):
            if sides[j] > sides[j + 1]:
                sides[j], sides[j + 1] = sides[j + 1], sides[j]

    
    if sides[0]+sides[1] > sides[2]:
        answer = 1
    else:
        answer = 2
            

    return answer