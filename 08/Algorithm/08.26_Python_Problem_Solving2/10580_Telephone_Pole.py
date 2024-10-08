﻿'''
현우는 길을 가다가 전선들이 복잡하게 꼬여 있는 전봇대 두 개를 보았다.
두 전봇대는 높이가 매우 높으며, N개의 팽팽한 전선으로 연결되어 있었다.
두 전선이 끝점이 같은 경우는 없으나, 교차하는 경우는 있다.
이를 그림으로 하면 아래와 같다. (전선 3개가 있으며, 교차점 2개가 검은색으로 칠해졌다.)

ㅣ             ㅣ
ㅣ             ㅇ
ㅣ            /ㅣ
ㅣ          /  ㅣ
ㅇ--------ㅎ---ㅇ
ㅣ       /     ㅣ
ㅇ-----ㅎ------ㅇ
ㅣ    /        ㅣ
ㅣ  /          ㅣ
ㅣ/            ㅣ
ㅇ             ㅣ
ㅣ             ㅣ

세 개 이상의 전선이 하나의 점에서 만나지 않는다고 가정하자.
이 전봇대에는 총 몇 개의 교차점이 있을까?

[입력]
첫 번째 줄에 테스트 케이스의 수 TC가 주어진다.
이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다.
각 테스트 케이스는 다음과 같이 구성되었다.
첫 번째 줄에 주어지는 전선의 개수 N이 주어진다 (1 ≤ N ≤1000).
이후 N개의 줄에 두 양의 정수 Ai, Bi 가 주어진다. (1 ≤ Ai, Bi ≤ 10000)
이는 i번째 전선이, 첫번째 전봇대의 Ai cm 고도에 걸려 있고,
두 번째 전봇대의 Bi cm 고도에 걸려 있음을 뜻한다.
모든 Ai는 서로 다르고, 모든 Bi 도 서로 다르다. (두 전선의 끝점이 같은 경우가 없기 때문이다.)
 전선이 한 점에서 만나지 않게 입력이 주어진다.

[출력]
각 테스트 케이스마다 한 줄씩 교차점의 개수를 출력하라.
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    ab = [list(map(int, input().split())) for _ in range(N)]

    ab.sort()
    cnt = 0         # 교차 수
    for i in range(1, N):
        for j in range(i):
            if ab[j][1] > ab[i][1]: # a가 더 아래있지만 b가 더 높으면 교차점
                cnt += 1

    print(f'#{tc} {cnt}')