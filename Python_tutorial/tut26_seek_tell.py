f = open("sani.txt")
print("cursor is in ",f.tell())  # show where is the cursor in the file
f.seek(5)  # Change the position of the cursor in the file or reset
print("Now Cursor is in ",f.tell())
f.close()
