import sys


print("")

print("Hi there and thank you for visiting.\n ")


try:

    info = input("Plaese enter your name: ")
except:
       print("EOF")

print("")

try:
    info2 = str(input("Hello " + info + " would you like a cup of tea. [y\\n]"))
except NameError: pass


print("")
yes = "y"
no = "n"

try:
    if info2 == yes:
        print("One cup of tea comming right up! ")
except NameError: pass

else:
     sys.exit("You must not like tea Haah!\nThanks for visiting anyways.\n\n ")
