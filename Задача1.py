# Python v 3.7
# -*- coding: utf-8 -*-
upper_chr=''.join(list(map(chr, (i for i in range(ord('А'),ord('Я')+1)))))
lower_chr=''.join(list(map(chr, (i for i in range(ord('а'),ord('я')+1)))))
upper_chr=upper_chr[:6]+'Ё'+upper_chr[6:]
lower_chr=lower_chr[:6]+'ё'+lower_chr[6:]
k=['','0']
a=open('input.txt','r',encoding='utf-8').read()

for i in a:
    i=i.lower()
    if i.isalpha() and a.lower().count(i) > int(k[1]):
        k[0]=i
        k[1]=a.lower().count(i)
        
N=ord(lower_chr[lower_chr.index(k[0])])-ord(lower_chr[lower_chr.index('о')])
decode_upper_chr=upper_chr[-N:]+upper_chr[:-N]
decode_lower_chr=lower_chr[-N:]+lower_chr[:-N]
trantab = str.maketrans(upper_chr, decode_upper_chr)
a=a.translate(trantab)
trantab = str.maketrans(lower_chr, decode_lower_chr)
a=a.translate(trantab)
open('output.txt','w').write(a)
