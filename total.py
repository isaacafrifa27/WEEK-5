import sys

count = len(sys.argv)
total = 0

while count > 1:
    count -= 1
    total += float(sys.argv[count])

print("Total is", total)


args = sys.argv[1:]

# Check if there are no arguments provided
if len(args) == 0:
    print("No arguments were provided.")
else:
    total = 0
    for arg in args:
        total += float(arg)

    average = total / len(args)

    print("Total is", total)
    print("Average is", average)
