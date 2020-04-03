i = 1
x=0
i = int(input("digite um número"))
while i !=0:
    x=x+(i%10) #guarda o último termo e descarta os primeiros
    i=i//10 #descarta o último termo
print(x)

