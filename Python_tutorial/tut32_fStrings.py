# f String --  String formating


# formating
me = "saniyaj"
me2= "mallik"
a = "This is %s" %me
print(a)

# formating
a1 = "This is {} {}"
b = a1.format(me,me2)
print(b)

# formating
b2 = f"This is another format. {me} {me2} {300+200}"
print(b2)