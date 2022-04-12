# initializing the data and empty list
data = [1, [2, 3, [4, 5]], 6, [[7], [8, 9]]]
flat_list = []

# function
def flatten_list(data):
    # iterating over the data
    for element in data:
        # checking for list
        if type(element) == list:
            # calling the same function with current element as new argument
            flatten_list(element)
        else:
            flat_list.append(element)

# flattening the given list
flatten_list(data)

# printing the flat_list
print(flat_list)
