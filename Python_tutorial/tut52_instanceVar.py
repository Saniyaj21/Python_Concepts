# class variable and instance variable

class student:
    high_score = 97  # class variable  objects can not change this value
    pass  # pass will allow to skip null

sani = student()  # objects

shubha = student()
shubha.roll = 12  # shubha instance variable
print(shubha.roll)

print(student.high_score)
# sani.high_score = 55  # this can not change the class value it will create new variable of sani object
print(student.high_score)



