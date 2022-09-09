class A:
  def A(self, y, x):
       a = {}
       for i, num in enumerate(y):
           if x - num in a:
               return (a[x - num], i )
           a[num] = i
print("index1 = %d, index2 = %d" % A().A((5,10,20,10,40,50,60,70),65))