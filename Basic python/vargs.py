from function import sum
res =sum(22,11123)
print(res)
def sum2(*num):
   print(num)
   total=0
   for i in num:
      print(i)
      total+=i
   return total

ans=sum2(10,20,30)
print(ans)

def info(**name):
   print(name)
   for key,val in name.items():
      print(key,":",val)

info(name='labib',title='khan',age=22)

   