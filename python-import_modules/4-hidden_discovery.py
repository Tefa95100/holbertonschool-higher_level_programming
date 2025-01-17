#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    list_name = sorted(dir(hidden_4))
    for word in list_name:
        if word[0] == "_":
            continue
        else:
            print(word)
