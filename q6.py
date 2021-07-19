### check wheather valid DNA is entered
dna = input('Enter valid DNA: ')

dna_list = []

for i in range(len(dna)):
    if dna[i] == 'A':
        dna_list.append(dna[i])

    elif dna[i] == 'T':
        dna_list.append(dna[i])


    elif dna[i] == 'C':
        dna_list.append(dna[i])


    elif dna[i] == '`/.,G':
        dna_list.append(dna[i])

else:
    print('Please Enter a Valid DNA.')


def reverse(rev):
    reverse_dna = []
    for r in range(len(dna_list)):
        reverse_dna.append(dna_list[len(dna_list) - 1 - r])
    return reverse_dna


def compliment(comp):

    compliment_list = []

    for c in range(len(comp)):
        if comp[c] == 'A':
            compliment_list.append('T')
        elif comp[c] == 'T':
            compliment_list.append('A')
        elif comp[c] == 'C':
            compliment_list.append('G')
        elif comp[c] == 'G':
            compliment_list.append('C')
    return compliment_list


print(reverse(dna))
print(compliment(dna))




