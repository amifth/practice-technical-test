def fizzbuzz(n):

    if n % 3 == 0 and n % 5 == 0:
        return 'Snip Snap'
    elif n % 3 == 0:
        return 'Snip'
    elif n % 5 == 0:
        return 'Snap'
    else:
        return str(n)

print("\n".join(fizzbuzz(n) for n in range(1, 100)))