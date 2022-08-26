def _calculate_A(bytes):
    a = 1
    for b in bytes:
        a += int(b)
    return a % 65521

def _calculate_B(bytes):
    b = 0
    for i in range(len(bytes)):
        b += _calculate_A(bytes[:i+1])
    return b % 65521

def adler32_hash(bytes):
    a = _calculate_A(bytes)
    b = _calculate_B(bytes)
    return 2**16 * b + a