from sys import stdin

N = int(stdin.readline())
ans = 0


def isCross(r, row):
  for i in range(len(row)):
    if abs(len(row)-i) == abs(r-row[i]):
      return False

  return True


def dfs(row):
  c = len(row)
  if c == N:
    global ans
    ans += 1
    return
  for r in range(N):
    if r in row:
      continue

    if isCross(r, row) != True:
      continue

    newRow = row[:]
    newRow.append(r)

    dfs(newRow)


if N == 0:
  print(0)
else:
  row = [0]*N
  dfs([])
  print(ans)

# 깔끔한 코드
# 출처 : https://claude-u.tistory.com/245
# def adjacent(x):
#     for i in range(x):
#         if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
#             return False
#     return True


# #한줄씩 재귀하며 DFS를 실행
# def dfs(x):
#     global result

#     if x == N:
#         result += 1

#     else:
#         for i in range(N):
#             row[x] = i
#             if adjacent(x):
#                 dfs(x + 1)

# N = int(input())
# row = [0] * N
# result = 0
# dfs(0)
# print(result)
