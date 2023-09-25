def linearSearch(list_, item):
    index, found = -1, False    
    for i in range(len(list_)):
        if list_[ i] == item:
            found = True
            index = i
            break
    return index 
   
test = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(linearSearch(test, 3))
print(linearSearch(test, 1))
print(linearSearch(test, 17))
print(linearSearch(test, 0))
