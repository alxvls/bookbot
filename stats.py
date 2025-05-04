def count_words(text: str) -> int:
    num_words = len(text.split())
    return num_words


def count_chars(text: str) -> dict[str, int]:
    res = dict()
    for ch in text:
        k = ch.lower()
        if k in res:
            res[k] += 1
        else:
            res[k] = 1
    return res


def sort_char_stats(st: dict[str, int]) -> list[dict[str, int]]:
    res = list()

    for k, v in st.items():
        if not k.isalpha():
            continue

        res.append(
            {"char": k, "num": v}
        )
    
    res.sort(key=lambda x: x["num"], reverse=True)

    return res