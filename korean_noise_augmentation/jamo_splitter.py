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
    if c_number < 0 : return [char]

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


def join(jamo: list) -> str:
    if not jamo:
        return " "

    if len(jamo) < 2:
        return "".join(jamo)

    cho, jung, jong = jamo
    cho_idx = _cho.index(cho)

    c = ""
    second_jung = ""
    second_jong = ""


    if isinstance(jung, list):
        jung, second_jung = _get_single_jung_from_double(jung)

        if second_jung:
            c = _get_character(cho_idx, jung, " ") + second_jung

    if isinstance(jong, list):
        jong, second_jong = _get_single_jong_and_second_jong(jong)

        if c:
            c = c + jong

    if not c:
        c = _get_character(cho_idx, jung, jong)

    return c + second_jong.replace(" ", "")

def _get_single_jung_from_double(double_jung: list) -> str:
    single_jung = inverted_double_jung["".join(double_jung)] if "".join(double_jung) in inverted_double_jung else double_jung[0]
    second_jung = "" if single_jung in _double_jung else double_jung[1]
    return single_jung, second_jung

def _get_single_jong_and_second_jong(double_jong: list) -> tuple:
    single_jong = inverted_double_jong["".join(double_jong)] if "".join(double_jong) in inverted_double_jong else double_jong[0]
    second_jong = "" if single_jong in _double_jong else double_jong[1]
    return single_jong, second_jong

def _get_character(cho_idx: int, jung: str, jong: str) -> str:
    len_jung, len_jong = len(_jung), len(_jong)

    jung_idx = _jung.index(jung)
    jong_idx = _jong.index(jong)
    c_number = cho_idx * len_jung * len_jong + jung_idx * len_jong + jong_idx
    return chr(c_number + ord("가"))
