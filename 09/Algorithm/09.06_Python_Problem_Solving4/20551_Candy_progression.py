﻿"""
세현이는 세 개의 상자를 나란히 세워 놓았다. 첫 번째 상자에는 사탕 A개, 두 번째 상자에는 사탕 B개, 세 번째 상자에는 사탕 C개가 들어 있다.
세현이는 각 상자에 들어 있는 사탕의 개수가 순증가하기를 원한다. 즉, 두 번째 상자에 들어 있는 사탕의 개수가 첫 번째 상자에 들어 있는 사탕의 개수보다 더 많기를 원하고, 세 번째 상자에 들어 있는 사탕의 개수가 두 번째 상자에 들어 있는 사탕의 개수보다 더 많기를 원한다.
또한, 세현이는 모든 상자가 비어 있지 않기를 원한다. 즉, 모든 상자에 1개 이상의 사탕이 들어 있기를 원한다.
세현이가 이 두 조건을 만족시키기 위해 할 수 있는 일은, 상자 속에 들어 있는 사탕을 (0개 이상) 먹어 없애 버리는 것이다. 세현이가 조건을 만족시킬 수 있는지 판단하고, 만족시킬 수 있다면 최소 몇 개의 사탕을 먹어야 하는지 구하는 프로그램을 작성하라.

입력
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스는 한 개의 줄로 이루어진다. 각 줄에는 세 개의 자연수 A,B,C (1≤A,B,C≤3000)가 공백 하나를 사이로 두고 주어진다.

출력
각 테스트 케이스마다,
세현이가 사탕을 먹어치워서 조건을 만족시킬 수 없다면 -1을 출력한다.
만족시킬 수 있다면, 최소 몇 개를 먹어야 하는지 출력한다.
"""



'''
[입력]

4
3 2 1
1 2 3
3 5 5
5 6 6
'''
'''
[출력]

#1 -1   예제1: 어떤 방식으로 먹더라도 사탕의 개수가 순증가하게 할 수 없다.
#2 0    예제2: 이미 조건이 만족되어 있다.
#3 1    예제3: 두 번째 상자에 들어 있는 사탕 1개를 먹으면 된다.
#4 2    예제4: 첫 번째 상자 사탕 1개, 두 번째 상자 사탕 1개를 먹으면 된다.
'''