def letters(palabra1:str, palabra2:str):
    encontradas2 = []
    encontradas = []
    deseconcontradas = []
    for i in palabra1:
        if i in palabra2:
            encontradas.append(i)
        else: 
            deseconcontradas.append(i)
    for i in palabra2:
        if i in palabra1:
            encontradas2.append(i)
        else:
            deseconcontradas.append(i)
    
    print(f"se repiten: {','.join(encontradas)}")
    print(f"no se repiten: {','.join(deseconcontradas)}")
            
palabra1 = input("primera palabra: ")
palabra2 = input("segunda palabra: ")
    
letters(palabra1, palabra2)


