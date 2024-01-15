def filter_list(input_list):
    if len(input_list) % 10 != 0:
        raise ValueError('Input list length must be a multiple of 10')

    filtered_list = [input_list[i] for i in range(len(input_list)) if (i + 1) % 2 != 0 and (i + 1) % 3 != 0]
    return filtered_list
