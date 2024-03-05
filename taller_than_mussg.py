def solution(array, height):
    answer = 0
    for i in range(len(array)):
        1 <= len(array) <= 100
        1 <= height <= 200
        1 <= array[i] <= 200
        if array[i] > height:
            answer += 1
    return answer