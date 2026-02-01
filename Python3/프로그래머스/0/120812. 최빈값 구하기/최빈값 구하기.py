def solution(array):
    answer = 0
    count = {}
    for i in array:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    in_max = max(count.values())
    
    modes = []
    for i in count:
        if count[i] == in_max:
            modes.append(i)
            
    if len(modes) > 1:
        answer = -1
    else:
        answer = modes[0]
    return answer