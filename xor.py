from pwn import xor

data = "label"
result = xor(data, 13)
print(result)

