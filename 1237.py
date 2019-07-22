from difflib import SequenceMatcher
while True:
    try:
        palavra1 = input()
        palavra2 = input()
        sequencia = SequenceMatcher(None, palavra1, palavra2).find_longest_match(0, len(palavra1), 0, len(palavra2))
        print(sequencia.size)
    except EOFError:
        break