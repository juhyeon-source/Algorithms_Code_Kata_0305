def solution(numbers, num1, num2):
    answer = []
    for number in numbers:
        answer.append(number)
    return answer[num1:num2+1]