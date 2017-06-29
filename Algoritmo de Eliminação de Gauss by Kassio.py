A = [[0,1,0,3,4], [2,1,-1,1,1], [3,-1,-1,2,-3], [-1,2,3,-1,4]]

n = len(A) # quantidade de linhas

x = [0 for i in range(n)]

# Passo 1
for i in range(0, n-1):
    # Passo 2
    p = i
    for j in range(i, n):
        if(A[p][i]==0):
            p = p + 1
                        
    if(p == n):
        print('Não existe solução única')
    else:
        # Passo 3
        if(p != i):
            A[p], A[i] = A[i], A[p]

        # Passo 4
        for j in range(i+1,n):
            # Passo 5
            m = A[j][i]/A[i][i]
            # Passo 6
            for k in range(0,n+1):
                A[j][k]=A[j][k]-m*A[i][k]
    # Passo 7
if(A[n-1][n-1]==0):
    print('Não existe solução única')
else:
    # Passo 8
    x[n-1]=A[n-1][n]/A[n-1][n-1]

    # Passo 9
    for i in range(n-2, -1, -1):
             
        soma=A[i][n]
        for j in range(i+1, n):
            soma=soma-A[i][j]*x[j]
                
            x[i] = (soma/A[i][i])
# Passo 10
print(x)
        
    
    
        
