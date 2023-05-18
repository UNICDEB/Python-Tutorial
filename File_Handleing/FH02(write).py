#Open the file "demofile2.txt" and append content to the file:

f = open("demo01.txt", "a")
f.write("Hii, I am a Boy")
f.close()

#open and read the file after the appending:
f = open("demo01.txt", "r")
print(f.read())