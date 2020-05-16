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

A_vars , H_vars, b_vars , row = sample_input()