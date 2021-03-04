import random
import string

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



def Chi2Fig(cha, complex=False, new_dict = False, replace_dict=dict()):

    dict_complex = {'空': 0, '壹': 1, '貳': 2, '參': 3, '參': 3, '肆': 4, '伍': 5, '陸': 6, '柒': 7, '捌': 8, '玖': 9, '拾': 10, '百': 100, '千': 1000, '萬': 10000}
    dict_simple = {'空':0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '十': 10, '百': 100, '千': 1000, '萬': 10000}
    dict_all = {**dict_complex, **dict_simple}

    if new_dict == True:
        dict_here = replace_dict
    else:
        if complex == False:
            dict_here = dict_all
        else: # complex == True:
            dict_here = dict_complex

    dict_unit = dict((k, v) for k, v in dict_here.items() if v%10 != 0 )
    dict_deci = dict((k, v) for k, v in dict_here.items() if v%10 == 0 and v != 0) # '空'은 제외.

    if len(cha) == 1:
        result = dict_here[cha]
    else:
        # (1) '空' 처리.
        cha = cha.replace('空', '')
        # (2)
        for deci in dict_deci.keys():
            cha = sliceitby(cha, deci, side='end')

        deci_sum = []
        for ch in cha: # now cha is a list
            if ch[-1] in dict_deci.keys():
                if len(ch) == 1:
                    p = dict_deci[ch[-1]]
                elif len(ch) == 2:
                    p = dict_unit[ch[-2]]*dict_deci[ch[-1]]                    
            else:
                p = dict_unit[ch[-1]]
            deci_sum.append(p)

        result = sum(deci_sum)


    return result
