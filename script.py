import csv

import polib

POFILE = 'empty.po'

def main():
    with open('empty.tsv', newline='') as tsv:
        reader = csv.reader(tsv, delimiter='\t')
        comment = []
        id = []
        translated = []
        for row in reader:
            comment.append(row[0])
            id.append(row[2])
            translated.append(row[5])

    po = polib.POFile()
    length = len(id)
    for i in range(1, length):
        po.append(polib.POEntry(msgid=id[i], msgstr=translated[i]))
    po.save(POFILE)

    with open(POFILE, mode='r') as f:
        read = f.readlines()
    for i in range(1, length, 3):
        read.insert(i, f'#: {comment[i]}')


if __name__ == '__main__':
    main()
