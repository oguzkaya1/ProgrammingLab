def my_matrix_addition(m_1,m_2): 
    result=[]
    for row in range(len(m_1)):
        result.append([])
        for column in range(len(m_1[0])):
            result[row].append(m_1[row][column]+m_2[row][column])
    return result
#-------------------------------------------------------------------
def my_matrix_substraction(m_1,m_2): 
    result=[]
    for row in range(len(m_1)):
        result.append([])
        for column in range(len(m_1[0])):
            result[row].append(m_1[row][column]-m_2[row][column])
    return result
#-------------------------------------------------------------------
def my_matrix_scalar_product(alpha,m_1): 
    result=[]
    for row in range(len(m_1)):
        result.append([])
        for column in range(len(m_1[0])):
            result[row].append(m_1[row][column]*alpha)
    return result
#------------------------------------------------------------------
def f_1(matrix_1,i):    
    return matrix_1[i]

def f_2(matrix_1,j):    
    my_j_th_col=[]
    for row in matrix_1:
        for indis in range(len(row)):
            if(indis==j):
                my_j_th_col.append(row[indis])
    return my_j_th_col
#-------------------------------------------------------------------
def my_vector_inner_product(v,w):
    size=len(v)
    my_result=[]
    for i in range(size):
        my_result.append(0)
    
    for i in range(size):
        my_result[i]=v[i]*w[i]
    t=0
    for i in range(size):
        t=t+my_result[i]
    return t
#-------------------------------------------------------------------
def my_matrix_multiply(m_1,m_2):
    result=[]
    for row in range(len(m_1)):
        result.append([])
        for column in range(len(m_2[0])):
            a=f_1(m_1,row)
            b=f_2(m_2,column)
            c=my_vector_inner_product(a,b)
            result[row].append(c)
    return result
#-------------------------------------------------------------------
def det_from_2_by_2(m_1):
    s_1=m_1[0][0]*m_1[1][1]
    s_2=m_1[0][1]*m_1[1][0]
    s_3=s_1-s_2
    return s_3
#-------------------------------------------------------------------
def delete_row_col_from_matrix(m_1,m,n):
    result=[]
    size_1=(len(m_1))
    size_2=(len(m_1[0]))
    
    for i in range(size_1):
        if(i==m):
            continue
        row_1=[]
        for j in range(size_2):
            if(j==n):
                continue
            row_1.append(m_1[i][j])
        result.append(row_1)
    return result
#------------------------------------------------------------------
def det_from_3_by_3(m_1):
    a_1=m_1[0][0]
    a_2=delete_row_col_from_matrix(m_1,0,0)
    a_3=det_from_2_by_2(a_2)
    a_4=a_1*a_3
    
    b_1=m_1[0][1]
    b_2=delete_row_col_from_matrix(m_1,0,1)
    b_3=det_from_2_by_2(b_2)
    b_4=b_1*b_3
    
    c_1=m_1[0][2]
    c_2=delete_row_col_from_matrix(m_1,0,2)
    c_3=det_from_2_by_2(c_2)
    c_4=c_1*c_3
    
    return a_4-b_4+c_4
#-----------------------------------------------------------------
def det_from_4_by_4(m_1):
    a_1=m_1[0][0]
    a_2=delete_row_col_from_matrix(m_1,0,0)
    a_3=det_from_3_by_3(a_2)
    a_4=a_1*a_3
    
    b_1=m_1[0][1]
    b_2=delete_row_col_from_matrix(m_1,0,1)
    b_3=det_from_3_by_3(b_2)
    b_4=b_1*b_3
    
    c_1=m_1[0][2]
    c_2=delete_row_col_from_matrix(m_1,0,2)
    c_3=det_from_3_by_3(c_2)
    c_4=c_1*c_3
    
    d_1=m_1[0][3]
    d_2=delete_row_col_from_matrix(m_1,0,3)
    d_3=det_from_3_by_3(d_2)
    d_4=d_1*d_3
    
    return a_4-b_4+c_4-d_4
