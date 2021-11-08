raw_translation = "A = chi B = tsu C = te D = to E = na F = ni G = nu H = ne I = no J = ha K = hi L = fu M = he N = ho O = ma P = mi Q = mu R = me S = mo T = ya U = yu V = yo W = ra X = ri Y = ru Z = re 1 = a 2 = i 3 = u 4 = u 5 = o 6 = ka 7 = ki 8 = ku 9 = ke 0 = --"
raw_translation = raw_translation.replace(' = ',':').split()

translated_dict = {' ':' '}
for i in raw_translation:
    element = i.split(':')
    translated_dict[element[0].lower()] = element[1]

def eng_to_jpn():
    name = input('Enter your name: ')
    jpn_name = ''
    for i in name:
        jpn_name += translated_dict[i.lower()]
    return jpn_name

print(eng_to_jpn())
