def solution(array):
    answer = 0
    temp = 0
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            if array[i] < array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    answer = array[len(array)//2]

    return answer