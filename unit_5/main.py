def is_valid_input(s) -> bool:
    err = err_check(s)
    if err == "E1" or err == "E2" or err == "E3":
        return False
    else:
        return True


def err_check(s) -> str:
    len_s = len(s)

    if(s.isalpha() and len_s == 1):
        return s.lower()
    elif(s.isalpha()):
        return "E1"
    elif(len_s == 1):
        return "E2"
    else:    
        return "E3"

def main():
    s = input("Guess a letter: ")
    print(is_valid_input(s))
    

if __name__ == '__main__':
    main()
