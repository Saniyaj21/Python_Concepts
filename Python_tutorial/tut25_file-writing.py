# my_file = open("sani2.txt", "w")  #this is write mood which removes existing data and insert the new lines
my_file = open("sani2.txt", "a")
my_file.write("\nCreating using file writing mode append ")  #this is append mood which is used to add dada after the existing data
my_file.close()

# handle read and write both
f = open ("sani.txt", "r+")   # r+ is used for read and write at the same time 
print(f.read())
f.write(" Writing using r+ mood in tut 25")
f.close()