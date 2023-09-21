print("Welcome to the right triangle checker")
a = int(input("put the lenght of the side a in: "))
print(a)
hyp = int(a)
b = int(input("put the lenght of the side b in: "))
print(b)
if b > a:
    hyp = int(b)
    Kat1 = int(a)
else:
    Kat1 = b
c = int(input("put the lenght of the side b in: "))
if c > hyp:
    hyp = int(c)
    Kat1 = int(b)
    Kat2 = int(a)
else:
    Kat2 = int(c)
print(c)
print("calculating....")

print("hyp = " + str(hyp))
print("kat1 = " + str(Kat1))
print("kat2 = " + str(Kat2))

if hyp*hyp == Kat1*Kat1+Kat2*Kat2:
    print("Calculated! It is a right triangle.")
else:
    print("Calculated! It is not a right triangle")


