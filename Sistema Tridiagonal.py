# Matriz A
A = [[2,-1,0,0,1], [-1,2,-1,0,0], [0,-1,2,-1,0], [0,0,-1,2,1]]
n = len(A)

# Vetor x e c

X = {}
C = {}

# Matriz L e U 
L = {}
U = {}

# Passo 1 a 3: Resolver Lc = b
# Passo 1

L[0,0]=A[0][0]
U[0,1]=A[0][1]/L[0,0]
C[0]=A[0][n]/L[0,0]

# Passo 2

for i in range(1,n-1):
    L[i,i-1]=A[i][i-1]
    L[i,i]=A[i][i]-L[i,i-1]*U[i-1,i]
    U[i,i+1]=A[i][i+1]/L[i,i]
    C[i]=(A[i][n]-L[i,i-1]*C[i-1])/L[i,i]

# Passo 3

L[n-1,n-2]=A[n-1][n-2]
L[n-1,n-1]=A[n-1][n-1]-L[n-1,n-2]*U[n-2,n-1]
C[n-1]=(A[n-1][n]-L[n-1,n-2]*C[n-2])/L[n-1,n-1]

# Passo 4 e 5: Resolver Ux = C

# Passo 4

X[n-1]=C[n-1]

# Passo 5

for i in range(n-2, -1, -1):
    X[i]=C[i]-U[i,i+1]*X[i+1]


print(X)



