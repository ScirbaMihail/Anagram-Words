from typing import Dict, List


def read_file() -> List[str]:
    results = list()

    with open("./sample.txt", "r") as f:
        for line in f:
            results.append(line.strip())

        return results


def get_anagrams() -> Dict[int, List[str]]:
    words = read_file()
    results = dict(list())
    for word in words:
        tuple_word = tuple(sorted(list(word)))
        results[tuple_word] = [word] if tuple_word not in results.keys() else results[tuple_word] + [word]

    return results


if __name__ == "__main__":
    anagrams = get_anagrams()
    for key, value in anagrams.items():
        for word in value:
            print(word, end=' ')
        print()
