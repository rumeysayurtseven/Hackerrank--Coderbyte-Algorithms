 count = 0
  for i in range(0,len(arr)-1):
    while arr[i] != i+1:
      t = arr[arr[i]-1]
      arr[arr[i]-1] = arr[i]
      arr[i]=t
      count+=1
