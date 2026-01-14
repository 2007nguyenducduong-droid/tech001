import random
code_3 = ""
for i in range(3):
    code_3 += str(random.randint(0, 9))
code_4 = ""
for i in range(4):
    code_4 += str(random.randint(1, 6))

print("3-digit lock code:", code_3)
print("4-digit lock code:", code_4)