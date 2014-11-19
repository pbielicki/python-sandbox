

def process_list(some_list):
    result = []
    for value in some_list:
        processed = do_something(value)
        result.append(processed)
    return result


# create new list by removing empty strings
some_list = [string for string in some_list if string != '']

# convert all strings to lowercase
some_list = [string.lower() for string in some_list]
