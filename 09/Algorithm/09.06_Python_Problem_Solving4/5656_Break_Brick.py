"""
구슬을 쏘아 벽돌을 깨트리는 게임을 하려고 한다.
구슬은 N번만 쏠 수 있고, 벽돌들의 정보는 아래와 같이 W x H 배열로 주어진다.
( 0 은 빈 공간을 의미하며, 그 외의 숫자는 벽돌을 의미한다. )

게임의 규칙은 다음과 같다.

① 구슬은 좌, 우로만 움직일 수 있어서 항상 맨 위에 있는 벽돌만 깨트릴 수 있다.
② 벽돌은 숫자 1 ~ 9 로 표현되며,
구슬이 명중한 벽돌은 상하좌우로 ( 벽돌에 적힌 숫자 - 1 ) 칸 만큼 같이 제거된다.
③ 제거되는 범위 내에 있는 벽돌은 동시에 제거된다.

예를 들어 아래와 같이 4 번 벽돌에 구슬이 명중할 경우,
9번 벽돌은 4 번 벽돌에 반응하여,
동시에 제거된다.

④ 빈 공간이 있을 경우 벽돌은 밑으로 떨어지게 된다.

N 개의 벽돌을 떨어트려 최대한 많은 벽돌을 제거하려고 한다.
N, W, H, 그리고 벽돌들의 정보가 주어질 때,
남은 벽돌의 개수를 구하라

[제약 사항]
1. 1 ≤ N ≤ 4
2. 2 ≤ W ≤ 12
3. 2 ≤ H ≤ 15

[입력]
가장 첫 줄에는 총 테스트 케이스의 개수 T 가 주어지고,
그 다음 줄부터 T 개의 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 N, W, H 가 순서대로 공백을 사이에 두고 주어지고,
다음 H 줄에 걸쳐 벽돌들의 정보가 1 줄에 W 개씩 주어진다.

[출력]
출력은 #t 를 찍고 한 칸 띄운 다음 정답을 출력한다.
(t 는 테스트 케이스의 번호를 의미하며 1 부터 시작한다)
"""
dij=[[-1,0],[1,0],[0,-1],[0,1]]

def shoot(level, remains, now_arr):
    global min_blocks
    # 구슬을 모두 발사 or 남은 벽돌 0이면 종료
    if level==N or remains==0:
        min_blocks=min(min_blocks,remains)
        return
    for col in range(W):
        # 방법1
        # 1. col 위치에 쏘기 전 상태 복사
        # 2. 원본 리스트의 col위치에 구슬발사
        # 3. level+1번 상태로 이동(다음재귀호출)
        # 4. col위치에 쏘기 전 상태 복구

        # 방법2 (복구시간 너무 오래걸림)
        # 1. col 위치에 쏘기 전 상태를 복사
        # 2. 복사한 리스트의 col위치에 구슬 발사
        # 3. 다음 재귀 호출 시 쏘고 난 상태 같이 넘김

        copy_arr=[row[:] for row in now_arr]

        # col 위치에 구슬 발사
        # 1. 첫번째로 만나는 벽돌 위치 찾기

        row=-1
        for r in range(H):
            if copy_arr[r][col]:
                row=r
                break
        if row==-1:continue
        # 벽돌이 없다면 다음열로 넘어감

        # 2. 벽돌의 값만큼 연쇄적으로 제거
        # 행, 열, 파워
        li=[(row,col,copy_arr[row][col])] # 깨질 벽돌 저장
        now_remains=remains-1
        copy_arr[row][col]=0

        while li:
            r, c, p=li.pop()
            for k in range(1,p):
                for di,dj in dij:
                    nr,nc=r+(di*k),r+(dj*k)

                    if nr<0 or nr>=H or nc<0 or nc>=W:continue
                    if copy_arr[nr][nc]==0:continue
                    li.append((nr, nc, copy_arr[nr][nc]))
                    copy_arr[nr][nc]=0
                    now_remains-=1
        for c in range(W):
            idx=H-1
            for r in range(H-1,-1,-1):
                if copy_arr[r][c]:
                    copy_arr[r][c],copy_arr[idx][c]=copy_arr[idx][c],copy_arr[r][c]#가독성 위해 이와 같이 구현
                    idx-=1
        shoot(level+1,now_remains,copy_arr)

for t in range(1, int(input())+1):
    N,W,H=map(int, input().split())
    # 최소벽돌
    # 현재 벽돌이 다 깨지면 더이상 진행 X
    # 현재 남은 벽돌 수 저장
    arr=[list(map(int,input().split())) for _ in range(N)]
    min_blocks=1e9
    blocks=0

    for row in arr:
        for e in row:
            if e:
                blocks+=1

    shoot(0,blocks,arr)

    print(f'#{t} {min_blocks}')
'''
[입력]

5
3 10 10
0 0 0 0 0 0 0 0 0 0
1 0 1 0 1 0 0 0 0 0
1 0 3 0 1 1 0 0 0 1
1 1 1 0 1 2 0 0 0 9
1 1 4 0 1 1 0 0 1 1
1 1 4 1 1 1 2 1 1 1
1 1 5 1 1 1 1 2 1 1
1 1 6 1 1 1 1 1 2 1
1 1 1 1 1 1 1 1 1 5
1 1 7 1 1 1 1 1 1 1
2 9 10
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0 0
1 1 0 0 1 0 0 0 0
1 1 0 1 1 1 0 1 0
1 1 0 1 1 1 0 1 0
1 1 1 1 1 1 1 1 0
1 1 3 1 6 1 1 1 1
1 1 1 1 1 1 1 1 1
3 6 7
1 1 0 0 0 0
1 1 0 0 1 0
1 1 0 0 4 0
4 1 0 0 1 0
1 5 1 0 1 6
1 2 8 1 1 6
1 1 1 9 2 1
4 4 15
0 0 0 0 
0 0 0 0 
0 0 0 0 
1 0 0 0 
1 0 0 0 
1 0 0 0 
1 0 0 0 
1 0 5 0 
1 1 1 0 
1 1 1 9 
1 1 1 1 
1 6 1 2 
1 1 1 5 
1 1 1 1 
2 1 1 2 
4 12 15
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
'''

'''
[출력]

#1 12
#2 27
#3 4
#4 8
#5 0
'''