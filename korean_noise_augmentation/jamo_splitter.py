_cho = ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
_jung = ["ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ", "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ"]
_jong = [" ", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ", "ㅁ", "ㅂ", "ㅄ", "ㅅ", "ㅆ",
         "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]

_double_jung = {"ㅘ": ["ㅗ", "ㅏ"], "ㅙ": ["ㅗ", "ㅐ"], "ㅚ": ["ㅗ", "ㅣ"], "ㅝ": ["ㅜ", "ㅓ"],
                "ㅞ": ["ㅜ", "ㅔ"], "ㅟ": ["ㅜ", "ㅣ"], "ㅢ": ["ㅡ", "ㅣ"]}
_double_jong = {"ㄳ": ["ㄱ", "ㅅ"], "ㄵ": ["ㄴ", "ㅈ"], "ㄶ": ["ㄴ", "ㅎ"], "ㄺ": ["ㄹ", "ㄱ"],
                "ㄻ": ["ㄹ", "ㅁ"], "ㄼ": ["ㄹ", "ㅂ"], "ㄽ": ["ㄹ", "ㅅ"], "ㄾ": ["ㄹ", "ㅌ"],
                "ㅀ": ["ㄹ", "ㅎ"], "ㅄ": ["ㅂ", "ㅅ"]}
inverted_double_jung = {"".join(value): key for key, value in
                        {"ㅘ": ["ㅗ", "ㅏ"], "ㅙ": ["ㅗ", "ㅐ"], "ㅚ": ["ㅗ", "ㅣ"], "ㅝ": ["ㅜ", "ㅓ"],
                         "ㅞ": ["ㅜ", "ㅔ"], "ㅟ": ["ㅜ", "ㅣ"], "ㅢ": ["ㅡ", "ㅣ"]}.items()}

inverted_double_jong = {"".join(value): key for key, value in
                        {"ㄳ": ["ㄱ", "ㅅ"], "ㄵ": ["ㄴ", "ㅈ"], "ㄶ": ["ㄴ", "ㅎ"], "ㄺ": ["ㄹ", "ㄱ"],
                         "ㄻ": ["ㄹ", "ㅁ"], "ㄼ": ["ㄹ", "ㅂ"], "ㄽ": ["ㄹ", "ㅅ"], "ㄾ": ["ㄹ", "ㅌ"],
                         "ㅀ": ["ㄹ", "ㅎ"], "ㅄ": ["ㅂ", "ㅅ"]}.items()}
def split(char, use_double_jung: bool=False, use_double_jong: bool=False):
    if char == " ": []

    c_number = ord(char) - ord("가")
    if c_number < 0 : return []

    len_jung, len_jong = len(_jung), len(_jong)
    jong_num = c_number % len_jong
    jung_num = (c_number // len_jong) % len_jung
    cho_num = (c_number // len_jong) // len_jung

    cho = _cho[cho_num]
    jung = _jung[jung_num]
    jong = _jong[jong_num]

    if use_double_jung:
        jung = _double_jung[jung] if jung in _double_jung else jung

    if use_double_jong:
        jong = _double_jong[jong] if jong in _double_jong else jong

    return [cho, jung, jong]


def join(jamo: list):
    if not jamo: return " "

    cho, jung, jong = jamo

    cho_num = _cho.index(cho)
    len_jung, len_jong = len(_jung), len(_jong)

    if isinstance(jung, list):
        if "".join(jung) in inverted_double_jung:
            jung = inverted_double_jung["".join(jung)]
        else:
            first_jung_num = _jung.index(jung[0])
            first_c = cho_num * len_jung * len_jong + first_jung_num * len_jong
            if isinstance(jong, list):
                if "".join(jong) in inverted_double_jong:
                    jong = inverted_double_jong["".join(jong)]
                else: jong = "".join(jong)

            return f"{chr(first_c + ord('가'))}{jung[1]}{jong}".replace(" ", "")

    if isinstance(jong, list):
        if "".join(jong) in inverted_double_jong:
            jong = inverted_double_jong["".join(jong)]
        else:
            first_jung_num = _jung.index(jung)
            first_c = cho_num * len_jung * len_jong + first_jung_num * len_jong + _jong.index(jong[0])
            return f"{chr(first_c + ord('가'))}{jong[1]}".replace(" ", "")
    jung_num = _jung.index(jung)
    jong_num = _jong.index(jong)

    c_number = cho_num * len_jung * len_jong + jung_num * len_jong + jong_num
    c = chr(c_number + ord("가"))

    return c