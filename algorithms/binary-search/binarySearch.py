def binarySearch(arr, l, r, target):
  m = int((l+r)/2)
  if l > r:
    return None
  if arr[m] == target:
    return m
  if arr[m] < target:
    return binarySearch(arr, m+1, r, target)
  if arr[m] > target:
    return binarySearch(arr, l, m-1, target)
