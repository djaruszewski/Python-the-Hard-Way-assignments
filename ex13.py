from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second cariable is:", second)
print("Your third variable is:", third)

script = input("What's your name? ")
print(f"Hello {script}.")