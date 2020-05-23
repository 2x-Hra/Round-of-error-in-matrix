''' 
    sorry but comments are in persian language
    '''
import math

def sample_input(row):
    '''
        inja voroodi haro mikhune faghat va be soorate tuple bar migardoone
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
    '''
        bar asase tedade row va column miad matrix haro misaze 
        va be shekle array 2 boadi barmigardune
    '''
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

    '''
        inja ke START barname hast va mige ta vaghty ke "O" zade nashode voroodi begire 
        be shekli ke dakhele PDF gofte shode
        va bad har Sample ro dakhele 1 Tuple gharar mide va bad hame Sample haro dakhele 1 array kolli gharar midahad
    '''

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

def zeroMatrix(n,m):

    '''
        yek matrix misaze ke tamame elemnt hash 0 hast 
        ke baraye mohasebe matrix inverse khyli niaz bood
    '''

    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(0)
        matrix.append(row)
    return matrix

def r_c_eliminate(row, column, matrix):
    '''
         row va column ro az matrix hazf mikone va matrix jadid ra barmigardune 
         ke baraye mohasebe Determinane N*N niaz mishe
    '''
    _matrix = []
    n = len(matrix)
    for i in range(n):
        # 'the' row is eliminated
        if i!=row:
            _matrix_row = []
            for j in range(n):
                # 'the' column is eliminated
                if j!=column:
                    _matrix_row.append(matrix[i][j])
            _matrix.append(_matrix_row)
    return _matrix


def detrmnt_NXN (matrix):
    
    '''
        az esmes tabe malume inja Deteminan hesab mishe
    '''
    n = len(matrix)
    if (n == 2):
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]

    if (n > 2):
        det = 0
        for counter in range(n):
            # builds 'the' matrix ...
            _matrix = r_c_eliminate(0, counter, matrix)
            # for + and -
            if counter%2==0:
                det+=(matrix[0][counter]*detrmnt_NXN(_matrix))
            else:
                det-=(matrix[0][counter]*detrmnt_NXN(_matrix))
        return det
    


def minors(matrix):
    '''
        baraye tak tak elemnt ha satro sotoon ro migire 
        va determinane matrixe moonde ro hesab mikone
    '''
    matrix_length = len(matrix)
    minors = []
    
    if matrix_length==2:
        return matrix
    for i in range(matrix_length):
        row = []
        for j in range(matrix_length):
            row.append(detrmnt_NXN(r_c_eliminate(i, j, matrix)))
        minors.append(row)
    return minors

def co_factor_m(matrix):
    '''
        elemnt haye too matrix baraye Invers kardan
        manfi mikone 
    '''
    n = len(matrix)
    my_matrix = zeroMatrix(n,n)
    for i in range(n):
        for j in range(n):
            if (i%2==0 and j%2!=0) or (i%2!=0 and j%2==0):
                my_matrix[i][j] = -matrix[i][j]
            else:
                my_matrix[i][j] = matrix[i][j]
    return my_matrix

def adjugate_m(matrix):
    '''
        inja nesbat be ghotre asli makoos mishan
    '''
    n = len(matrix)
    my_matrix = zeroMatrix(n,n)
    counter = 0
    for i in range(n):
        for j in range(n):
            my_matrix[i][j] = matrix[i][j]
    
    if n==2:
        return [
            [my_matrix[1][1],my_matrix[0][1]],
            [my_matrix[1][0],my_matrix[0][0]]
        ]
    for i in range(n):
        for j in range(n):
            if j>=counter:
                tmp = my_matrix[i][j]
                my_matrix[i][j] = my_matrix[j][i]
                my_matrix[j][i] = tmp
        counter+=1
    return my_matrix

def divideByDetrmint(matrix, original_matrix):
    '''
         inja ma baraye hesab kardane Invers miaim oon 1/det ro hesab miknim
    '''
    n = len(matrix)
    my_matrix = zeroMatrix(n,n)
    det = detrmnt_NXN(original_matrix)
    for i in range(n):
        for j in range(n):
            my_matrix[i][j] = matrix[i][j]/det
    return my_matrix
            
def matrixInverse(matrix):
    '''
        oon 4 ta stepi ke baraye Invers niaz hast inja emal shode

    '''
    minor_matrix = minors(matrix)
    cofactor_matrix = co_factor_m(minor_matrix)
    adjugate_matrix = adjugate_m(cofactor_matrix)
    inverse_matrix = divideByDetrmint(adjugate_matrix, matrix)
    return inverse_matrix 



def matrixMultiply(a, b):

    '''
         zarbe 2 ta matrix, row * column
    '''
    ans = []
    a_rows_num = len(a)
    a_columns_num = len(a[0])
    b_columns_num = len(b[0])
    for i in range(a_rows_num):
        row_mult = []
        for k in range(b_columns_num):
            sum = 0
            for j in range(a_columns_num):
                sum+=a[i][j]*b[j][k]
            row_mult.append(sum)
        ans.append(row_mult)
    return ans

def solver(matrix, b):
    '''
        inja baraye halle moadele Ax = b , Hx = b
    '''
    matrix = matrixInverse(matrix)
    return matrixMultiply(matrix, b)


def residualVector(b, matrix, x):
    '''
    mohasebeye residual
    '''
    matrix_Mult_x = matrixMultiply(matrix,x)
    minus = []
    n = len(b)
    for i in range (n):
        row = []
        row.append(b[i][0]- matrix_Mult_x[i][0])
        minus.append(row)
    
    return minus



def residualVectorNorm(vector):
    '''
        mohasebeye Norm
    '''
    sum = 0
    n = len(vector)
    for i in range(n):
        sum+=(vector[i][0])**2
    return math.sqrt(sum)


'''
   here is Step one :
'''
samples_arr = samples()

for sample in samples_arr:
    A , H, b = sample


    '''here is Step Two :'''
    A_det = detrmnt_NXN(A)
    H_det = detrmnt_NXN(H)

    '''here is Step Three :'''
    if A_det!=0 and H_det!=0:

        A_inverse = matrixInverse(A)
        H_inverse = matrixInverse(H)


        '''here is Step Four :'''
        x1 = solver(A, b)
        x2 = solver(H, b)

        '''here is Step Five :'''
        vec1 = residualVector(b, A, x1)
        vec2 = residualVector(b, H, x2)

        '''here is Step Six :'''
        n1 = residualVectorNorm(vec1)
        n2 = residualVectorNorm(vec2)
        print("||b-Ax||=" + str(n1))
        print("||b-Hx||=" + str(n2))

