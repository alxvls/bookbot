import sys
from pathlib import Path
from stats import count_words, count_chars, sort_char_stats


def get_book_text(path: Path) -> str:
    with open(path, "r") as f:
        t = f.read()
    return t


def print_report(path: Path, wc: int, ch_st: list[dict[str, int]]) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {str(path)}...")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    for d in ch_st:
        print(f"{d['char']}: {d['num']}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    p = Path(sys.argv[1])

    book_text = get_book_text(p)
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document")

    char_stat = count_chars(book_text)
    st_ch_st = sort_char_stats(char_stat)

    print_report(p, num_words, st_ch_st)


if __name__ == "__main__":
    main()