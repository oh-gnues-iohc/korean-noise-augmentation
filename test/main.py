from korean_noise_augmentation import HangulGraph, split, join, augment


if __name__ == "__main__":
    g = HangulGraph()
    print(g.search("ㄹ", 1))

    print(g.search("ㄹ", 3))

    print(g.search("ㅗ", 2))

    print(split("얶", use_double_jung=True))
    print(join(['ㅇ', ['ㅡ', 'ㅣ'], ['ㅂ', 'ㅅ']]))

    print(augment("안녕하세요 저는 최승호에요", prob=.1, sample=3, use_double_jung=True))