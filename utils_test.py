import my_utils

my_utils.average([10, 23, 30])
print("Average is", my_utils.average([10, 23, 30]))


my_utils.average([10.2, 8.8, 2.6])
print("Another average is", my_utils.average([10.2, 8.8, 2.6]))


from my_utils import average

average1 = average([10, 23, 30])
print("Average is", average1)

average2 = average([10.2, 8.8, 2.6])
print("Another average is", average2)


