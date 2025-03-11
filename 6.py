str1 = "PythonIsFun"
substring = "Fun"
exists = False
for i in range(len(str1) - len(substring) + 1):
    if str1[i:i + len(substring)] == substring:
        exists = True
        break
print(exists) 