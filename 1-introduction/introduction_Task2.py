numbers = [1, 2, '0', '300', -2.5, 'Dog', True, 0o1256, None]
for n, i in enumerate(numbers):
    try:
        numbers[n] = int(i)
    except TypeError:
        numbers.pop(n)
    except ValueError:
        numbers.pop(n)

print(f'Maximum value is: {max(numbers)}')
print(f'Minimum value is: {min(numbers)}')
