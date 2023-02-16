from cProfile import label
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo, showerror, askyesno, showwarning

def read_words(f):

  list=[]
  f.seek(0)
  for i in f:
    if len(i.strip("\n"))>=3:

     list.append(i.strip("\n").upper())

  return list


def read_sequences(f2):
    """*****************cle*********************************"""
    d = {}
    f2.seek(0)
    i = 0
    for x in f2:

        pos = x.find("|")
        s = ""
        if (pos != -1):
            for c in range(pos + 1, len(x)):
                if x[c] == "|":
                    w = c
                    break
                else:
                    s = s + x[c]
            cle = s
            d[cle] = 0
            """*****************séquence*********************************"""
    f2.seek(0)

    ch = f2.read()
    f2.seek(0)
    l = ch.split(">")
    del l[0]

    i = 0
    for key in d:
        col = l[i]
        pos2 = col.find("\n")
        val = col[pos2:len(col)]
        d[key] = val
        i += 1

    return d
"""****************************exercice 3 *************************************"""
"""def search_words_in_proteome(dic,list) :


    dicMots = {}
    for i in list:
        nbDeSq = 0
        for j in dic.values():
            if j.find(i) != -1:
                nbDeSq += 1
        dicMots[i] = nbDeSq

    return (dicMots)"""
def search_words_in_proteome(dic,list) :


    dicMots = {}
    for i in list:
        nbocc = 0
        for j in dic.values():
          nbocc =nbocc+j.count(i)
        dicMots[i] = nbocc

    return (dicMots)

"""*******************************question 4*****************************"""
def find_most_frequent_word(dic):
    l=[]
    for key in dic:
        l.append(dic[key])
    maxVal=max(l)
    for key in dic:
        if dic[key]==maxVal :
            mot=key
            nbrSeq=dic[key]

    l=[mot,nbrSeq]
    print(mot, "found in ", nbrSeq, "sequences")
    return l


"""************************************interface*************************************"""
f=open("D:/python/LPE-BI_Mini-projet Python/english-common-words.txt")
f.seek(0)
f2 = open("D:/python/LPE-BI_Mini-projet Python/human-proteome.fasta")
f2.seek(0)

def parite2():
    dic = read_sequences(f2)
    list1 = read_words(f)
    d = search_words_in_proteome(dic, list1)
    code2= var2.get()


    if (code2 in d.keys()):
            messagebox.showinfo("le nombre de mots sélectionnés", "lenombre de mot : "+ str(d[code2]))
    else:
            messagebox.showinfo("le nombre de mots sélectionnés", "erreur")

def parite():

    d =read_sequences(f2)
    code= var1.get()

    for key in d:
        if (code==key):
            messagebox.showinfo("la séquence :", "la séquence est : "+ d[key])

def longeur():
    messagebox.showinfo("le nombre de mots:", "le nombre totale des mots : "+str( len(read_words(f))))

def longeur2():
    messagebox.showinfo(" séquences:", "le nombre totale de séquences : "+str( len(read_sequences(f2))))

def mot_plus_fréquent():
    l=find_most_frequent_word(search_words_in_proteome(read_sequences(f2),read_words(f)))
    messagebox.showinfo("plus fréquent",l[0]+ "found in "+ str(l[1])+ "sequences")

main=Tk()
main.title("Mini_Projet")
main.config(background="#FEF5E7")
main.geometry("1000x480")
main.iconbitmap("logo (1).ico")
#ajouter un 1re texte
label_text = Label (main, text ="bienvenue sur l'application" , font=("courrier", 30) , bg='#FEF5E7', fg='#85808A ' )
label_text.pack()

frame = Frame(main, bg="#FEF5E7",  relief=SUNKEN)
l1=Label(frame,text ="id des protéines:",bg="#FEF5E7",font=("courrier", 15), fg='#85808A ')
l1.pack(side=LEFT)
var1=StringVar()
E1=Entry(frame , textvariable=var1 ,width=100 ,bd=4)
E1.pack()
Button(frame,text='recherche', command=parite, width=50,bg="#ABB2B9").pack( padx=6, pady=6)
frame.pack(expand=YES)

frame2 = Frame(main, bg="#FEF5E7",  relief=SUNKEN)
l2=Label(frame2,text ="Mot cherché:",bg="#FEF5E7",font=("courrier", 15), fg='#85808A ')
l2.pack(side=LEFT)
var2=StringVar()
E2=Entry(frame2, textvariable=var2 ,width=100 ,bd=4)
E2.pack()

Button(frame2,text='recherche', command=parite2,width=50, bg="#ABB2B9").pack( padx=6, pady=6)
frame2.pack(expand=YES)
frame3 = Frame(main, bg="#FEF5E7",  relief=SUNKEN)
Button(frame3,text='le nombre de mot totale', command=longeur , width=40, bg="#ABB2B9").pack(side=RIGHT,padx=6, pady=6)
Button(frame3,text='nombre totale de séquences', command=longeur2,width=40, bg="#ABB2B9").pack(side=RIGHT, padx=6, pady=6)
Button(frame3,text='plus_fréquent', command=mot_plus_fréquent,width=40, bg="#ABB2B9").pack(side=RIGHT, padx=6, pady=6)
frame3.pack(expand=YES)
B1=Button(main, text="annuler",command=main.quit,bg="#ABB2B9",width=7)
B1.pack( padx=6, pady=6,side=RIGHT)

main.mainloop()








