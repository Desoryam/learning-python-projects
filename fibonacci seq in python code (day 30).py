def f_seq(n):
  if n==0:
    return 0 
  elif n==1:
    return 1
  else:
    return (f_seq(n-1)+f_seq(n-2))
for i in range(20):
  print(f_seq(i),end=' ')
