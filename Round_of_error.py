def sample_input(row):
    '''

    '''
    row =int(row)

    A_input = input().split()
    A_input =[float(i) for i in A_input]
    H_input = input().split()
    H_input =[float(i) for i in H_input]
    b_input = input().split()
    b_input =[float(i) for i in b_input]


    return (A_input, H_input, b_input, row)



def martix_maker(row,coloumn, elements):
    counter1=0
    counter2=0
    arr_out =[]
    arr_temp =[]
    i=0 
    while(counter1 < row):
        counter2 = 0
        arr_temp = []
        while( counter2 < coloumn):
            arr_temp.append(elements[i])
            i += 1
            counter2 += 1

        arr_out.append(arr_temp)
        counter1 += 1
    
    return arr_out

def samples():

    row = input()
    all_matrix = []
    while(row != "o" ):
        A_vars , H_vars, b_vars , row = sample_input(row)

        A_matrix = martix_maker(row,row,A_vars)
        H_matrix = martix_maker(row,row,H_vars)
        b_matrix = martix_maker(row,1,b_vars)

        all_matrix.append((A_matrix, H_matrix, b_matrix))
        row = input()
    return all_matrix


def determinant(row, elements):
    

print(samples())