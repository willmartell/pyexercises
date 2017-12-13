def facto(n):
    assert n > -1, "facto requires positive value as param"
    if n==0:
        return 1
    return n * facto(n -1)

print facto(8)
