def rolling_hash(bytes, constant=2**5):
    hash_val = 0
    n = len(bytes)
    for index, b in enumerate(bytes):
        i = index + 1
        hash_val += int(b) * constant**(n-i)

    return hash_val % 2**32