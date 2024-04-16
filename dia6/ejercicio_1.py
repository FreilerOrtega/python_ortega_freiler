head=[1,15,65,4,3,1,2,3,4,5,5,6,6,7,10,10] # la lista dada  la sometemos al proceso de eliminar los numeros repetidos 
nlista=list(set(head))         #procedemos a almacenar la lista para eliminar  los numeros repetidos
                                # comando set son un tipo que permite almacenar varios elementos y acceder a ellos de una forma muy similar a las listas pero con ciertas
nlista.sort()                            

print(nlista)                   #imprimimos en pantalla la lista actualizada y de forma ordenada

