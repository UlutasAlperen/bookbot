def main():
    path ="books/frankenstein.txt"
    print("--- Begin report of books/frankenstein.txt ---")
    var = count_character(get_the_text(path))
    var_2 = create_report(var)
    for i in var_2:
        print(f"The {i["name"]} character was found {i["num"]} times")
    print("--- End report ---")
    print("Thanks for reading")





def get_the_text(path):
    with open(path) as f:
        return f.read()


def count_character(text):
    text = list(str(text).lower()) 
    my_dict ={}
    my_set = set(text)
    for i in my_set:
        my_dict[i]=text.count(i)

    return my_dict



def sort_on(var:dict):
    return var["num"]



def create_report(var:dict):
    my_list  = []
    for i in var.keys():
        if i >= 'a' and i <='z':
            temp = {
                "name": i,
                "num": var[i]
            }
            my_list.append(temp)
    my_list.sort(reverse=True,key=sort_on)
    return my_list


main()
