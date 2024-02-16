import random
from tqdm import trange
from .hangul_graph import HangulGraph
from .jamo_splitter import split, join

graph = HangulGraph()
def augment(text, prob: float=.1, sample: int=1, depth: int=1, use_double_jung: bool=False, use_double_jong: bool=False):

    outputs = []

    if not (0 <= prob <= 1):
        raise ValueError(f'prob must be between {0} and {1}')

    for _ in trange(sample):
        texts = list(text)
        new_text = ""
        for char in texts:
            split_chars = split(char, use_double_jung, use_double_jong)
            new_chars = []
            for c in split_chars:
                if isinstance(c, list):
                    temp = []
                    for _c in c:
                        if random.uniform(0, 1) < prob:
                            temp.append(random.choice(graph.search(_c, depth)))
                        else:
                            temp.append(_c)
                    new_chars.append(temp)
                else:
                    if random.uniform(0, 1) < prob:
                        new_chars.append(random.choice(graph.search(c, depth)))
                    else:
                        new_chars.append(random.choice(c))
            new_text += join(new_chars)

        outputs.append(new_text)

    return outputs