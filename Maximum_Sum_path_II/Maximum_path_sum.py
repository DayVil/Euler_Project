def SortToList (linput = []):
    linput = [int(i) for i in linput]

    max_len = len(linput)
    pyramid_twod = []
    col = []
    col_test = False
    row_test = False
    counter = 0
    gen_counter = 0
    stopper = 0

    while row_test is False:
        while col_test is False:
            col.append(linput[gen_counter])
            gen_counter += 1
            if gen_counter == max_len:
                break

            elif counter == stopper:
                col_test = True
            
            else:
                counter += 1
        
        pyramid_twod.append(col)
        col = []
        col_test = False
        counter = 0
        stopper += 1

        if gen_counter == max_len:
            break

    return pyramid_twod


def MaxSum(lin = []):
    sum_way = []
    max_len = len(lin) - 1
    counter = 0
    pos_of_num = 0
    pos_of_num_t = 0
    sum_way_result = 0

    sum_way.append(lin[pos_of_num][pos_of_num_t])

    while counter != max_len:
        counter += 1
        pos_of_num_t = pos_of_num + 1
        num_one = lin[counter][pos_of_num]
        num_two = lin[counter][pos_of_num_t]

        if num_one >= num_two:
            sum_way.append(lin[counter][pos_of_num])
        
        else:
            sum_way.append(lin[counter][pos_of_num_t])
            pos_of_num = pos_of_num_t
        
    for x in sum_way:
        sum_way_result = sum_way_result + x
    
    return sum_way_result, sum_way
        

if __name__ == "__main__":
    #Input pyramid below.
    rinput = "75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
    
    raw_list_input = rinput.split()
    cleaned_up = SortToList(raw_list_input)
    result = MaxSum(cleaned_up)

    print(result)