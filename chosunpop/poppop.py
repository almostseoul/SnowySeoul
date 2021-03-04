def sliceitby(cha_list, by, side='front'):
    """Slice a string or list of strings by 2nd argument(by).
    The result will be returned in list type.
    If side=='both', elements of list will be separated by the front and end of 2nd argument.
    If side=='end', they will be separated only by the end of it.
    If side == 'front', they will be separated only by the front of it. And this is default.
    """

    if type(cha_list) == str:
        cha_list = [cha_list]

    random_code = ""
    while random_code in "".join(cha_list):
        for _ in range(100):
            for _ in range(random.choice(range(1, 10))):
                random_code += random.choice(string.printable)

    result = []
    if side == 'front':
        merged_code = random_code + by
        for cha in cha_list:
            result.extend(merged_code.join(cha.split(by)).split(random_code))

    elif side == 'end':
        merged_code = by + random_code
        for cha in cha_list:
            result.extend(merged_code.join(cha.split(by)).split(random_code))

    elif side == 'both':
        merged_code = random_code + by + random_code
        for cha in cha_list:
            result.extend(merged_code.join(cha.split(by)).split(random_code))

    result = [r for r in result if r != ""]

    return result
