import sys


print("")

print("Hi there and thank you for visiting.\n ")


try:

    info = input("Plaese enter your name: ")

except:
       print("EOF")

print("")

info2 = input("Hello " + info + " would you like a cup of tea. [y\\n]")
print("")
yes = "y"
no = "n"

if info2 == yes:
    print("One cup of tea comming right up! ")
# elif info2 == no:
#     print(" You must not like tea haa! ")
else:
    sys.exit("You must not like tea Haah!\nThanks for visiting anyways.\n\n ")
