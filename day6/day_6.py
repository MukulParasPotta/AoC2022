with open('input.txt') as input:
    message = input.readline().strip()
    size = len(message)
    for offset in [4, 14]:
        for idx in range(size-offset):
            if len(set(message[idx:idx+offset])) == offset:
                print(idx+offset)
                break
    