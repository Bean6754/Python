import os, fnmatch

def findReplace(directory, find, replace, filePattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                s = f.read()
            s = s.replace(find, replace)
            with open(filepath, "w") as f:
                f.write(s)

user_input1 = input("Directory (e.g: www): ")
user_input2 = input("String to replace: ")
user_input3 = input("Replace with string: ")
user_input4 = input("File extention (e.g: html): ")

findReplace(user_input1, user_input2, user_input3, "*." + user_input4)
