def combination(arr, r):
  for i in range(len(arr)):
    if r == 1:
      yield [arr[i]]
    else:
      for next in combination(arr[i+1:], r-1):
        yield [arr[i]] + next
