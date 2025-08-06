def decode_hex_string(hex_string):
    """
    Decodes a hex-encoded string to its ASCII representation.

    Args:
        hex_string (str): The hex string to decode.

    Returns:
        str: The decoded ASCII string.
    """
    try:
        bytes_object = bytes.fromhex(hex_string)
        return bytes_object.decode('utf-8')
    except ValueError:
        return "Invalid hex string"

#Declare hex string here
hex_input = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
print(decode_hex_string(hex_input))