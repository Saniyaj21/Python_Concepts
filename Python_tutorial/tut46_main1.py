from pip import main


def sum(x, y):   # importing this funcyion in tut46_main2 file
    c = x + y
    print(f"Sum of {x} and {y} is : {c}")

if __name__=='__main__':  # if we import this files function on any file main will not run only functions will execute
    print("This is the main body which will not execute if we import this file ")
    sum(3,7)

