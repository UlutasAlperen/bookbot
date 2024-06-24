def main():
    path ="books/frankenstein.txt"
    print(create_dict(get_the_text(path)))


def get_the_text(path):
    with open(path) as f:
        return f.read()

def create_dict(text):
    text = list(str(text).lower()) 
    my_dict ={}
    my_set = set(text)
    for i in my_set:
        my_dict[i]=text.count(i)
    return my_dict

main()
