from typing import Dict, List


def read_file() -> List[str]:
    with open("./sample.txt", "r") as f:
        return [line.strip() for line in f]


def get_anagrams() -> Dict[int, List[str]]:
    words = read_file()
    results: Dict[tuple, List[str]] = {}

    for word in words:
        key_word = tuple(sorted(word))
        results.setdefault(key_word, list()).append(word)

    return results


if __name__ == "__main__":
    anagrams = get_anagrams()
    for list_value in anagrams.values():
        print(' '.join(list_value))
