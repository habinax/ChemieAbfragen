import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from os import listdir
import random

alles = """Phenol
Pyridin
Pyrimidin
Pyrrol
Resorcin
Asparaginsäure
Styrol
Thiazol
Thiophen
Thiophenol
Toluol
Xylol
Cycloheptatrien
Cyclooctatetraen
Cyclopentadien
Cystein
Pyran (y-Pyran)
Acetaldehyd
Aceton
Acetophenon
Acetylaceton
Benzaldehyd
Carvon
Formaldehyd / Methanal
Phenylethanal
Seleno-Cystein
Acetamid / Essigsäureamid
Acetanhydrid / Essigsäureanhydrid
Acetessigester / Essigsäureethylester
Acrylsäure / (Acrylat)
Acrylsäureamid / Acrylamid
Acrylsäuremethylester (Methacrylat)
Acrylsäureethylester (Ethylacrylat)
Ameisensäure / Methansäure
Benzoesäure
Buttersäure
Glutamin
Dimethylacrylamid
Dimethylformamid
Essigsäure / Ethansäure
Essigsäureanhydrid/Acetanhydrid
Ethylmethylacrylat / Methacrylsäureethylester
Methacrylsäure
Methylbenzoat/Benzoesäuremethylester
Methylmethacrylat / Methacrylsäuremethylester
Methylporpionat / Propionsäuremethylester
N,N-Dimethylpropionsäureamid
Glutaminsäure
Propansäureanhydrid
Vinylacetat / Essigsäurevinylester
Linolensäure
Linolsäure
Ölsäure
Palmitinsäure
Stearinsäure
Bernsteinsäureanhydrid
Bernsteinsäure
Glycin
Dimethylfumarat / Fumarsäuredimethylester
Dimethylmalonat / Malonsäuredimethylester
Dimethyloxalat / Oxalsäuredimethylester
Dimethylphthalat / Phthalsäuredimethylester
Fumarsäure
Glutarsäure
Maleinsäureamid / Maleinimid
Maleinsäure
Malonsäure
Oxalsäure
Histidin
Phthalsäure
Phthalsäureanhydrid
Acetessigsäure
Acetylcholin
Acetylsalicylsäure
Äpfelsäure
Biuret
Brenztraubensäure
γ-Butyrolacton
Zitronensäure
Isoleucin
Dimethylmalat / Apfelsäuredimethylester
Dimethyltartrat / Weinsäuredimethylester
Ethyllactat / Milchsäureethylester
Milchsäure
γ-Lactam
γ-Lactim
Methyllactat / Milchsäuremethylester
Methylsalicylat / Salicylsäuremethylester
Milchsäure
Phenylpyruvat / Phenylbrenztraubensäure
Leucin
Salicylsäure
δ-Valerolacton
Weinsäure
Adenin
Cytosin
Guanin
Purin
Thymin
Uracil
Lysin
5-Methylcytosin
Butanal
Cyclohexanol
Cyclohexen
Cyclopenten
Diethylether
Dimethylamin
Dimethylether
Ethanol
Ethylamin / Ethanamin
Methionin
Ethylmethylether
Methanal / Formaldehyd
Octanol
Pentanol
Propanal
Propansäure
Propionsäureamid
Propin
Proylen / Propen
1,3-Cyclopentandion
Phenylalanin
2-Aminoethanol
2-Methyl-1-propanol
2-Propanol / Isopropanol
3-Hydroxybuttersäure
Ascorbinsäure
Chinon
Cholin
Cholsäure
Cysteamin
Prolin
Dehydroascorbinsäure
Dihydroxyaceton
Glycerin
Harnsäure
Harnstoff
Hydrochinon
Steran
Tyramin
Vanillin
Acrylnitril
Serin
Decalin
Dibenzoylperoxid
Dimethylglyoxim
H4EDTA / EthylenDiaminTetraessigsäure (Acid)
Glykol / genauer: Ethylglykol
Isopren
Methylenblau
Morpholin
Ninhydrin
Piperidin
Threonin
Pyrrolidin
Tetrahydrofuran
Thalidomid
Vinylchlorid
2-Hydroxytetrahydropyran
Tryptophan
Tyrosin
Valin
ß-Alanin
Alanin
Acetylcystein
Acetylglycin
Hydroxyprolin
D-Fructose (R: ß-D-Fructofuranose) Rechts?
D-Glucose (R: ß-D-Glucopyranose)
Maltose
D-Ribulose
Arginin
Saccharose
D-Gluconolacton
Gluconsäure
D-Glycerinaldehyd
Riboflavin
D-Sorbitol
Anilin
Brenzcatechin (1,2-Dihydroxybenzol)
Asparagin
Chinolin
Furan
Imidazol
Indol
Naphthalin
D-Galactose (R: a-D-Galactopyranose) Rechts?
D-Mannose (R: a-D-Mannopyranose) Rechts?
D-Ribose (R: ß-D-Ribofuranose) Rechts?
D-Xylose (R: ß-D-Xylofuranose)"""


import os
cwd = os.getcwd()
listallestoffe = alles.split("\n")

onlyfiles = [f for f in listdir(cwd+"\\venv\\Picturesprinttopdf")]
print(len(onlyfiles))
dic = []
for i in range(len(onlyfiles)):
    # im = Image.open("C:\\Users\\inap\\PycharmProjects\\ChemieAbfragen\\venv\\Picturesprinttopdf\\mol-"+str(i)+".png")
    dic.append(
        [cwd+"\\venv\\Picturesprinttopdf\\mol-" + str(i) + ".png",
         listallestoffe[i]])

class MyGUI:
    def loadNewMol(self):
        allestoffecopy = listallestoffe.copy()
        buttonlist=[]
        rint=random.randint(0,len(listallestoffe))
        # self.image_path=""
        # self.image_path=dic[rint][0]
        buttonlist.append(dic[rint][1])
        allestoffecopy.remove(dic[rint][1])

        print("rint: ", rint)
        print(len(dic))

        lowerborder = rint-15
        higherborder = rint+15
        if lowerborder<0:
            lowerborder=0
        if higherborder>len(listallestoffe):
            higherborder=len(listallestoffe)-1
        print("higherboarder: ", higherborder)
        print("lowerboarder: ", lowerborder)
        for i in range(0,4):
            buttonlist.append(allestoffecopy[random.randint(lowerborder,higherborder)])

        while any(buttonlist.count(x) > 1 for x in buttonlist):
            buttonlist.clear()
            buttonlist.append(dic[rint][1])
            for i in range(0,4):
                buttonlist.append(allestoffecopy[random.randint(lowerborder,higherborder)])

        self.clear_frame()
        self.image_path = dic[rint][0]  # Passe den Dateipfad zu deinem Bild an
        self.img = Image.open(self.image_path)
        i = self.img.size
        i = i[0] // 2, i[1] // 2
        newimg = self.img.resize(i)
        #self.img = self.img.resize((self.root.winfo_reqwidth(), self.root.winfo_reqheight()))
        self.tk_img = ImageTk.PhotoImage(newimg, Image.ANTIALIAS)

        # Oberer Teil des Fensters (Bildanzeige)
        self.image_label = tk.Label(self.root, image=self.tk_img)
        self.image_label.pack(side = 'left', expand=True, fill='both')

        # Unterer Teil des Fensters (Buttons)
        button_frame = tk.Frame(self.root)
        button_frame.pack(side='right', expand=True, fill='both')

        random.shuffle(buttonlist)

        # 5 verschiedene Buttons hinzufügen
        for i in range(len(buttonlist)):
            print(buttonlist[i])
            if buttonlist[i] is dic[rint][1]:
                button = tk.Button(button_frame, text=buttonlist[i], command=lambda i=i: self.button_clicked_right(i))
                button.grid(row=i, column=0, padx=10, pady=10)
            else:
                button = tk.Button(button_frame, text=buttonlist[i], command=lambda i=i: self.button_clicked_wrong(i,dic[rint][1]))
                button.grid(row=i, column=0 , padx=10, pady=10)

        # Fenster-Größenänderungsereignisse binden
        #self.root.bind("<Configure>", self.resize_image)

    def __init__(self, root):
        self.root = root
        self.root.title("Absoluter Chemie-Spaß!")
        self.root.configure(bg='#333333')  # Dunkelgrau

        self.loadNewMol()

    def resize_image(self, event):
        new_width = event.width
        new_height = event.height

        # Bild an die neue Größe anpassen
        self.img = self.img.resize((new_width, new_height), Image.ANTIALIAS)
        self.tk_img = ImageTk.PhotoImage(self.img)
        self.image_label.config(image=self.tk_img)

    def button_clicked_right(self, button_number):
        self.openNewWindowRight(button_number)

    def button_clicked_wrong(self, button_number,right_answer):
        newWindow = tk.Toplevel(self.root)
        newWindow.title("Richtig")

        # sets the geometry of toplevel
        newWindow.geometry("320x120+150+100")

        text_label = tk.Label(newWindow, text=f'Falsche Antwort!\nRichtige Antwort wäre: '+right_answer+'.')
        text_label.pack(padx=20, pady=20)

        # Button im neuen Fenster hinzufügen
        new_button = tk.Button(newWindow, text="Fortfahren",
                               command=lambda: self.close_and_execute_action(newWindow, button_number))
        new_button.pack(pady=10)

    def openNewWindowRight(self, button_number):
        newWindow = tk.Toplevel(self.root)
        newWindow.title("Richtig")

        # sets the geometry of toplevel
        newWindow.geometry("200x100+200+100")

        text_label = tk.Label(newWindow, text=f"Richtige Antwort!")
        text_label.pack(padx=20, pady=20)

        # Button im neuen Fenster hinzufügen
        new_button = tk.Button(newWindow, text="Fortfahren", command=lambda: self.close_and_execute_action(newWindow, button_number))
        new_button.pack(pady=10)

    def close_and_execute_action(self, window, button_number):
        # Fenster schließen
        window.destroy()
        # Hier die Aktion einfügen, die im vorherigen Fenster ausgeführt werden soll
        self.loadNewMol()



    def clear_frame(self):
        for widgets in self.root.winfo_children():
            widgets.destroy()
