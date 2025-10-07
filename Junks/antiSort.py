a = [8,6,7,2,9,3]

print(a)
for i in range(0,len(a)):
  if a[i] >= a[j]:
    temp = a[i]
    a[j] = temp
    print(a)
