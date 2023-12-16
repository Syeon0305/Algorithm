def main():
    l = input()
    output = len(l.split())
    #output = len(list(filter(None, l.split(' '))))
    print(output)

main()