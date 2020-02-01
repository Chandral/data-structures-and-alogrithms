def get_val(num, limit):
    if num > limit:
        return num
    return get_val(num + 1, limit)


print(get_val(1, 50))
