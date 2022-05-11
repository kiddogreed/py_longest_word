# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    txt = input("add phrases or sentence:")
    ntx = txt.split(" ")
    nlen = []
    nwor = []
    for n in ntx:
        nlen.append(len(n))
        nwor.append(n)

    longest = max(nlen)
    for l in nwor:
        if longest == len(l):
            print(f"longest word:{l}")
