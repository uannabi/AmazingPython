seq='sdfsdfkslfsdlkfjlaljdlsjf'
seq1='sdfsdfkslfsdlkfjlTljdlsjf'

zip_seq =zip(seq,seq1)

print(list(zip_seq))

enum_seqs=enumerate(zip_seq)

print(list(enum_seqs))

for i (a,b) in enum_seqs:
	if a!=b:
	    print(f'index:(i)')
 
