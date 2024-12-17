kalimat = "REC adalah kursus robotik di Jogja"
print(len(kalimat)) #output 34

huruf_terakhir = kalimat[len(kalimat)-1]
print(huruf_terakhir) #output 'a'

huruf_terakhir_versi2 = kalimat[-1]
print(huruf_terakhir_versi2)  #output 'a'

kalimat = "Robotik Education" 
i=0
while i < len(kalimat):
    print(kalimat[i],end='\n')
    i += 1


kalimat = "Aku anak sehat"
for kal in kalimat:
    print(kal,end='\n')

    