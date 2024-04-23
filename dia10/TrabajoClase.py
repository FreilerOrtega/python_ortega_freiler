def encontrarnum(nums, objetivo):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] < objetivo:
            l = mid + 1
        elif nums[mid] > objetivo:
            r = mid - 1
        else:
            return mid
    return l

nums_input = input("Ingresa una lista de números recuerde separar con comas : ")
nums = [int(num) for num in nums_input.split(",")]

objetivo = int(input("Ingresa el objetivo: "))

resultado = encontrarnum(nums, objetivo)
print(resultado)

#hecho por freiler aleiro ortega estupiñan cc: 1010075774