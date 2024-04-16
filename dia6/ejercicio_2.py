def freiler (numeros,target ): #creamos la variable que vamos implmetar 
    
    nums={}                     #creamos un dicionario donde se guardaran 

    for i ,num in enumerate(numeros):  # creamos un ciclo for para recorrer los numero que componen nuestra lista 
        comple= target - num
        if comple in nums:
            return [nums[comple],i]
        
        nums[num]=i
            
        
    return["no hay nada ,no existe "]


numeros=[8,20,16,5,3,2,4,3]               # definimos que numeros estaran dentro de nuestra lista 
target=36                                 #este sera el objetivo a alcazar   

print(freiler(numeros,target))            

#hecho por freiler cc:1010075774