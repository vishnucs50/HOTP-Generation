from Crypto.Hash import HMAC, SHA1
import sys

secret = b'febd2036b04690e307342884d14ba164'            # Bytes HMAC key value

counter = int(sys.argv[1])                              # takes command line input from the user.

key = HMAC.new(secret, digestmod=SHA1)
hash_to_byte = str.encode(str(counter))
hash_value = key.update(hash_to_byte)

hash_value = hash_value.hexdigest()


offsetvalue = hash_value[39]
offset = int(offsetvalue, 16)

offset = offset * 2                                     # Offset position. Hex representation

snumvalue = hash_value[offset: (offset + 8)]                  # truncation of the hash message

snumbin = bin(int(snumvalue, 16))[2:].zfill(32)         # Transform the hexadecimal to binary
truncateval = snumbin[1:]                               # Returns the last 31 bits value
truncatehex = hex(int(truncateval, 2))                  # Hex conversion
digitvalue = int(truncateval, 2)
otp_value = digitvalue % (10 ** 6)                      # Compute OTP value


key_value = sys.argv[-1]                        # Capture the keyword "verbose" or otherwise.

if (key_value == "verbose"):

    print("The value of the hash:", hash_value)
    print("Offset: ", offset)
    print("DT : ", truncatehex)
    Print("Otp_value: ", otp_value)

else:
    print("The OTP generated is:",otp_value)
