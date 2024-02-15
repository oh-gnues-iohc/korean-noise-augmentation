# korean-noise-augmentation
한국어 입력을 자음과 모음으로 분리한 후, 오타가 발생하기 쉬운 키보드 인접 자모로 대체하여 음성 인식 시스템의 오류 대응 능력을 향상시키는 레포지토리

## Getting Started

## Augment

```python
from korean_noise_augmentation import augment

augment("안녕하세요 저는 최승호에요", prob=.1, sample=3, use_double_jung=True)
# ['간녕하세요 저는 최승호에요', '앋녕하세요 조는 최승호에요', '언녕하세요 저는 쵸ㅏ 승호에요']
```

```python
def augment(text, prob: float=.1, sample: int=1, depth: int=1, use_double_jung: bool=False, use_double_jong: bool=False):
    
# text: input text
# prob: augmentation probability
# sample: num of returns
# depth: search depth
```


## Details

### Split

입력받은 문자를 초정, 중성, 종성으로 자릅니다.

```python
from korean_noise_augmentation import split

split("읪")
# ['ㅇ', 'ㅢ', 'ㅄ']

split("읚", use_double_jung=True)
# ['ㅇ', ['ㅡ', 'ㅣ'], 'ㅄ']

split("읚", use_double_jung=True, use_double_jong=True)
# ['ㅇ', ['ㅡ', 'ㅣ'], ['ㅂ', 'ㅅ']]
```

### Join

잘린 초정, 중성, 종성을 다시 문자로 합칩니다.
```python
from korean_noise_augmentation import join

join(['ㅇ', 'ㅢ', 'ㅄ'])
# 읪

join(['ㅇ', ['ㅡ', 'ㅣ'], 'ㅄ'])
# 읪

join(['ㅇ', ['ㅡ', 'ㅣ'], ['ㅂ', 'ㅅ']])
# 읪
```

### Search

자음은 자음끼리, 모음은 모음끼리 키보드 자판 기준 오타 날 수 있는 범위(depth)의 다른 자모를 찾아줍니다.

```python
from korean_noise_augmentation import HangulGraph

graph = HangulGraph()

graph.search("ㄹ", 1)
# ['ㅇ', 'ㄱ', 'ㅎ', 'ㅊ', 'ㅍ', 'ㅅ']

graph.search("ㄹ", 3)
# ['ㅇ', 'ㅈ', 'ㄱ', 'ㅋ', 'ㅎ', 'ㅊ', 'ㅍ', 'ㅁ', 'ㄴ', 'ㅅ', 'ㄷ', 'ㅌ']

graph.search("ㅗ", 2)
# ['ㅕ', 'ㅜ', 'ㅏ', 'ㅓ', 'ㅑ', 'ㅠ', 'ㅡ', 'ㅛ']
```
