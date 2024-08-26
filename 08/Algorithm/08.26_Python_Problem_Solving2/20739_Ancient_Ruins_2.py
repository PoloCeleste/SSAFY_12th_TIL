﻿'''
땅속의 구조물을 촬영할 수 있는 특수 위성 카메라에 땅속에 묻힌 고대 구조물이 발견되었다.
구조물은 폭 1m, 길이 Xm의 직선 형태로 서로 평행 또는 직각으로만 자리하고 있어서, 1mx1m의
해상도의 사진데이터에 구조물이 있는 자리는 1로 나타난다.

0 0 0 0 0 0 0 0
0 0 0 0 0 0 Y 0
0 R R R R 0 Y 0
0 0 0 0 0 0 Y 0
0 0 0 G 0 0 Y 0
0 0 0 G 0 0 Y 0
0 B B 0 0 0 Y 0
0 0 0 0 0 0 0 0

사진의 해상도는 NxM이며, 구조물이 있는 곳은 1, 빈 땅은 0으로 표시된다.
위 그림의 경우 가장 긴 구조물은 노란색으로 표시된 영역이며, 길이는 6이다.
교차하거나 만나는 것처럼 보이는 구조물은 서로 다른 깊이에 묻힌 것이므로 직선인 구조만 고려하면 된다.

다음과 같은 경우는 길이가 3인 구조물 4개가 겹쳐 보이는 것이다.

0 1 0 0 0
1 1 1 0 0
0 1 0 0 1
0 0 0 0 1
0 0 1 1 1

평행한 모든 구조물은 서로 1m이상 떨어져 있어 빈칸으로 구분되며, 구조물의 최소 크기는 1x2m이다.
만약 다음과 같이 1x1m인 경우는 사진의 노이즈이다.

0 1 0
1 0 1
0 1 0

여러 구역의 사진 데이터가 주어질 때, 각 구역 별로 가장 긴 구조물의 길이를 알아내자.
만약 구조물이 하나도 없는 경우 0을 출력한다.

[입력]
첫 줄에 사진 데이터의 개수, 다음 줄부터 사진 데이터 별로 첫 줄에 N과 M,
이후 N개의 줄에 M개씩의 데이터가 제공된다.
(3<=N, M<=100)

[출력]
#과 1번부터 시작하는 사진 번호, 빈칸과 가장 긴 구조물의 길이를 출력한다.
'''

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0           # 가장 긴 구조물 길이
    for i in range(N):  # i행에서 가로 구조물 길이 확인
        cnt = 0             # 구조물 길이
        for j in range(M):
            if arr[i][j]:   # 구조물이면
                cnt += 1        # 길이 1m증가
                if max_v < cnt: # 가로 구조물의 최대 길이 찾기
                    max_v = cnt
                #max_v = max(max_v, cnt)
            else:
                cnt = 0
    for j in range(M):  # j열에서 세로 구조물 길이 확인
        cnt = 0
        for i in range(N):
            if arr[i][j]:   # 구조물인 경우
                cnt += 1
                if max_v < cnt:  # 가로 구조물의 최대 길이 찾기
                    max_v = cnt
            else:
                cnt = 0
    if max_v == 1:  # 노이즈인 경우
        max_v = 0
    print(f'#{t} {max_v}')