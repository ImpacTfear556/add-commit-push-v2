import os
import sys

print("testing")
numOfArgs = len(sys.argv)
print("Total Arguments Passed:" , numOfArgs) 
message = "Update files"
if numOfArgs == 3:   
  if sys.argv[1] == "-m":
    print("Number of args = 3 and p2 =-m")
    message = sys.argv[2]

print(message)



print("Add Commit Push")
print("\ngit status")
os.system("git status")

if numOfArgs != 2:   
    print("Do you want to continue with add commit push? (y):")
    confirm = input()
    if confirm != "y":
        print("canceling ", confirm)
        quit()

print("\ngit add -A")
os.system("git add -A")

commitStatment = '\ngit commit -m "' + message + '"'
print(commitStatment)
os.system(commitStatment)

print("\ngit push")
os.system("git push")
