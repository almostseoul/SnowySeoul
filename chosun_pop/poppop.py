"""
sliceitby ... split strings while not omiting the split character.
Chi2Fig ... transfer Chinese fig into decimal fig.
ganji ... get ganji(Sexagenary cycle) of a year.
ganji_gap,
years_of_ganji

"""

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


def ganji(year, kr=False):
    """
    IF kr == True, the result will be in Korean Character. Otherwise, in Chinenese. False is the default.
    """
    list_ganji = ['甲子','乙丑','丙寅','丁卯','戊辰','己巳','庚午','辛未','壬申','癸酉','甲戌','乙亥','丙子','丁丑','戊寅','己卯','庚辰','辛巳','壬午','癸未','甲申','乙酉','丙戌','丁亥','戊子','己丑','庚寅','辛卯','壬辰','癸巳','甲午','乙未','丙申','丁酉','戊戌','己亥','庚子','辛丑','壬寅','癸卯','甲辰','乙巳','丙午','丁未','戊申','己酉','庚戌','辛亥','壬子','癸丑','甲寅','乙卯','丙辰','丁巳','戊午','己未','庚申','辛酉','壬戌','癸亥']
    list_ganji_kr = ['갑자','을축','병인','정묘','무진','기사','경오','신미','임신','계유','갑술','을해','병자','정축','무인','기묘','경진','신사','임오','계미','갑신','을유','병술','정해','무자','기축','경인','신묘','임진','계사','갑오','을미','병신','정유','무술','기해','경자','신축','임인','계묘','갑진','을사','병오','정미','무신','기유','경술','신해','임자','계축','갑인','을묘','병진','정사','무오','기미','경신','신유','임술','계해']
    resid = (year-4)%60 #4년=甲子년 기준
    if year > 0:
        gj = list_ganji[resid]
        gj_kr = list_ganji_kr[resid]
        if kr == True:
            return(gj_kr)
        else:
            return(gj)
    elif year < 0:
        gj = list_ganji[resid+1]
        gj_kr = list_ganji_kr[resid+1]
        if kr == True:
            return(gj_kr)
        else:
            return(gj)
    elif year == 0:
        return("year 0 doens't exist")
    
  
def ganji_gap(a, b): # a가 b보다 최신 년도 간지라고 가정
    """
    두 간지의 년차 구하기
    """
    list_ganji_kor = ['갑자','을축','병인','정묘','무진','기사','경오','신미','임신','계유','갑술','을해','병자','정축','무인','기묘','경진','신사','임오','계미','갑신','을유','병술','정해','무자','기축','경인','신묘','임진','계사','갑오','을미','병신','정유','무술','기해','경자','신축','임인','계묘','갑진','을사','병오','정미','무신','기유','경술','신해','임자','계축','갑인','을묘','병진','정사','무오','기미','경신','신유','임술','계해']
    ar = list_ganji_kr.index(a)
    br = list_ganji_kr.index(b)
    if ar>br:
        rs = ar-br
    elif ar<br:
        rs = 60-(br-ar)
    elif ar==br:
        rs = 0
    print("year_gap: ", rs, "or", rs+60, "...")
    print("Korean_age: ", rs+1, "or", rs+61, "...")
    
    
    
def years_of_ganji(ganji):
    """
    어떤 간지에 해당하는 년도의 리스트업 (16~21세기 내에서)
    """
    list_ganji_kor = ['갑자','을축','병인','정묘','무진','기사','경오','신미','임신','계유','갑술','을해','병자','정축','무인','기묘','경진','신사','임오','계미','갑신','을유','병술','정해','무자','기축','경인','신묘','임진','계사','갑오','을미','병신','정유','무술','기해','경자','신축','임인','계묘','갑진','을사','병오','정미','무신','기유','경술','신해','임자','계축','갑인','을묘','병진','정사','무오','기미','경신','신유','임술','계해']
    a = list_ganji_kor.index(ganji)
    b = a+1504
    list_c = []
    for i in range(10):
        c = b + 60*i
        list_c.append(c)
    return(list_c)
