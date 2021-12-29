def sumDigits(n):
  sum=0
  while n!=0:
     sum+=n%5
     n=n//5
  return sum(n)
print (sumDigits(10,23,3,4,5))
