import Maximum_path_sum as Ms

pyramid_file = open(r"D:\ProgrammProjects\Python\Maximum_path_sum\triangle.txt", "r")
pyra_list = []
clean_string = ""

for x in pyramid_file:
    stripped_line = x.strip()
    split_line = stripped_line.split()

    for i in split_line:
        clean_string = clean_string + " " + i

pyra_list_str = clean_string.split()
pyra_list = Ms.SortToList(pyra_list_str)
result = Ms.MaxSum(pyra_list)

print(result)