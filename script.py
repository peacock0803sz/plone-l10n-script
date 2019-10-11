import csv

POFILE = 'plone.po'


def main():
    with open('empty.tsv', newline='') as tsv:
        reader = csv.reader(tsv, delimiter='\t')
        # comment = []
        msgid = []
        msgstr = []
        translated = {}
        for row in reader:
            # comment.append(row[0])
            msgid.append(row[2])
            msgstr.append(row[5])
        del(msgid[:1])
        del(msgstr[:1])
        # for i in range(len(msgid)):
        #     translated[msgid[i]] = msgstr[i]
    meta = 0
    escape_index = []
    msg_index = []
    with open(POFILE, mode='r') as f:
        line = f.readlines()
        for i in range(len(line)):
            for j in range(len(msgid)):
                if line[i].startswith(f'msgid "{msgid[j]}'):
                    msg_index.append(i + 1)
                # if line[i].startswith('#:'):
                #     escape_index.append(i)
        if line[i].startswith('#:'):
            meta += 1
        for i in range(len(msgstr)):
            del(line[msg_index[i]])
            line.insert(msg_index[i] - meta, f'msgstr "{msgstr[i]}"\n')
    # print('\n'.join(line))
    with open(POFILE, mode='w') as f:
        for i in line:
            f.write(i)
    # po = polib.pofile(POFILE)
    # yet = po.untranslated_entries()
    # ind = []
    # ans = 0
    # for i in range(len(yet)):
    #     yet[i].msgstr = msgstr[i]
    # po.save()


if __name__ == '__main__':
    main()
