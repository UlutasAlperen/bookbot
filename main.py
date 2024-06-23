def main():
    path ="books/frankenstein.txt"
    print(get_the_text(path))


def get_the_text(path):
    with open(path) as f:
        return f.read()


main()
