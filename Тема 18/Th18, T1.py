# =============================================================================
# Imports practice
# 
#  Make a directory with 2 modules; make a function in one of them; then import this function in the other module and use that in your script of choice.
# =============================================================================

from Func1_18 import add_data

data_file = {}

add_data(data_file, 2020, 198)
add_data(data_file, 2019, 190)
add_data(data_file, 2018, 197)

data_file1 = {}

add_data(data_file1, 'a', 11)
add_data(data_file1, 'b', 3)
add_data(data_file1, 'c', 10)

print(data_file)
print(data_file1)

