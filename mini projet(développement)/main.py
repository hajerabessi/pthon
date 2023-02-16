from words_in_proteome import *
print("************question 1 *****************")
f=open("D:/python/LPE-BI_Mini-projet Python/english-common-words.txt")

print(len(read_words(f)))
f.seek(0)

print("**********************question 2***************************")

f2 = open("D:/python/LPE-BI_Mini-projet Python/human-proteome.fasta")
print("***********dictionnaires**************************")
print("*****************nombre de séquence*************************")
nombreSec=len(read_sequences(f2))
print(nombreSec)
print("************ la séquence à la protéine O95139 ********************* ")
dict = read_sequences(f2)
print(dict["O95139"])
f2.seek(0)
print("*******************************exercice 3*******************************")

list1=read_words(f)
var=search_words_in_proteome(dict,list1)
for cle in var:
    print(cle ,"Found in ",var[cle],"sequence")
print("**************************question 4******************************")
listCleVal=find_most_frequent_word(search_words_in_proteome(read_sequences(f2),read_words(f)))
print("Quel est le pourcentage des séquences du protéome qui contiennent ce mot:\n" ,int(( listCleVal[1]*100)/len(read_sequences(f2))),"%")
