import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class ScoreLabel(tk.Label):
    def __init__(self, master, score, points_per_click, **kwargs):
        super().__init__(master, **kwargs)
        self.score = score
        self.points_per_click = points_per_click
        self.config(text=f"Score: {self.score}, Points per click: {self.points_per_click}")

    def increment_score(self):
        self.score += self.points_per_click
        self.config(text=f"Score: {self.score}, Points per click: {self.points_per_click}")

    def update_score(self, new_score):
        self.score = new_score
        self.config(text=f"Score: {self.score}, Points per click: {self.points_per_click}")

    def update_points_per_click(self, new_points_per_click):
        self.points_per_click = new_points_per_click
        self.config(text=f"Score: {self.score}, Points per click: {self.points_per_click}")
#See klass esindab kohandatud sildi vidinat, mis kuvab skoori ja punkte kliki kohta.
#__init__ meetod: Initsialiseerib sildi antud skoori ja punktide väärtusega kliki kohta.
#self.score: Salvestab praeguse skoori.
#self.points_per_click: Salvestab punktide väärtuse kliki kohta.
#self.config(text=f"Score: {self.score}, Points per click: {self.points_per_click}"): Seab sildi algse teksti, et kuvada skoori ja punkte kliki kohta.
#increment_score meetod: Suurendab skoori praeguse punktide väärtusega kliki kohta ja uuendab sildi teksti.
#update_score meetod: Seab skoori uuele väärtusele ja uuendab sildi teksti.
#update_points_per_click meetod: Seab punktide väärtuse kliki kohta uuele väärtusele ja uuendab sildi teksti.

class ScoreButton(tk.Button):
    def __init__(self, master, score_label, **kwargs):
        super().__init__(master, **kwargs)
        self.score_label = score_label
        self.config(text="Click", command=self.increment_score)

    def increment_score(self):
        self.score_label.increment_score()
#See klass esindab nuppu, mis suurendab skoori klikkimisel.
#__init__ meetod: Initsialiseerib nupu viitega ScoreLabel instantsile.
#self.score_label: Salvestab viite ScoreLabel instantsile.
#self.config(text="Klikk", command=self.increment_score): Seab nupu tekstiks "Klikk" ja määrab, et nupu klikkimisel kutsutakse increment_score meetod.
#increment_score meetod: Kutsutakse ScoreLabel instantsi increment_score meetodit, et suurendada skoori.

def complete_purchase(item, quantity, comment, score_label):
    item_cost = {
        "1": 200,
        "2": 400,
        "3": 1000,
        "4": 2000,
        "5": 3000,
        "6": 4000,
        "7": 7000,
        "8": 15000,
        "9": 30000,
        "kampsun": 500000,
        "T-särk": 250000,
        "püksid": 350000,
        "lühikesed püksid": 200000
    }
    points_per_click_increments = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 5,
        "5": 6,
        "6": 7,
        "7": 10,
        "8": 13,
        "9": 25
    }

    quantity = int(quantity) if quantity else 1
    total_cost = item_cost.get(item, 0) * quantity

    if score_label.score >= total_cost:
        score_label.update_score(score_label.score - total_cost)
        if item in points_per_click_increments:
            new_points_per_click = score_label.points_per_click + (points_per_click_increments[item] * quantity)
            score_label.update_points_per_click(new_points_per_click)
            print(f"Points per click increased to {new_points_per_click}")
        print(f"Olete ostnud {quantity} ühikut {item} kommentaariga: {comment}")
        save_purchase(item, quantity, comment, total_cost)
    else:
        print("You don't have enough clicks to purchase this item")
#Käitleb loogikat eseme ostmiseks.
#item_cost sõnastik: Seob eseme identifikaatorid nende maksumustega klikkides.
#points_per_click_increments sõnastik: Seob eseme identifikaatorid väärtuste kasvuga punktide kohta kliki kohta.
#quantity = int(quantity) if quantity else 1: Konverteerib koguse täisarvuks, vaikesättena 1, kui kogust pole määratud.
#total_cost = item_cost.get(item, 0) * quantity: Arvutab ostu kogumaksumuse.
#Kontrollib, kas kasutajal on piisavalt skoori, et ostu sooritada.
#Kui jah, uuendab skoori ja punkte kliki kohta vastavalt ning salvestab ostu.
#Kui ei, kuvab teate, et klikke pole piisavalt.

def save_purchase(item, quantity, comment, total_cost):
    with open("purchases.txt", "a") as file:
        file.write(f"Purchased {quantity} x {item} with comment: {comment} for {total_cost} clicks\n")
#Kirjutab ostu üksikasjad faili nimega "purchases.txt".

def show_submenu(button, event):
    submenu = tk.Menu(root, tearoff=0)
    if button == "Button-1":
        submenu.add_command(label="Osta asi 1", command=lambda: open_purchase_window("1"))
        submenu.add_command(label="Osta asi 2", command=lambda: open_purchase_window("2"))
        submenu.add_command(label="Osta asi 3", command=lambda: open_purchase_window("3"))
    elif button == "Button-2":
        submenu.add_command(label="Osta asi 4", command=lambda: open_purchase_window("4"))
        submenu.add_command(label="Osta asi 5", command=lambda: open_purchase_window("5"))
        submenu.add_command(label="Osta asi 6", command=lambda: open_purchase_window("6"))
    elif button == "Button-3":
        submenu.add_command(label="Osta asi 7", command=lambda: open_purchase_window("7"))
        submenu.add_command(label="Osta asi 8", command=lambda: open_purchase_window("8"))
        submenu.add_command(label="Osta asi 9", command=lambda: open_purchase_window("9"))
    elif button == "Button-4":
        submenu.add_command(label="kampsun", command=lambda: open_purchase_window("kampsun"))
        submenu.add_command(label="T-särk", command=lambda: open_purchase_window("T-särk"))
        submenu.add_command(label="püksid", command=lambda: open_purchase_window("püksid"))
        submenu.add_command(label="lühikesed püksid", command=lambda: open_purchase_window("lühikesed püksid"))
    submenu.post(event.x_root, event.y_root)
#Kuvab kontekstimenüü ostuvõimalustega, kui nuppu klõpsatakse.
#submenu = tk.Menu(root, tearoff=0): Loob uue kontekstimenüü.
#Lisab alammenüüle käsud sõltuvalt sellest, milline nupp klõpsati.
#submenu.post(event.x_root, event.y_root): Kuvab alammenüü kursori asukohas.

def open_purchase_window(item):
    purchase_window = tk.Toplevel(root)
    purchase_window.title(f"Ostma {item}")
    purchase_window.geometry("300x300")

    label = ttk.Label(purchase_window, text=f"Ostma {item}")
    label.pack(pady=10)

    quantity_label = ttk.Label(purchase_window, text="Arv:")
    quantity_label.pack(pady=5)

    quantity_entry = ttk.Entry(purchase_window)
    quantity_entry.pack(pady=5)

    predefined_comments = {
        "1": "aitab tuua söögituppa head toitu \n hind: 200 klikki / tk \n saada pumpamisel: +1 klikile",
        "2": "uute arvutite ostmine \n Hind: 400 klikki / tk \n saada pumpamisel: + 2 klikile",
        "3": "uute laudade ostmine aitab teil hästi õppida \n hind: 1000 klikki / tk \n saada pumpamisel: + 3 klikile.",
        "4": "konditsioneeri ostmine klassidesse \n Hind: 2000 klikki/ tk \n saada pumpamisel: + 5 klikile",
        "5": "tulekahjusignalisatsiooni ostmine \n Hind: 3000 klikki/tk \n saada pumpamisel: + 6 klikile",
        "6": "palgata rohkem õpetajaid \n Hind: 4000 klikki/ tk \n saada pumpamisel: + 7 klikile",
        "7": "täiustatud Interneti lisamine \n Hind: 7000 klikki/ tk \n saada pumpamisel: + 10 klikile",
        "8": "Veel ühe korruse lisamine IVKHK-le \n Hind: 15000 klikki/ tk \n saada pumpamisel: + 13 klikile",
        "9": "IVKHK uus filiaal Toilas \n Hind: 30000 klikki/ tk \n saada pumpamisel: + 25 klikile",
        "kampsun": "Kampsun IVKHK hind: 500000 klikki",
        "T-särk": "T-särk IVKHK hind: 250000 klikki",
        "püksid": "Püksid IVKHK hind: 350000 klikki",
        "lühikesed püksid": "Lühikesed püksid IVKHK hind: 200000 klikki"
    }

    predefined_comment = predefined_comments.get(item, "")
    if predefined_comment:
        comment_label = ttk.Label(purchase_window, text=f"Kommentaar: {predefined_comment}")
        comment_label.pack(pady=5)

    purchase_button = ttk.Button(purchase_window, text="Ostma", command=lambda: complete_purchase(item, quantity_entry.get(), predefined_comment, score_label))
    purchase_button.pack(pady=10)
#Avab uue akna valitud eseme ostmiseks.
#Kuvab esemespetsiifilised üksikasjad ja võimaldab kasutajal sisestada koguse.
#Pakub eelnevalt määratud kommentaari valitud eseme kohta.

def load_progress():
    try:
        with open("progress.txt", "r") as file:
            lines = file.readlines()
            score = int(lines[0].strip())
            points_per_click = int(lines[1].strip())
            return score, points_per_click
    except FileNotFoundError:
        return 0, 1  # Default values if file doesn't exist
#Laadib skoori ja punktide arvu kliki kohta failist "progress.txt".
#Tagastab vaikimisi väärtused, kui faili pole olemas.

def save_progress():
    with open("progress.txt", "w") as file:
        file.write(f"{score_label.score}\n")
        file.write(f"{score_label.points_per_click}\n")
#Salvestab praeguse skoori ja punktide arvu kliki kohta faili "progress.txt"

root = tk.Tk()
root.title("Cliker IVKHK")
root.geometry("850x625")

main_frame = ttk.Frame(root, padding="10 10 10 10")
main_frame.pack(expand=True, fill=tk.BOTH)

bottom_menu = ttk.Frame(root, padding="5 5 5 5")
bottom_menu.pack(side=tk.BOTTOM, fill=tk.X)
#Initsialiseerib peamise Tkinter akna ja raami.
#Laadib logo pildi ja loob nupud erinevate ostutasemete jaoks.

button1 = ttk.Button(bottom_menu, text="kliki eest pumpamine LVL1")
button2 = ttk.Button(bottom_menu, text="kliki eest pumpamine LVL2")
button3 = ttk.Button(bottom_menu, text="kliki eest pumpamine LVL3 ")
button4 = ttk.Button(bottom_menu, text="asjade ostmine müntidega")

button1.bind("<Button-1>", lambda event: show_submenu("Button-1", event))
button2.bind("<Button-1>", lambda event: show_submenu("Button-2", event))
button3.bind("<Button-1>", lambda event: show_submenu("Button-3", event))
button4.bind("<Button-1>", lambda event: show_submenu("Button-4", event))

button1.pack(side=tk.LEFT, padx=5, pady=5)
button2.pack(side=tk.LEFT, padx=5, pady=5)
button3.pack(side=tk.LEFT, padx=5, pady=5)
button4.pack(side=tk.LEFT, padx=5, pady=5)
#Loob nupud erinevate ostutasemete jaoks ja seob need alammenüü kuvamisega.

image = Image.open("ivkhk_logo2.jpg")
tk_image = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=tk_image)
image_label.pack()
#Laadib ja kuvab IVKHK logo pildi.

score, points_per_click = load_progress()
score_label = ScoreLabel(root, score, points_per_click)
score_label.pack()
score_button = ScoreButton(root, score_label)
score_button.pack()
#Laadib algse skoori ja punktide arvu kliki kohta.
#Loob ja paigutab ScoreLabel ja ScoreButton.


root.protocol("WM_DELETE_WINDOW", lambda: (save_progress(), root.destroy()))
#Konfigureerib peamise akna salvestama progressi, kui see suletakse.

root.mainloop() 
#Käivitab Tkinteri peamise tsükli, et rakendus töötaks.

root.update()
