class HangulGraph:

    def __init__(self):
        self.graph = {
            "ㅂ": [], "ㅈ": [], "ㄷ": [], "ㄱ": [], "ㅅ": [], "ㅛ": [], "ㅕ": [], "ㅑ": [], "ㅐ": [],
            "ㅔ": [], "ㅁ": [], "ㄴ": [], "ㅇ": [], "ㄹ": [], "ㅎ": [], "ㅗ": [], "ㅓ": [], "ㅏ": [],
            "ㅣ": [], "ㅋ": [], "ㅌ": [], "ㅊ": [],"ㅍ": [], "ㅠ": [], "ㅜ": [], "ㅡ": [],
        }
        self.shift = {"ㅃ": "ㅂ", "ㅉ": "ㅈ", "ㄸ": "ㄷ", "ㄲ": "ㄱ", "ㅆ": "ㅅ", "ㅒ": "ㅐ", "ㅖ": "ㅔ"}
        self.inverted_shift = {value: key for key, value in self.shift.items()}

        edges = [("ㅈ", "ㅁ"), ("ㅁ", "ㄴ", "ㄷ"), ("ㄴ", "ㅇ", "ㄱ"), ("ㅇ", "ㄹ", "ㅅ"), ("ㄹ", "ㅎ"), ("ㅗ", "ㅕ"),
                 ("ㅗ", "ㅓ", "ㅑ"), ("ㅓ", "ㅏ", "ㅐ"), ("ㅏ", "ㅣ", "ㅔ"), ("ㅣ"), ("ㄴ", "ㅋ"), ("ㅋ", "ㅌ", "ㅇ"), ("ㅌ", "ㅊ", "ㄹ"),
                 ("ㅊ", "ㅍ", "ㅎ"), ("ㅍ"), ("ㅠ", "ㅜ", "ㅓ"), ("ㅜ", "ㅡ", "ㅏ"), ("ㅡ", "ㅣ"), (), ("ㅌ"), ("ㅊ"), ("ㅍ"), (),
                 ("ㅜ"), ("ㅡ"), ()]

        for key, edge in zip(self.graph.keys(), edges):
            for e in edge:
                self.add_edge(key, e)

    def add_edge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)

    def search(self, key, depth: int = 1):
        if key in self.shift:
            is_shift = True
            key = self.shift[key]
        else:
            is_shift = False

        if key not in self.graph: return key

        base = self.graph[key]
        outputs = []
        if depth != 1:
            for _key in base:
                outputs += self.search(_key, depth-1)
        outputs += base
        outputs = list(set(outputs))
        if key in outputs:
            outputs.remove(key)

        if is_shift:
            for i in range(len(outputs)):
                outputs[i] = self.inverted_shift[outputs[i]] if outputs[i] in self.inverted_shift else outputs[i]
            outputs.append(key)
        return outputs