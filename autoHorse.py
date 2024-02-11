import os
import sys


while True:
    filename=input("Give file name =>")
    os.system("file "+filename+" 1>output.txt")
    outputcontext1=open("output.txt","r")
    text1=outputcontext1.read()
    word1="gzip"
    word2="tar"
    word3="bzip2"
    word4="Zip"
    word5="ASCII"
    if word1 in text1:
        os.system("cat output.txt \n")
        print(word1+" Is here\n Extracting =>\n\n")
        os.system("mv "+filename+" "+filename+".gz")
        os.system("gunzip "+filename+".gz")
        os.system("ls")
        continue
    if word2 in text1:
        os.system("cat output.txt \n")
        print(word2+" Is here \n Extracting =>\n\n")
        os.system("tar -xf "+filename)
        os.system("ls")
        continue
    if word3 in text1:
        os.system("cat output.txt \n ")
        print(word3+" Is here\n Extracting =>\n\n")
        os.system("mv "+filename+" "+filename+".bz2")
        os.system("bunzip2 "+filename+".bz2")
        os.system("ls")
        continue
    if word4 in text1:
        os.system("cat output.txt \n")
        print(word4+" Is here\n Extracting =>\n\n")
        os.system("unzip "+filename)
        os.system("ls")
        continue
    if word5 in text1:
        os.system("cat output.txt \n")
        print(word5+" Is here\n I will open it =>\n\n")
        os.system("cat "+filename)
        print("~~~~~~~~~~~~~~~~~BINGO~~~~~~~~~~~~~~~~~~")
        break
    else:
        print("BAD LUCK")
