# 第一题: 淘气还是乖孩子（Naughty or Nice）
def naughty_or_nice(data):
    naughty_count = 0
    nice_count = 0
    
    for month in data.values():
        for value in month.values():
            if value == 'Naughty':
                naughty_count += 1
            else:
                nice_count += 1
    
    if naughty_count > nice_count:
        return "Naughty!"
    elif nice_count > naughty_count:
        return "Nice!"
    else:
        return "Nice!"

# 第二题：观察到的PIN（The observed PIN）
def get_pins(observed):
    adjacent_digits = {
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['5', '7', '8', '9', '0'],
        '9': ['6', '8', '9'],
        '0': ['0', '8']
    }
    variations = ['']
    for digit in observed:
        new_variations = []
        for variation in variations:
            for adjacent_digit in adjacent_digits[digit]:
                new_variations.append(variation + adjacent_digit)
        variations = new_variations
    return variations

# 第三题：RNA到蛋白质序列的翻译（RNA to Protein Sequence Translation）
def protein(rna):
    protein_seq = ''
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        if codon in PROTEIN_DICT:
            amino_acid = PROTEIN_DICT[codon]
            if amino_acid == 'Stop':
                break
            protein_seq += amino_acid
    return protein_seq

# 第四题：填写订单（Thinkful - Dictionary drills: Order filler）
def fillable(stock, merch, n):
    if merch in stock and stock[merch] >= n:
        return True
    else:
        return False