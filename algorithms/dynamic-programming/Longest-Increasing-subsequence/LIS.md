# Longest Increasing Subsequence

> 길이 N 의 배열에서 오름차순을 이루는 subsequece 의 최대 길이를 구하는 문제이다. 간단하게는 O(N^2) 의 시간복잡도를 가지는 dynamic programming 형식의 접근이 있고 binary search 를 이용한다면 시간복잡도를 O(NlogN) 까지 줄일 수 있다.

## O(N^2)

```c
lengthOfLis = 0
dp[] = initialize all with 1
for i <- 0 to N
  for j <- 0 to i
    if arr[i] < arr[j]
      dp[i] = max(dp[i], dp[j] + 1)
  lengthOfLis = max(lengthOfLis, dp[i])
```

단순하게 모든 원소 쌍들을 비교해보면 답을 알 수 있다. 대신 모든 쌍을 검사하는데에 O(N^2) 의 시간복잡도가 걸린다.
i 번째 아이템을 가지고 0 부터 i-1 까지 의 원소들이 자기보다 작은지 검사하고 작다면 +1 씩 더해준다.

```python
def lisNSquare(arr):
  N = len(arr)
  dp = [1]*N                          # 자기자신만 쳐도 1이기 떄문에
  answer = 0
  for i in range(N):
    for j in range(i):
      if arr[i] > arr[j]:             # increasing 인지 확인
        dp[i] = max(dp[i], dp[j] + 1) # increasing 이기 때문에 j 고르고 i 고르면 +1 됨
    answer = max(answer, dp[i])       # 최대값 업데이트

  return answer
```

## O(NlogN)

O(N^2) 의 복잡도로는 input 이 큰 경우에는 제 시간내에 못 풀수도 있다. 그래서 binary search (lower bound) 를 이용해서 풀 수 있다. 이 풀이는 dynamic programming 기법은 아니다. (아마도?)

빈 배열(dp)부터 시작하며, arr 에 들어있는 값을 하나씩 꺼내서 increasing subsequence 를 만들 수 있는 자리를 찾는다.

빈자리를 찾을 때 lower_bound 를 이용하는데 인자로 넘긴 배열에서 x 원소가 들어갈 수 있는 위치를 binary search 로 찾아준다. 일반적인 binary_search 에서는 찾고자 하는 값이 없으면 -1 를 리턴하면서 탐색이 종료되지만, lower_bound 는 찾고자 하는 값 이상이 나오는 첫번째 위치를 알려준다.
(upper_bound 는 찾고자 하는 값 보다 큰 위치를 알려준다.)

만약 찾은 자리가 맨 뒤라면 dp 배열 마지막에 추가해주고 전체 길이가 +1 늘어난다.

만약 찾은 자리가 맨 뒤가 아니라면 중간에 들어가게 되는데 이때는 전체 길이는 변하지 않는다.

어떻게 보면 삽입정렬 하고도 비슷한 접근이라고 느껴진다. 삽입 정렬에서는 들어갈 위치를 찾으면 기존값을 한칸씩 밀어난다. 하지만 LIS 문제에서는 기존 arr 의 원소들의 상대적인 위치를 바꾸면 안되기 때문에 그리고 본래 목적이 정렬이 아니기 때문에 들어갈 만한 위치를 찾고나서 그냥 기존값을 덮어 씌워버린다.

```c
dp[] = initialize all with 0
length = 0
for num in arr
 index = lower_bound(dp, num, 0, length)
 if index < 0:
   i=0
 dp[index] = num
 if i == length
   length = length+1

return length
```

```python
def lisNlogN(arr):
  N = len(arr)
  dp = [0]*N
  length = 0

  for num in arr:
    i = bisect_left(dp, num, 0, length)      # num 이 들어갈 만한 위치를 찾음 (dp 배열을 오름차 순으로 만들 수 있는 위치를 찾음)
    if i<0:                                  # 원하는 값이 없다면 (num 이 dp 안에 있는 어떤 값보다 작다는 것)
      i = 0
    dp[i] = num                              # 해당위치에 num 삽입
    if i == length:                          # 방금 넣은 위치가 젤 마지막 위치면 최대길이를 갱신해줌
      length += 1

  return length
```
