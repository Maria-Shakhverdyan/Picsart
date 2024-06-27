st = "find the letter z"
index_of_z = None

for index, char in enumerate(st):
    if char == 'z':
        print(index)
        index_of_z = index
        break
    
if index_of_z == None:
    print("character not found")