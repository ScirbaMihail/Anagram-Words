from collections import defaultdict, Counter
from typing import Dict, List


def read_file() -> List[str]:
    with open("./sample.txt", "r") as f:
        return [line.strip() for line in f]


def get_anagrams(words: List[str]) -> Dict[tuple, List[str]]:
    results = defaultdict(list)

    for word in words:
        key_word = tuple(sorted(Counter(word).items()))
        results[key_word].append(word)

    return results


if __name__ == "__main__":
    anagrams = get_anagrams(read_file())
    for list_value in anagrams.values():
        print(' '.join(list_value))
