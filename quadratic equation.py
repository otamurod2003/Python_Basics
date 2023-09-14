import math
a = int(input('a sonni kiriting:'))
b = int(input('b sonni kiriting:'))
c = int(input('c sonni kiriting:'))
#qiymatlar kiritildi va o'zgaruvchilarga o'zlashtirildi
d=math.pow(b,2) - 4*a*c;
print('Diskriminant: ', d)

if(d<0):
    print('Ushbu kvadrat tenglama ildizga ega emas')
elif(d==0):
    x=(-b-math.sqrt(d))/2*a
    print('bitta yechimga ega: ', x)
elif(d>0):
    x1=(-b+math.sqrt(d))/2*a
    x2=(-b-math.sqrt(d))/2*a
    print('Ikkita ildizga ega. \n', 'x1 = ',x1,'x2 = ', x2)

