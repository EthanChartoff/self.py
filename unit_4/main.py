def main():
    s = input("Guess a letter: ")
    if(s.isalpha() and len(s) == 1):
        print(s)
    elif(s.isalpha()):
        print("E1")
    elif(len(s) == 1):
        print("E2")
    else:    
        print("E3")

if __name__ == '__main__':
    main()
