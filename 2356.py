# -*- coding: utf-8 -*-

while True:
    try:
        d = input()
        s = input()
        print('Resistente') if s in d else print('Nao resistente')
    except EOFError:
        break