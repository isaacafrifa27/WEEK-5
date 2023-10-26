def average(values):
    """ Calculates the average of the given list. """
    total = 0;
    for n in values:        	# total the given values
        total += float(n)
    return total/len(values)    # return calculated average

# initialisation statement
print("Welcome, utils module has been imported and initialised!")


import sys

def average(values):
    total = sum(float(val) for val in values)
    return total / len(values)

if __name__ == "__main__":

    if len(sys.argv) > 1:
        arguments = sys.argv[1:]
        avg = average(arguments)
        print("Average:", avg)
    else:
        print("No command-line arguments provided.")
