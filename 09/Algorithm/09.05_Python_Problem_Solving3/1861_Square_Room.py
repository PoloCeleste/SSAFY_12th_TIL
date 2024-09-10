﻿"""
N2개의 방이 N×N형태로 늘어서 있다.
위에서 i번째 줄의 왼쪽에서 j번째 방에는 1이상 N2 이하의 수 Ai,j가 적혀 있으며,
이 숫자는 모든 방에 대해 서로 다르다.
당신이 어떤 방에 있다면, 상하좌우에 있는 다른 방으로 이동할 수 있다.
물론 이동하려는 방이 존재해야 하고, 이동하려는 방에 적힌 숫자가 현재 방에 적힌
숫자보다 정확히 1 더 커야 한다.
처음 어떤 수가 적힌 방에서 있어야 가장 많은 개수의 방을 이동할 수 있는지 구하는
프로그램을 작성하라.


[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N (1 ≤ N ≤ 103)이 주어진다.
다음 N개의 줄에는 i번째 줄에는 N개의 정수 Ai, 1, … , Ai, N (1 ≤ Ai, j ≤ N2)이
공백 하나로 구분되어 주어진다.
Ai, j는 모두 서로 다른 수이다.


[출력]
각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 
출력하고, 한 칸을 띄운 후, 처음에 출발해야 하는 방 번호와 최대 몇 개의 방을
이동할 수 있는지를 공백으로 구분하여 출력한다.
이동할 수 있는 방의 개수가 최대인 방이 여럿이라면 그 중에서 적힌 수가 가장 
작은 것을 출력한다.


[예제 풀이]
첫 번째 테스트 케이스는 1 또는 3이 적힌 곳에 있어야 한다.
두 번째 테스트 케이스는 3 또는 6이 적힌 곳에 있어야 한다.
"""

import sys
sys.stdin = open('input.txt')

from collections import deque

#     상  하  좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def search(x, y):
    # 해당 위치에서 q로 탐색
    # 첫 시작방도 이동으로 간주하므로 1칸으로 표기
    q = deque([(x, y, 1)])
    while q:
        x, y, cnt = q.popleft()
        for k in range(4):  # 4방향에 대해서
            nx = x + dx[k]
            ny = y + dy[k]
            # 범위를 벗어나지 않고, 원본 위치보다 정확히 1큰 경우,
            if 0 <= nx < N and 0 <= ny < N and data[x][y] + 1 == data[nx][ny]:
                q.append((nx, ny, cnt+1))   # 다음 위치도 조사 대상에 삽입
    # 모든 조사를 마친 후 결과 반환
    return cnt

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    result = []     # 각 방별 결과물 취합.

    # 전수 조사
    for i in range(N):
        for j in range(N):
            # data[i][j]의 방 번호와 i, j번째 위치에서 탐색한 결과 누적 이동수를 result에 추가
            result.append([data[i][j], search(i, j)])

    # 누적 이동수를 기준으로 내림차순 정렬후, 방 번호로 오름차순 정렬
    result.sort(key=lambda x: (-x[1], x[0]))
    print(f'#{tc}', *result[0])




'''
[입력]

2
2
1 2
3 4
3
9 3 4
6 1 5
7 8 2
'''

'''
[출력]

#1 1 2
#2 3 3
'''