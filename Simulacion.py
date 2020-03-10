#Simulación de lo clasico a lo cuantico
#Autor: Julian Camacho



def multiplicacion_matrices(m_one, m_two):
    """(list, list) ->  list
    Multiplicacion de matrices"""

    if len(m_one[0]) == len(m_two):

        r = [[0 for i in range (len(m_one))] for j in range (len(m_two[0]))]
        
        for i in range (len(m_one)):
            for j in range(len(m_two[0])):
                for k in range(len(m_two)):
                    r[i][j] += m_one[i][k] * m_two[k][j]
                 
        return (r)
    
    else:
        
        print("Dimension incopatibles")


def accion_matriz_vector(m,v):
    """(list, list) -> list
    Accion de un vector sobre una matriz"""

    if len(m[0]) == len(v):
        
        r = [0 for i in range(len(v))]
        
        for i in range(len(m)):
            for k in range(len(v)):
                r[i] += round(m[i][k] * v[k], 3)

        return (r)
                
    else: 
        print("Dimension incopatibles")

    

def rectificar_m_ady(m):
    """(list) -> bool
    Rectificar que la matriz de adyacencia del sistema
    este correcta"""
    r = True
    for i in range(len(m)):
        cont = 0
        for j in range(len(m[0])):
            if m[i][j] != 0 and m[i][j] != 1:
                r = False
            if m[j][i] == 1:
                cont += 1
        if cont > 1:
            r = False
    return r

def experimento_rendijas(proba,blancos,rendijas):
    """(list, list, int) -> list
    Expoerimento probabilistico de rendijas multibles"""

    mat = [[0.0 for x in range(blancos+rendijas+1)] for x in range(blancos+rendijas+1)]
    cada = blancos//rendijas if blancos%2==0 else (blancos+1)//(rendijas)
    repite = False if blancos%2==0 else True
    j=1

    for k in range(1,rendijas+1):
        mat[k][0]=round(proba[k-1],1)
        for i in range(j,j+cada):
            mat[i][k]= round(1/cada,1)
        j+=cada-1

        for l in range(blancos-rendijas+1,len(mat)):
            mat[l][l]=1.0

    return mat

def experimento_rendijas_cuantico(proba,blancos,rendijas):
    """(list, list, int) -> list
    Expoerimento probabilistico de rendijas multibles cuantico"""

    for u in range(len(proba)):
        
        proba[u]=(proba[u][0]**2)+(proba[u][1]**2)
    
    mat = [[0.0 for x in range(blancos+rendijas+1)] for x in range(blancos+rendijas+1)]
    cada = blancos//rendijas if blancos%2==0 else (blancos+1)//(rendijas)
    j=1
    
    for k in range(1,rendijas+1):
        mat[k][0]=round(proba[k-1],1)
        for i in range(j,j+cada):
            mat[i][k]= round(1/cada,1)
        j+=cada-1
        for l in range(blancos-rendijas,len(mat)):
            mat[l][l]=1.0

            
    return mat

      
def expr_canicas(m_ady, v_inc, n_clics):
    """(list, list, int) -> list
    Simulacion de experimento de canicas donde m_ady
    es la matriz de adyacenca del sistema, v_inc es el
    vector de los estados iniciales y n_clics es el numero
    de clics que desea realizar"""

    if len(m_ady) == len(m_ady[0]) == len(v_inc):
        
        r = [[0 for i in range(len(m_ady))] for j in range(len(m_ady))]
        
        for o in range(len(m_ady)):
            for p in range(len(m_ady)):
                if o == p:
                    r[o][p] = 1
                
        for i in range(n_clics):   
            k = multiplicacion_matrices(r,m_ady)
            r = k
          
        return (accion_matriz_vector(r,v_inc))
        
    else:
        print("Dimension incopatibles")








def main():

    m_ady = [[0,1/3,2/3],[1/6,1/2,1/3],[5/6,1/6,0]]
    v_inc = [1/3,0,2/3]
    n_clics = 1

    print(expr_canicas(m_ady, v_inc, n_clics))
    print()
    for i in experimento_rendijas([1/2,1/2],4,2):
        print(i)
    print()
    for i in experimento_rendijas_cuantico([(1/(2**(1/2)),0),(1/(2**(1/2)),0)],5,2):
        print(i)
    
    
    
        
        
    

    
main()
