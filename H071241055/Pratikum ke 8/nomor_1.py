import re

def validate_string(s):
    if len(s) != 45:
        return False
    
    pattern = r'^[a-zA-Z02468]{40}[13579\s]{5}$'
    if re.match(pattern, s):
        return True
    else:
        return False


input1 = "2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57"
input2 = "x4202v2A22A8a6aaaaaa2G2222m222qwertyYuIo13957"

print(validate_string(input1))  
print(validate_string(input2))  
