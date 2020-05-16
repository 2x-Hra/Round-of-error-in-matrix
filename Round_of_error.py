def sample_input():
    
    # while(input() != "o"):

    row =int(input())
    # counter = 0

    A_input = input().split()
    A_input =[int(i) for i in A_input]
    print(A_input)
    
    H_input = input().split()
    H_input =[int(i) for i in H_input]
    print(H_input)

    b_input = input().split()
    b_input =[int(i) for i in b_input]


    return (A_input, H_input, b_input, row)



def martix_maker(row_number, elements):
    counter1=0
    counter2=0
    arr_out =[]
    arr_temp =[]
    i=0 
    while(counter1 < row_number):
        counter2 = 0
        arr_temp = []
        while( counter2 < row_number):
            arr_temp.append(elements[i])
            i += 1
            counter2 += 1

        arr_out.append(arr_temp)
        counter1 += 1
    print(arr_out)
A_vars , H_vars, b_vars , row = sample_input()

martix_maker(row,A_vars)