import base64

#Declare byte string here
byte_string = b"Hello"
encoded_string = base64.b64encode(byte_string)
print(encode_b64_string(byte_string))