def NonRepeat(s):
 
   for i in s:
 
       if (s.find(i,(s.find(i)+1))) == -1:
 
           print(f'first repetation word is',i)
 
           break
 
   return
 
x = 'sysylsy' 
NonRepeat(x)