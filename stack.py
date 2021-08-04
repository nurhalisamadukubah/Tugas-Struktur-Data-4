class ArrayStack:
    def __init__(self):
        self._data = []

    def len(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        return self._data.pop()

def reverse_file(filename):
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n'))
    original.close()

    output = open(filename, 'w')
    while not S.is_empty():
        output.write(S.pop() + '\n')
    output.close()

    file = open(filename, 'r')
    baris = file.readlines()
    for i in baris:
        print(i.rstrip())

def is_matched(expr):
    lefty = '({['
    righty = ')}]' 
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c) 
        elif c in righty:
            if S.is_empty():
                return False 
            if righty.index(c) != lefty.index(S.pop()):
                return False 
    return S.is_empty()

active = True

while active :
    print('\nMenu : \n 1. Reverse File \n 2. Matching Delimiters \n 3. Stop Running Program')
    option = int(input('Masukkan Pilihan Anda = '))
    if option == 1 :
        file_name = input('Masukkan Nama File = ')
        print(file_name + '.txt', '\n')
        reverse_file(file_name + ".txt")
    elif option == 2 :
        expr = input('Masukkan Expression (righty/lefty) = ')
        print('\n', is_matched(expr))
    else :
        break
