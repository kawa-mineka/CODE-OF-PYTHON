edits = {#必要のない範囲のデータ　無くてもあっても変わらないので消しても〇
    2:[['〓','∈'],['∩','∧'],['∃','∠'],['∬','Å'],['¶','◯']],
    3:[[0,'0'],['9','A'],['Z','a'],['z',1]],
    4:[['ん',1]],
    5:[['ヶ',1]],
    #6:[['Ω','a'],['ω',1]],
    7:[['Я','а'],['я',1]],
    8:[['╂',1]],
    9:[[0,1]],
    10:[[0,1]],
    11:[[0,1]],
    12:[[0,1]],
    13:[['㎡','㊥']],
    14:[[0,1]],
    15:[[0,1]],
    47:[['腕',1]]
}

with open('./code_table.txt','r',encoding='utf-8') as f:#さきほど作成した「code_table.txt」を開いて文字列を取得します。
    s = f.read().replace('2面（第4水準漢字）','')#必要のない、「2面（第4水準漢字）」を取り除きます

    result_s = ""
    i = 1

    #コード表から文字だけを摘出します。
    for line in s.split('\n\n'):
        append_s = ""
        for l in line.split('\n')[1:]:
            append_s += ''.join(l.split('\t')[-16:])
        if i in edits:
            for r_0,r_1 in edits[i]:
                if type(r_0) == int:
                    r_0 *= len(append_s)
                else:
                    r_0 = append_s.find(r_0)+1
                if type(r_1) == int:
                    r_1 *= len(append_s)
                else:
                    r_1 = append_s.find(r_1)

                append_l = list(append_s)
                append_l[r_0:r_1] = " " * (r_1-r_0)

                append_s = ''.join(append_l)

        result_s += append_s.rstrip() + '\n'

        i += 1

    result_s = result_s[:result_s.find('熙')+1]

with open('./codes.txt','w',encoding='utf-8') as f:#「codes.txt」にresult_sを書き込みます
    f.write(result_s)
