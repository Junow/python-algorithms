# Backtracking

- 해가 아니면 되돌아가서 다시 해를 찾아가는 기법
  - 최적화(optimazation) 문제와 결정 (decision) 문제 해결가능
  - 결정문제 종류
    - 미로찾기
    - n-Queen
    - Map coloring
    - 부분 집합의 합
- 초기상태에서 목표상태로 가는 경로를 탐색하는 기법
- 경로가 해답으로 이어지지 않으면 가지치기를 통해 시도횟수를 줄인다.
- 파이썬으로는 백트래킹 문제를 제시간내에 풀기 매우 힘들다.

```c
checknode (node v)
  IF promising(v)
    IF there is a solution at v
      write the solution
    ELSE
      FOR each child u of v
        checknode(u)

```
