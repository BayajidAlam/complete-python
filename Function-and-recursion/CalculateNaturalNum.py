def Calculate_natural_num(n):
   if n== 0:
     return 0
   return n + Calculate_natural_num(n-1)

print(Calculate_natural_num(5))