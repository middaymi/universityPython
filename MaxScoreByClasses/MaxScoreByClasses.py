# Goldobina Svetlana
#
# output the best students in each class
# data of progress are in file


# print modified result_map
def print_result_map(dict):
    for i in sorted(dict, key=dict.__getitem__):
        print(i, ":", dict.get(i))


# result map
max_result_map = {}
try:
    # open file
    with open('results.txt', encoding="utf-8") as file:
        print(file)
        # read a line
        for file_string in file:
            file_string = file_string.split()

            # get class and score
            class_number = int(file_string[2])
            score = int(file_string[3])

            # append class if not exist in map
            max_result_map.setdefault(class_number)

            # get a max result by class
            value = max_result_map.get(class_number)

            # if new item or the current value bigger then existed
            if value is None or score > value:
                max_result_map.update({class_number : score})

    # print result
    print_result_map(max_result_map)

# if file is incorrect
except IndexError:
    print("Check the text of file")

    file.close()
except FileNotFoundError:
    print("File not found")
