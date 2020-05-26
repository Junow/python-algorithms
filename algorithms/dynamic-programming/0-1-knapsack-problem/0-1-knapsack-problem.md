# 0-1 Knapsack Problem

> 주어진 아이템의 무게와 가치를 고려해서 최대 가치를 뽑아내는 문제

> 각 아이템을 쪼갤 수 없고 완전히 선택하거나 선택하지 않는 경우밖에 없기 때문에 0-1 이라고 불린다.

> 아이템의 가치와 무게인 value[], weight[] 그리고 최대 무게인 W 가 주어진다.

## Recursion

**방법**
가장 간단한 방법으로 아이템의 모든 부분집합에 대한 무게와 가치에 대한 테이블을 만드는 것. 그 중 W 보다 작은 부분집합 중에서 가치가 가장 높은 부분집합을 선택한다.

**Optimal Sub-Structure**
모든 부분집합에 대해 두가지 케이스가 있다.

- case 1: Optimal Subset 에 포함된다.
- case 2: Optimal Subset 에 포함되지 않는다.

n개 아이템의 최개 가치는 다음 두가지 값으로 얻어진다.

1. n-1개의 아이템과 무게로 얻은 최대 가치
2. n번 째 아이템의 가치와 n-1개의 아이템으로 얻은 최대 값, W 에서 n 번째 항목의 무게를 뺀 값

만약 n 번째 아이템의 무게가 W 보다 크다면 n 번째 아이템은 포함될 수 없고 case 1 의 경우만 가능하다.

```python

def knapsack(W, wt, val, n):
  if n == 0 or W == 0:
    return 0

  if (wt[n-1] > W):
    return knapSack(W, wt, val, n-1)
  else:
    return max(
      val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),
      knapSack(W, wt, val, n-1))

  val = [60,100,120]
  wt = [10,20,30]
  W = 50
  n = len(val)
  print knapSack(W, wt, val, n)
```

- Time Complexity: O(2^n)

sub-problem 이 다시 평가 되기 때문에 이 문제는 Overlapping sub-problem 의 특성을 갖는다.

## Dynampic Programming

같은 sub-problem 의 bottom-up 방식으로 경우 추가 공간을 이용해 재계산을 피할 수 있다.

**방법**

dp 라는 2차원 배열을 이용해서 모든 가능한 무게를 계산한다.
dp[i][j] 는 무게가 j 이고 i 개의 아이템을 선택했을 때 최대 가치를 나타낸다.

만약 현재 가능한 무게(w)에서 i-1 번째 아이템을 집을 수 있다면, i-1번째 아이템과 i-1번째 아이템의 무게 만큼을 뺐을때 가능한 최대무게 (아래 코드에서 K[i-1]w-wt[i-1]]) 를 더한값과 i-1 번째 아이템을 집지 않는 경우 (K[i-1][w]) 를 비교해서 큰 값을 취한다.

```python
def knapSack(W, wt, val, n):
  K = [[0 for x in range(W + 1)] for x in range(n+1)]

  for i in range(n+1):
    for w in range(W + 1):
      if i == 0 or w == 0:
        K[i][w] = 0
      elif wt[i-1] <= w:
        K[i][w] = max(val[i-1]) + K[i-1][w-wt[i-1]], K[i-1][w]
      else:
        K[i][w] = K[i-1][w]

  return K[n][W]

val = [60, 100, 120]
wt = [10,20,30]
W = 50
n = len(val)
print(knapSack(W, wt, val, n))
```

- Time Complexity: O(N\*W)
