# -- coding: utf-8 --






# lettersToNum = {ord():1  , 'b':2}

# def gimatriya(str):
#     for letter in str:
#         if not letter in lettersToNum:
#             return 'use hebrew letters only'
#     return 'good'

# print(lettersToNum['א'])
# print('d' in lettersToNum)

# print(ord('א'))  # Aleph
# print(ord('ב'))  # Bet
# print(ord('ג'))  # Gimel
# print(ord('ד'))  # Dalet
# print(ord('ה'))  # He
# print(ord('ו'))  # Vav
# print(ord('ז'))  # Zayin
# print(ord('ח'))  # Het
# print(ord('ט'))  # Tet
# print(ord('י'))  # Yod
# print(ord('כ'))  # Kaf
# print(ord('ל'))  # Lamed
# print(ord('מ'))  # Mem
# print(ord('נ'))  # Nun
# print(ord('ס'))  # Samekh
# print(ord('ע'))  # Ayin
# print(ord('פ'))  # Pe
# print(ord('צ'))  # Tsadi
# print(ord('ק'))  # Qof
# print(ord('ר'))  # Resh
# print(ord('ש'))  # Shin
# print(ord('ת'))  # Tav
# print(ord(' '))  # Space


aleph = 1488
tav = 1514
gimatriya_dict = {
    1488: 1,    # Aleph (א)
    1489: 2,    # Bet (ב)
    1490: 3,    # Gimel (ג)
    1491: 4,    # Dalet (ד)
    1492: 5,    # He (ה)
    1493: 6,    # Vav (ו)
    1494: 7,    # Zayin (ז)
    1495: 8,    # Het (ח)
    1496: 9,    # Tet (ט)
    1497: 10,   # Yod (י)
    1499: 20,   # Kaf (כ)
    1500: 30,   # Lamed (ל)
    1502: 40,   # Mem (מ)
    1504: 50,   # Nun (נ)
    1505: 60,   # Samekh (ס)
    1506: 70,   # Ayin (ע)
    1508: 80,   # Pe (פ)
    1510: 90,   # Tsadi (צ)
    1511: 100,  # Qof (ק)
    1512: 200,  # Resh (ר)
    1513: 300,  # Shin (ש)
    1514: 400,   # Tav (ת)

    1498 :20, #Kaf Sofith (ך)
    1501 :40, #Mem Sofith (ם)
    1503 :50, #Nun Sofith (ן)
    1507 :80, #Pe Sofith (ף)
    1509 :90, #Tsadi Sofith (ץ)

    # 32: 0,    # ' ' (space)
    # 44: 0,    # ',' (comma)
    # 46: 0,    # '.' (period)
    # 58: 0,    # ':' (colon)
    # 10: 0,    # '\n' (newline)
    # 39: 0,    # "'" (single quote)
    # 34: 0,    # '"' (double quote)
    # 48: 0,    # '0'
    # 49: 0,    # '1'
    # 50: 0,    # '2'
    # 51: 0,    # '3'
    # 52: 0,    # '4'
    # 53: 0,    # '5'
    # 54: 0,    # '6'
    # 55: 0,    # '7'
    # 56: 0,    # '8'
    # 57: 0,    # '9'
    # 33: 0,    # '!' 
    # 63: 0,    # '?' 
    # 40: 0,    # '(' 
    # 41: 0,    # ')' 
    # 45: 0,    # '-' 
    # 95: 0,    # '_'
    # 43: 0,    # '+' 
    # 61: 0,    # '=' 
    # 47: 0,    # '/' 
    # 92: 0,    # '\\' (backslash)
    # 42: 0,    # '*' 
    # 38: 0,    # '&' 
    # 37: 0,    # '%' 
    # 35: 0,    # '#' 
    # 64: 0,    # '@' 
    # 94: 0,    # '^'
    # 124: 0,   # '|'
    # 96: 0,    # '`'
    # 126: 0,   # '~'
    # 1456: 0,   # Sheva (ְ)
    # 1457: 0,   # Hataf Segol (ֱ)
    # 1458: 0,   # Hataf Patah (ֲ)
    # 1459: 0,   # Hataf Qamats (ֳ)
    # 1460: 0,   # Hiriq (ִ)
    # 1461: 0,   # Tzere (ֵ)
    # 1462: 0,   # Segol (ֶ)
    # 1463: 0,   # Patah (ַ)
    # 1464: 0,   # Qamats (ָ)
    # 1465: 0,   # Holam (ֹ)
    # 1467: 0,   # Qubuts (ֻ)
    # 1468: 0,   # Dagesh or Mappiq (ּ)
    # 1469: 0,   # Meteg (ֽ)
    # 1470: 0,   # Rafe (ֿ)
    # 1471: 0,   # Shin Dot (ׁ)
    # 1472: 0,   # Sin Dot (ׂ)
    # 1473: 0,   # Paseq (׃)
    # 1474: 0,   # Upper Dot (ׄ)
}

# def gimatiya(theText):
#     sum = 0
#     for letter in theText:
#         ASCIIofLetter = ord(letter)
#         if not ASCIIofLetter in gimatriya_dict:
#             return "only hebrew letters please", letter
#         gimatriyaOfLetter = gimatriya_dict[ASCIIofLetter]
#         sum += gimatriyaOfLetter
#     return sum

def gimatiya(the_text):
    total_value = 0
    for letter in the_text:
        letter_ASCII = ord(letter)
        if letter_ASCII in gimatriya_dict:
            letter_value = gimatriya_dict[letter_ASCII]
            total_value += letter_value
    return total_value
