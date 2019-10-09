import csv

import polib


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
    po.save('empty.po')


if __name__ == '__main__':
    main()
