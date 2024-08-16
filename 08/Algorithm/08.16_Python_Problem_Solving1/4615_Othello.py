﻿"""
4615. 재밌는(?) 오셀로 게임
오셀로라는 게임은 흑돌과 백돌을 가진 사람이 번갈아가며 보드에 돌을 놓아서 최종적으로 보드에 자신의 돌이 많은 사람이 이기는 게임이다.
보드는 4x4, 6x6, 8x8(가로, 세로 길이) 크기를 사용한다. 
6x6 보드에서 게임을 할 때, 처음에 플레이어는 다음과 같이 돌을 놓고 시작한다(B : 흑돌, W : 백돌).
4x4, 8x8 보드에서도 동일하게 정가운데에 아래와 같이 배치하고 시작한다.

ㅁㅁㅁㅁㅁㅁ
ㅁㅁㅁㅁㅁㅁ
ㅁㅁㅎㄱㅁㅁ
ㅁㅁㄱㅎㅁㅁ
ㅁㅁㅁㅁㅁㅁ
ㅁㅁㅁㅁㅁㅁ

그리고 흑, 백이 번갈아가며 돌을 놓는다.
처음엔 흑부터 시작하는데 이 때 흑이 돌을 놓을 수 있는 곳은 다음과 같이 4군데이다.

ㅁㅁㅁㅁㅁㅁ
ㅁㅁㅌㅁㅁㅁ
ㅁㅌㅎㄱㅁㅁ
ㅁㅁㄱㅎㅌㅁ
ㅁㅁㅁㅌㅁㅁ
ㅁㅁㅁㅁㅁㅁ

플레이어는 빈공간에 돌을 놓을 수 있다.
단, 자신이 놓을 돌과 자신의 돌 사이에 상대편의 돌이 있을 경우에만 
그 곳에 돌을 놓을 수 있고, 그 때의 상대편의 돌은 자신의 돌로 만들 수 있다.
(여기에서 "사이"란 가로/세로/대각선을 의미한다.)
(2, 3) 위치에 흑돌을 놓은 후의 보드는 다음과 같다.

ㅁㅁㅁㅁㅁㅁ
ㅁㅁㅁㅁㅁㅁ
ㅁㄱㄱㄱㅁㅁ
ㅁㅁㄱㅎㅁㅁ
ㅁㅁㅁㅁㅁㅁ
ㅁㅁㅁㅁㅁㅁ

이런 식으로 번갈아가며 흑, 백 플레이어가 돌을 놓는다.
만약 돌을 놓을 곳이 없다면 상대편 플레이어가 다시 돌을 놓는다.
보드에 빈 곳이 없거나 양 플레이어 모두 돌을 놓을 곳이 없으면 게임이 끝나고 그 때 보드에 있는 돌의 개수가 많은 플레이어가 승리하게 된다.


[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 보드의 한 변의 길이 N과 플레이어가 돌을 놓는 횟수 M이 주어진다. N은 4, 6, 8 중 하나이다.
그 다음 M줄에는 돌을 놓을 위치와 돌의 색이 주어진다.
돌의 색이 1이면 흑돌, 2이면 백돌이다.
만약 3 2 1이 입력된다면 (3, 2) 위치에 흑돌을 놓는 것을 의미한다.
돌을 놓을 수 없는 곳은 입력으로 주어지지 않는다.

[출력]
각 테스트 케이스마다 게임이 끝난 후 보드 위의 흑돌, 백돌의 개수를 출력한다.
흑돌이 30개, 백돌이 34인 경우 30 34를 출력한다.
"""
def f(i, j, bw, N):
    board[i][j] = bw
    for di, dj in [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]:
        ni, nj = i+di, j+dj
        tmp=[]
        while 0<=ni<N and 0<nj<N and board[ni][nj] == op[bw]:
            tmp.append((ni,nj))
            ni,nj = ni+di, nj+dj
        if 0<=ni<N and 0<=nj<N and board[ni][nj]==bw:
            for p,q in tmp:
                board[p][q]
# 1이면 흑돌, 2이면 백돌
B=1
W=2
op=[0,2,1]

T=int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 보드 한 변의 길이 N, 돌을 놓는 횟수 M
    play = [list(map(int, input().split())) for _ in range(M)]
    
    board = [[0]*N for _ in range(N)] # N x N board 준비, 0->N-1 인덱스 사용
    # 중심부 자리 배치
    # WB
    # BW
    board[N//2-1][N//2-1]=W
    board[N//2-1][N//2]=B
    board[N//2][N//2-1]=B
    board[N//2][N//2]=W

    for col, row, bw in play:
        f(row-1, col-1, bw, N)
    
    bcnt = wcnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j]==B:bcnt+=1
            elif board[i][j]==W:wcnt+=1
    print(f'#{tc} {bcnt} {wcnt}')
    

'''
[입력]
1
4 12
1 2 1
1 1 2
4 3 1
4 4 2
2 1 1
4 2 2
3 4 1
1 3 2
2 4 1
1 4 2
4 1 2
3 1 2
'''

'''
[출력]
#1 0 16
'''