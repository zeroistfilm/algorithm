# https://programmers.co.kr/learn/courses/30/lessons/64063
import sys
sys.setrecursionlimit(10000000)

def findEmptyRoom(number,rooms):
    if number not in rooms:
        rooms[number] = number
        return number
    empty = findEmptyRoom(rooms[number]+1,rooms)
    rooms[number] = empty
    return empty

def solution(k, room_number):
    answer=[]
    rooms={}
    for number in room_number:
        emptyRoom = findEmptyRoom(number, rooms)
        answer.append(emptyRoom)
    return answer

print(solution(10, [1, 3, 4, 1, 3, 1]))

