import csv

POFILE = 'plone.po'


def main():
    with open('empty.tsv', newline='') as tsv:
        reader = csv.reader(tsv, delimiter='\t')
        msgid = []
        msgstr = []
        for row in reader:
            msgid.append(row[2])
            msgstr.append(row[5])
        del(msgid[:1])
        del(msgstr[:1])

    with open(POFILE, mode='r') as f:
        meta = 0
        msg_index = []
        line = f.readlines()
        for i in range(len(line)):
            for j in range(len(msgid)):
                if line[i].startswith(f'msgid "{msgid[j]}'):
                    msg_index.append(i + 1)
        if line[i].startswith('#:'):
            meta += 1
        for i in range(len(msgstr)):
            del(line[msg_index[i]])
            line.insert(msg_index[i] - meta, f'msgstr "{msgstr[i]}"\n')
    with open(POFILE, mode='w') as f:
        for i in line:
            f.write(i)


if __name__ == '__main__':
    main()
