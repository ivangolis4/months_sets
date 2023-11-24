months = {"JANUARY","FEBRUARY","MARCH","APRIL",
          "MAY","JUNE","JULY","AUGUST",
          "SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER"}

#IVAN N. GOLIS

first_group = set([])
second_group = set([])
s1 = set([])
s2 = set([])
def userInput():
    try:
        return int(input("Enter length:"))
    except ValueError:
        return userInput()


def my_birth_month():
    ins3 = input("Enter your birth month:").upper()
    if ins3.upper() in months:
        s1.add(ins3)
    else:
        print("Invalid Input.")
        return my_birth_month()


def my_classmate_birth_monh():
    ins4 = input("Enter your classmate birth month:").upper()
    if ins4.upper() in months:
        s2.add(ins4)
    else:
        print("Invalid Input.")
        return my_birth_month()



i = userInput()
print("======================================")
print("Enter first group:")
for in1 in range(i):
    fg = input(str(in1+1)+".")
    first_group.add(fg)

print("Enter second group:")
for in2 in range(i):
    sg = input(str(in2+1)+".")
    second_group.add(sg)

print("======================================")
print("Set 1:", first_group)
print("Set 2:", second_group)
print("======================================")
union = first_group.union(second_group)
inter = first_group.intersection(second_group)
diff = first_group.difference(second_group)
print("Union:", union)
print("Intersection:", inter)
print("Difference:", diff)
print("======================================")
my_birth_month()
my_classmate_birth_monh()

if s1 == s2:
    print("The same birth month.")
else:
    print("Not the same birth month.")






