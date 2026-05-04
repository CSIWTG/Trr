from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel
import random
from PyQt5.QtCore import QTimer, Qt
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QTransform

mon = 100
age = 0
hatchlvl = 0
stav = "den"
lock = False
enemies = []
enemak = [
    {"name": "Zombi", "img": "Zombi.png", "spd": 1, "dmg": 2, "hp": 2},
    {"name": "Skeli", "img": "Skeli.png", "spd": 2, "dmg": 1, "hp": 1},
    {"name": "Slim", "img": "Slim.png", "spd": 1, "dmg": 2, "hp": 3},
    {"name": "Ammoni", "img": "Ammoni.png", "spd": 1, "dmg": 3, "hp": 2}
]
personaliii = ["Chrabry", "Zbabeli", "Mrštný", "Obžerství"   ]
nemoci = []
event = "X"
hlad = 0
LedSwitch = 0
envir = "Domov"
Hp = 1
sub_buttons = []
start = False
povaha = random.choice(personaliii)
UIstate = "X"
print(povaha)
app = QtWidgets.QApplication([])
novak = QtWidgets.QWidget()
novak.resize(600, 300)
novak.setWindowIcon(QIcon(r"TB.png"))
novak.setWindowTitle('Minigotchi')
novak.setFixedSize(600, 300)
novak.setObjectName("Min")
novak.setStyleSheet("""
#Min {
    border-image: url("Pikij.png") 0 0 0 0 stretch stretch;
}
""")
console = QPushButton(novak)
console = QPushButton(novak)
console.setIcon(QIcon("ConsoleNull.png"))
console.move(120,45)
console.setIconSize(QSize(130, 230))
console.show()
console.setStyleSheet("""
    QPushButton {
        border: none;
        background: transparent;
    }
    QPushButton:hover {
        background: transparent;
    }
    QPushButton:pressed {
        background: transparent;
    }
""")
inputer = QLineEdit(novak)
inputer.setGeometry(150, 200, 60, 30)
inputer.hide()
noc = QLabel(novak)
noc.setGeometry(0, 0, 600, 300)
noc.setStyleSheet("background-color: rgba(0, 0, 0, 80);")
noc.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
noc.hide()
zmrz = QPushButton(novak)
zmrz = QPushButton(novak)
zmrz.setIcon(QIcon(r"IceCreamVan.png"))
zmrz.move(38,40)
zmrz.setIconSize(QSize(180, 280))
zmrz.hide()
zmrz.setStyleSheet("""
    QPushButton {
        border: none;
        background: transparent;
    }
    QPushButton:hover {
        background: transparent;
    }
    QPushButton:pressed {
        background: transparent;
    }
""")
psik = QPushButton(novak)
psik.setIcon(QIcon(r"Psik.png"))
psik.move(420,58)
psik.setIconSize(QSize(180, 280))
psik.hide()
psik.setStyleSheet("""
    QPushButton {
        border: none;
        background: transparent;
    }
    QPushButton:hover {
        background: transparent;
    }
    QPushButton:pressed {
        background: transparent;
    }
""")
hopkun = QPushButton(novak)
hopkun.setIcon(QIcon(r"HopKonik.png"))
hopkun.move(300,25)
hopkun.setIconSize(QSize(180, 280))
hopkun.hide()
hopkun.setStyleSheet("""
    QPushButton {
        border: none;
        background: transparent;
    }
    QPushButton:hover {
        background: transparent;
    }
    QPushButton:pressed {
        background: transparent;
    }
""")
menuexit = QPushButton(novak)
menuexit.setIcon(QIcon(r"MinLilIdio.png"))
menuexit.hide()
menuexit.move(67,-50)
menuexit.setIconSize(QSize(450, 500))
menuexit.setStyleSheet("""
    background: transparent;
    border: none;
""")
minik = QPushButton(novak)
minik.hide()
minik.setIcon(QIcon(r"MinLilIdio.png"))
minik.move(204,0)
minik.setFixedSize(160, 360)
minik.setIconSize(QSize(180, 380))
minik.setStyleSheet("""
    QPushButton {
        border: none;
        background: transparent;
    }
    QPushButton:hover {
        background: transparent;
    }
    QPushButton:pressed {
        background: transparent;
    }
""")

vajco = QPushButton(novak)
vajco.setIcon(QIcon(r"MinEgg.png"))
vajco.setIconSize(QSize(160, 200))
vajco.move(200,110)
vajco.setStyleSheet("""
    QPushButton {
        border: none;
        background: transparent;
    }
    QPushButton:hover {
        background: transparent;
    }
    QPushButton:pressed {
        background: transparent;
    }
""")
 
frig = QPushButton(novak)
frig.move(450,140)
frig.setFixedSize(QSize(40, 80))
frig.setStyleSheet("""
QPushButton {
    border: none;
    background: transparent;
    border-image: url("Frigider.png");
}
QPushButton:hover {
    border-image: url("FrigiderB.png");
}
""")
minarickabytost = False
um = QPushButton(novak)
um.move(-20,135)
um.setIcon(QIcon(r"UzuriMazura.png"))
um.hide()
um.setFixedSize(220, 180)
um.setIconSize(QSize(220, 300))
um.setStyleSheet("""
QPushButton {
    border: none;
    background: transparent;;
}
""")
lajna = QLabel(novak)
lajna.setText(f"{mon}")
lajna.setStyleSheet("color: black; font-size: 16px;")
lajna.adjustSize()
lajna.move((600 - lajna.width()) // 2, 5)
 
def zmena():
    lajna.setText(f"{mon:g}")
 
HPBar = QPushButton(novak)
HPBar.setIcon(QIcon(r"1.png"))
HUBar = QPushButton(novak)
HUBar.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
HPBar.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
HUBar.setIcon(QIcon(r"1H.png"))
HPBar.setIconSize(QSize(250, 300))
HPBar.move(0,-130)
HUBar.move(0,-100)
HUBar.setIconSize(QSize(250, 300))
HPBar.setStyleSheet("""
    QPushButton {
        border: none;
        background: transparent;
    }
    QPushButton:hover {
        background: transparent;
    }
    QPushButton:pressed {
        background: transparent;
    }
""")
HUBar.setStyleSheet("""
    QPushButton {
        border: none;
        background: transparent;
    }
    QPushButton:hover {
        background: transparent;
    }
    QPushButton:pressed {
        background: transparent;
    }
""")
 
frigmenu = QPushButton(novak)
frigmenu.setIcon(QIcon(r"Frigimenu.png"))
frigmenu.move(67,-50)
frigmenu.setIconSize(QSize(450, 500))
frigmenu.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
frigmenu.hide()
frigmenu.setStyleSheet("""
    QPushButton {
        border: none;
        background: transparent;
    }
    QPushButton:hover {
        background: transparent;
    }
    QPushButton:pressed {
        background: transparent;
    }
""")
'''frigmenu.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)'''
Iterator = 0
frip = QPushButton(novak)
frip.setIcon(QIcon(r"Next.png"))
frip.move(440,116)
frip.setIconSize(QSize(30, 30))
frip.hide()
frip.setStyleSheet("""
    QPushButton {
        border: none;
        background: transparent;
    }
    QPushButton:hover {
        background: transparent;
    }
    QPushButton:pressed {
        background: transparent;
    }
""")

'''
for objekt, x, y, png in dekorace:
    btn = QPushButton(novak)
    btn.setGeometry(x, y, 100, 50)
    btn.setIcon(f"Min{png}.png")
    btn.setIconSize(QSize(40, 40))
    btn.setStyleSheet("""
    QPushButton {
        border: none;
        background: transparent;
    }
    QPushButton:hover {
        background: transparent;
    }
    QPushButton:pressed {
        background: transparent;
    }
""")
'''

def zmrzf():
    global LedSwitch
    global lock
    global UIstate
    if LedSwitch == 0:
        frigmenu.setIcon(QIcon(f"ZmrzMenu.png"))
        UIstate = "Zmrz"
        menuexit.show()
        frigmenu.show()
        for item in zmrzliny:
            item["button"].show()
            item["label"].show()
        update("Zmrz")
        LedSwitch = 1
    else:
        UIstate = "X"
        frigmenu.hide()
        frip.hide()
        menuexit.hide()
        for item in zmrzliny:
            item["button"].hide()
            item["label"].hide()
        LedSwitch = 0

def Switcharoonie(enemy=None):
    global Iterator
    global hlad
    if Iterator == 1:
        HPBar.setIcon(QIcon(f"1.png"))
        vajco.setIcon(QIcon("MinEgg.png"))
        vajco.show()
        minik.hide()
    elif Iterator == 2:
        vajco.hide()
        um.hide()
        if len(nemoci) > 0:
            minik.setIcon(QIcon(f"Min{random.choice(nemoci)}.png"))
            return
        elif hlad > 0:
            minik.setIcon(QIcon("MinHungry.png"))
        else:
            minik.setIcon(QIcon(f"Min{povaha}.png"))
    elif Iterator == 3:
        widget = enemy.get("widget")
        if widget:
            widget.hide()
            widget.deleteLater()
        enemy["widget"] = None
        if enemy in enemies:
            enemies.remove(enemy)
        if hlad > 0:
            minik.setIcon(QIcon("MinHungry.png"))
        else:
            minik.setIcon(QIcon(f"Min{povaha}.png"))
           
ZStoggle = 0

def zneskodnit(enemy):
    enemy["alive"] = False
    widget = enemy.get("widget")
    if widget:
        widget.hide()
        widget.deleteLater()
    enemy["widget"] = None

def sezer(item):
    global Hp, hlad, UIstate, Iterator, povaha, mon
    if item["count"] <= 0:
        return
    if item["name"] == "Horkopes":
        if hlad == 0 and not povaha == "Obžerství":
            return
        if not povaha == "Obžerství":
            if hlad - 2 == -1:
                hlad = hlad - 1
                mon += 1
            else:
                hlad = hlad - 2
                mon += 2
        else:
            hlad = hlad - 2
            mon += 2
    elif item["name"] == "Pizza":
        if random.randint(1,2) == 2:
            if hlad == 0 and not povaha == "Obžerství":
                return
            hlad = hlad - 1
            mon += 1
        else:
            if not Hp == 1:
                Hp = Hp - 1
                mon += 1
            else:
                return
    elif item["name"] == "Nugetky":
        if hlad == 0 and not povaha == "Obžerství":
            return
        hlad = hlad - 1
        mon += 1
    elif item["name"] == "Monster":
        if not Hp == 1:
            Hp = Hp - 1
            mon += 1
        else:
            return
    elif item["name"] == "Drogy":
        if len(nemoci) > 0:
            nemoci.pop()
            Iterator = 2
            Switcharoonie()
        else:
            return
    elif item["name"] == "Vroci":
        if hlad == 0 and not povaha == "Obžerství":
            return
        if random.randint(1,2) == 2:
            hlad = hlad - 1
        mon += 1
    else:
        if hlad == 0 and not povaha == "Obžerství":
            return
        hlad = hlad - 1
        mon += 1
    item["count"] = item["count"] - 1
    HPBar.setIcon(QIcon(f"{Hp}.png"))
    if hlad < 6:
            HUBar.setIcon(QIcon(f"{hlad+1}H.png"))
            if hlad < -3:
                minik.setIcon(QIcon("Burt.png"))
            if hlad == 5:
                HPBar.setIcon(QIcon(f"{hlad-3}.png"))
    zmena()         
    Iterator = 2
    Switcharoonie()
    update(UIstate)
 
def chcipl():
    global age
    global hatchlvl
    global hlad
    global start
    global povaha
    global Hp
    global Iterator
    global ZStoggle, agedotaznik
    hybaj.stop()
    ani.stop()
    spawner.stop()
    kladno.stop()
    cyklus.stop()
    ZStoggle = 0
    start = False
    HPBar.setIcon(QIcon(f"5.png"))
    vajco.setIcon(QIcon(f"GunPoint.png"))
    minik.setIcon(QIcon(r"Mrtvej.png"))
    povaha = random.choice(personaliii)
    print(povaha)
    hatchlvl = 0
    hlad = 0
    age = 0
    Hp = 1
    agedotaznik = False
    Iterator = 1
    QTimer.singleShot(300,Switcharoonie)

nabytky = [
    {"name": "Maple", "img": "PotMaple.png", "y": 211, "x": 240, "price": 150, "type": 1, "count": 0, "object": None},
    {"name": "NastenkaOpic", "img": "MinApe.png", "y": 211, "x": 340, "price": 120, "type": 2, "count": 0, "object": None},
    {"name": "Bonsai", "img": "PotBonsai.png", "y": 140, "x": 340, "price": 150, "type": 1, "count": 0, "object": None},
    {"name": "Bulba", "img": "PotBulbus.png", "y": 211, "x": 140, "price": 150, "type": 1, "count": 0, "object": None},
    {"name": "NastenkaVseho", "img": "Borda.png", "y": 140, "x": 240, "price": 150, "type": 2, "count": 0, "object": None},
    {"name": "SlavaArmenii", "img": "AtZijeArcach.png", "y": 140, "x": 140, "price": 120, "type": 2, "count": 0, "object": None}
]

jidlicka = [
    {"name": "Horkopes", "img": "Horkopes.png", "y": 211, "x": 240, "price": 50, "count": 0},
    {"name": "Pizza", "img": "Pizza.png", "y": 211, "x": 340, "price": 40, "count": 0},
    {"name": "Nugetky", "img": "Nugetky.png", "y": 140, "x": 340, "price": 35, "count": 2},
    {"name": "Monster", "img": "Monster.png", "y": 211, "x": 140, "price": 45, "count": 0},
    {"name": "Drogy", "img": "Drogy.png", "y": 140, "x": 240, "price": 50, "count": 0},
    {"name": "Vroci", "img": "Vroci.png", "y": 140, "x": 140, "price": 20, "count": 1}
]

zmrzliny = [
    {"name": "Cookie", "img": "ZCookie.png", "y": 211, "x": 240, "price": 30, "count": 0},
    {"name": "Ruska", "img": "ZPycknn.png", "y": 211, "x": 340, "price": 30, "count": 0},
    {"name": "Mint", "img": "ZMint.png", "y": 150, "x": 340, "price": 30, "count": 0},
    {"name": "Vanila", "img": "ZVanila.png", "y": 211, "x": 140, "price": 30, "count": 0},
    {"name": "Limon", "img": "ZLimon.png", "y": 150, "x": 240, "price": 30, "count": 0},
    {"name": "Choco", "img": "ZChoco.png", "y": 150, "x": 140, "price": 30, "count": 0}
]

multi = 1
def update(mode):
    global event
    global multi
    if mode == "Led":
        for item in jidlicka:
            if event == "BL" or event == "E":
                item["label"].setText(f"{item['price']*multi}$!")
            else:
                item["label"].setText(f"{item['price']}$")
    elif mode == "Zmrz":
        for item in zmrzliny:
            if event == "BL" or event == "E":
                item["label"].setText(f"{item['price']*multi}$!")
            else:
                item["label"].setText(f"{item['price']}$")
    elif mode == "Hamu":
        for item in jidlicka:
            item["label"].setText(f"({item['count']})")
    elif mode == "Zimi":
        for item in zmrzliny:
            item["label"].setText(f"({item['count']})")
    elif mode == "Nakup":
        for item in nabytky:
            if event == "BL":
                item["label"].setText(f"{item['price']-15}$")
            elif event == "E":
                item["label"].setText(f"{item['price']+40}$")
            else:
                item["label"].setText(f"{item['price']}$")
   
def HorsiNezFilipTurekOtaznik(item):
    global mon
    global multi
    if mon < item["price"] * multi:
        return
    mon -= item["price"] * multi
    item["count"] += 1
    update(UIstate)
    zmena()
 
jidlo_btns = []
jidlo_inputs = []
 
def volbyvarmenii(item):
    if UIstate == "Led":
        HorsiNezFilipTurekOtaznik(item)
    else:
        if lock:
            return
        sezer(item)

def aktivujeme(item):
    global mon, multi, hlad
    if UIstate == "Zmrz":
        if mon < item["price"] * multi:
            return
        mon -= item["price"] * multi
        item["count"] += 1
        zmena()
        update(UIstate)
    else:
        if item["count"] <= 0:
            return
        if hlad == 0:
            return
        item["count"] -= 1
        hlad -= 1
        if hlad < 0:
            hlad = 0
        HUBar.setIcon(QIcon(f"{hlad+1}H.png"))
        zmena()
        update(UIstate)

for item in jidlicka:
    btn = QPushButton(novak)
    btn.setIcon(QIcon(item["img"]))
    btn.setGeometry(item["x"], item["y"], 115, 50)
    btn.setIconSize(QSize(60,60))
    btn.hide()
    btn.setStyleSheet("""
    QPushButton {
        border: none;
        background: transparent;
    }
    """)
    label = QLabel(novak)
    label.setGeometry(item["x"] + 85, item["y"], 140, 50)
    label.setStyleSheet("color: black; font-size: 14px; background: transparent;")
    label.hide()
    label.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
    item["button"] = btn
    item["label"] = label
    btn.clicked.connect(lambda _, i=item: volbyvarmenii(i))

for item in zmrzliny:
    btn = QPushButton(novak)
    btn.setIcon(QIcon(item["img"]))
    btn.setGeometry(item["x"], item["y"], 115, 50)
    btn.setIconSize(QSize(60,60))
    btn.hide()
    btn.setStyleSheet("""
    QPushButton {
        border: none;
        background: transparent;
    }
    """)
    label = QLabel(novak)
    label.setGeometry(item["x"] + 85, item["y"], 140, 50)
    label.setStyleSheet("color: black; font-size: 14px; background: transparent;")
    label.hide()
    label.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
    item["button"] = btn
    item["label"] = label
    btn.clicked.connect(lambda _, i=item: aktivujeme(i))

def updateenvir():
    for item in nabytky:
        if item["count"] > 0:
            if item["object"] is None:
                obj = QPushButton(novak)
                obj.setIcon(QIcon(item["img"]))
                if item["type"] == 1:
                    obj.move(56, 73)
                else:
                    obj.move(150, 45)
                obj.setIconSize(QSize(140,140))
                obj.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
                obj.show()
                obj.lower()
                console.lower()
                item["object"] = obj
                obj.setStyleSheet("""
    QPushButton {
        border: none;
        background: transparent;
    }
    """)
            else:
                item["object"].show()
        
def koupimesikocicku(item):
    global mon
    global multi
    if multi == 0.5:
        multiv = 15
    else:
        multiv = -40
    if mon < item["price"] - multiv:
        return
    mon = mon - (item["price"] - multiv)
    for jini in nabytky:
        if jini["type"] == item["type"] and jini != item:
            jini["count"] = 0
            if jini["object"]:
                jini["object"].hide()
                jini["object"].deleteLater()
                jini["object"] = None
    item["count"] = 1
    zmena()
    update("Nakup")
    updateenvir()

for item in nabytky:
    btn = QPushButton(novak)
    btn.setIcon(QIcon(item["img"]))
    btn.setGeometry(item["x"], item["y"], 115, 50)
    btn.setIconSize(QSize(60,60))
    btn.hide()
    btn.clicked.connect(lambda _, i=item: koupimesikocicku(i))
    btn.setStyleSheet("""
    QPushButton {
        border: none;
        background: transparent;
    }
    """)
    label = QLabel(novak)
    label.setGeometry(item["x"] + 85, item["y"], 140, 50)
    label.setStyleSheet("color: black; font-size: 14px; background: transparent;")
    label.hide()
    label.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
    item["button"] = btn
    item["label"] = label

def swap(enemy, losos=None):
    widget = enemy.get("widget")
    if widget is None:
        return
    img = losos if losos else enemy["data"]["img"]
    pix = QPixmap(img)
    if pix.isNull():
        print(f"Missing image: {img}")
        return
    if enemy.get("rot") == "left":
        pix = pix.transformed(QTransform().scale(-1, 1))
    widget.setIcon(QIcon(pix))

def animacija(enemy, killornot):
    global lalala
    enemy["zmrznihajzle"] = "ne"
    if not killornot:
        vajco.setIcon(QIcon("GunPoint.png"))
        lalala = 0
        enemy["zmrznihajzle"] = "ne"
        swap(enemy)
        return
    widget = enemy.get("widget")
    try:
        if widget:
            zneskodnit(enemy)
    except RuntimeError:
        return
    if enemy in enemies:
        enemies.remove(enemy)
    vajco.setIcon(QIcon("GunPoint.png"))
    swap(enemy)
    lalala = 0

def consola():
    global RepublikaTaiwan
    global mon
    global nemoci
    global Iterator
    if RepublikaTaiwan > 29:
        console.setIcon(QIcon("Console.png"))
        if inputer.isVisible():
            text = inputer.text().strip()    
            if text == "Money": 
                mon = mon + 100 
                zmena()
            elif text == "Noc" or text == "Den":
                day_night()
            elif text == "Nemoc":
                nemoci.append(random.choice(["Demence", "Nemoc", "Nemoc Šílených Krav", "ModraNemoc"]))
                print(nemoci)
                Iterator = 2
                Switcharoonie()
            elif text == "Artsakh" or text == "Palestine":
                obj = QPushButton(novak)
                obj.setIcon(QIcon(f"{text}.png"))
                obj.move(150, 45)
                obj.setIconSize(QSize(140,140))
                obj.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
                obj.show()
                obj.lower()
                console.lower()
                item["object"] = obj
                obj.setStyleSheet("""
    QPushButton {
        border: none;
        background: transparent;
    }
    """)
            elif text == "UM" or text == "um" or text == "Uzuri Mazura" or text == "uzuri mazura":
                global minarickabytost
                minarickabytost = True
            inputer.hide()
            inputer.clear()
        else:
            inputer.show()
            inputer.setFocus()
    else:
        RepublikaTaiwan += 1

def zabijho(enemy, skin):
    global hatchlvl
    global lalala
    if hatchlvl == 10:
        lalala = 10
        noc.raise_()
        vajco.setIcon(QIcon("Shot.png"))
        matarael = skin.replace(".png", "")
        widget = enemy["widget"]
        widget.setIcon(QIcon(f"{matarael}Murder.png"))
        enemy["hp"] = enemy["hp"] - 1
        swap(enemy, f"{matarael}Murder.png")
        enemy["zmrznihajzle"] = "ano"
        if enemy["hp"] < 1:
            QTimer.singleShot(300, lambda: animacija(enemy, True))
        else:
            QTimer.singleShot(300, lambda: animacija(enemy, False))


def utok(enemy):
    global Hp, povaha, Iterator, enemies
    if not enemy or not enemy.get("widget"):
        return
    damage = enemy["data"]["dmg"]
    if povaha == "Chrabry" and random.randint(1, 2) == 2:
        minik.setIcon(QIcon("MinAttack.png"))
        Iterator = 3
        QTimer.singleShot(300, lambda e=enemy: Switcharoonie(e))
        return
    Hp += damage
    if Hp > 4:
        Hp = 5
        chcipl()
    HPBar.setIcon(QIcon(f"{Hp}.png"))
    zneskodnit(enemy)
    if enemy in enemies:
        enemies.remove(enemy)

def spawnzombi():
    if random.randint(1,3) == 3:
        data = random.choice(enemak[2:4])
    else:
        data = random.choice(enemak[0:2])
    ene = QPushButton(novak)
    ene.setIcon(QIcon(data["img"]))
    ene.setIconSize(QSize(180, 380))
    ene.setFixedSize(180, 370)
    Zmenik = QPixmap(data["img"])
    flipped = Zmenik.transformed(QTransform().scale(-1, 1))
    if random.randint(1,2) == 2:
        x = 550
        dir = "right"
    else:
        x = -100
        dir = "left"
        ene.setIcon(QIcon(flipped))
    y = 10
    ene.move(x, y)
    ene.show()
    ene.lower()
    global envir
    for item in nabytky:
        obj = item.get("object")
        if obj:
            obj.lower()
    frig.lower()
    console.lower()
    ene.setStyleSheet("""
    QPushButton {
        border: none;
        background: transparent;
    }
    QPushButton:hover {
        background: transparent;
    }
    QPushButton:pressed {
        background: transparent;
    }
""")
    enemy = {
        "widget": ene,
        "data": data,
        "rot": dir,
        "zmrznihajzle": "ne",
        "hp": data["hp"],
        "frame": 0
    }
    swap(enemy)
    ene.clicked.connect(lambda _, e=enemy: zabijho(e, data["img"]))
    enemies.append(enemy)

lalala = 0
def m1917m():
    for enemy in enemies:
        if enemy.get("zmrznihajzle") == "ano":
            continue
        img = enemy["data"]["img"]
        matarael = img.replace(".png", "")
        if enemy["frame"] == 0:
            enemy["frame"] = 1
            swap(enemy, f"{matarael}2.png")
        else:
            enemy["frame"] = 0
            swap(enemy, f"{matarael}.png")

artsakh = 0
def piskoviste():
    global start
    global lock
    global artsakh
    if not start:
        return
    if lock and not artsakh == 1:
        return
    if artsakh == 0:
        lock = True
        artsakh = 1
        minik.hide()
        psik.setIcon(QIcon(r"Psik2.png"))
    else:
        artsakh = 0
        minik.show()
        psik.setIcon(QIcon(r"Psik.png"))
        lock = False

def hamu_papu(trr=None):
    global start
    global LedSwitch
    global UIstate
    if not start:
        return
    if LedSwitch == 0 or trr == "Kosova":
        for item in jidlicka:
            item["button"].hide()
            item["label"].hide()
        for item in zmrzliny:
            item["button"].hide()
            item["label"].hide()
        frip.show()
        menuexit.show()
        frigmenu.setIcon(QIcon(r"Inventormenu.png"))
        frigmenu.show()
        LedSwitch = 1
        if UIstate == "Hamu":
            UIstate = "Zimi"
            for item in zmrzliny:
                item["button"].show()
                item["label"].show()
                update("Zimi")
        else:
            UIstate = "Hamu"
            for item in jidlicka:
                item["button"].show()
                item["label"].show()
                update("Hamu")
        LedSwitch = 1
    else:
        if trr == "Kosova":
            return
        menuexit.hide()
        UIstate = "X"
        LedSwitch = 0
        for item in jidlicka:
            item["button"].hide()
            item["label"].hide()
        for item in zmrzliny:
                item["button"].hide()
                item["label"].hide()
        frip.hide()
        frigmenu.hide()
 
def zmrdetaktydostanes():
    global start
    global Iterator
    global povaha
    global ZStoggle
    if not start:
        return
    if lock:
        return
    global Hp
    if povaha == "Mrštný" and random.randint(1,2) == 2:
            minik.setIcon(QIcon(f"MinVýmyk.png"))
            Iterator = 2
            QTimer.singleShot(300,Switcharoonie)
            ZStoggle = 0
            return
    Hp = Hp + 1
    HPBar.setIcon(QIcon(f"{Hp}.png"))
    Iterator = 2
    minik.setIcon(QIcon(f"Kopan.png"))
    QTimer.singleShot(300,Switcharoonie)
    if Hp >= 5:
        chcipl()

def schovse():
    global envir
    for item in nabytky:
        obj = item.get("object")
        if obj:
            if envir == "Hriste":
                obj.hide()
            else:
                obj.show()

def navod(Type):
    global envir
    global start
    global stav
    global event, minarickabytost
    if not event == "RN":
        pejsek = ""
    else:
        pejsek = event
    if lock and not Type == "Exit":
        return
    if not start:
        return
    if stav == "noc":
        return
    inputer.hide()
    if envir == "Domov":
        envir = "Hriste"
        novak.setStyleSheet(f"""
#Min {{
    border-image: url("Fild{pejsek}.png");
}}
""")
        frig.hide()
        console.hide()
        psik.show()
        hopkun.show()
        schovse()
        if minarickabytost:
            um.show()
            um.setIcon(QIcon(f"UzuriMazura.png"))
        if event == "Z":
            zmrz.show()
    else:
        envir = "Domov"
        novak.setStyleSheet(f"""
#Min {{
    border-image: url("Pikij{pejsek}.png");
}}
""")
        frig.show()
        um.hide()
        psik.hide()
        console.show()
        zmrz.hide()
        hopkun.hide()
        minik.show()
        schovse()

def hybame():
    if not minik.isVisible():
        return
    mx, my = minik.x(), minik.y()
    toremove = []
    for enemy in enemies[:]:
        ene = enemy["widget"]
        if ene is None:
            continue
        spd = enemy["data"]["spd"]
        ex, ey = ene.x(), ene.y()
        if enemy.get("zmrznihajzle") != "ano":
            if ex < mx:
                ex += spd
            elif ex > mx:
                ex -= spd

            if ey < my:
                ey += spd
            elif ey > my:
                ey -= spd
            ene.move(ex, ey)
        if abs(ex - mx) < 30 and abs(ey - my) < 30:
            toremove.append(enemy)
    for enemy in toremove:
        utok(enemy)

hybaj = QTimer(novak)
hybaj.timeout.connect(hybame)
ani = QTimer(novak)
ani.timeout.connect(m1917m)
spawner = QTimer(novak)
spawner.timeout.connect(spawnzombi)

def zastrel():
    global ZStoggle
    global start
    global Hp
    if not start:
        return
    if lock:
        return
    global hatchlvl
    global povaha
    if ZStoggle == 1:
        ZStoggle = 0
        vajco.hide()
        return
    ZStoggle = 1
    vajco.show()
    vajco.setIcon(QIcon(f"GunPoint.png"))
    hatchlvl = 10

def nakupy():
    global LedSwitch
    global UIstate
    if UIstate == "Led" or UIstate == "Hamu":
        return
    if LedSwitch == 0:
        frigmenu.setIcon(QIcon("NabytMenu.png"))
        UIstate = "Nakup"
        menuexit.show()
        frigmenu.show()
        for item in nabytky:
            item["button"].show()
            item["label"].show()
        update("Nakup")
        LedSwitch = 1
    else:
        UIstate = "X"
        frip.hide()
        frigmenu.hide()
        menuexit.hide()
        for item in nabytky:
            item["button"].hide()
            item["label"].hide()
        LedSwitch = 0

def toggle_menu():
    if not sub_buttons:
        return
    if len(sub_buttons) == 0:
        return
    is_visible = sub_buttons[0].isVisible()
    for btn in sub_buttons:
        btn.setVisible(not is_visible)
 
menu_items = [
    ("IcoPizza.png", 45, hamu_papu),
    ("IcoBox.png", 80, zmrdetaktydostanes),
    ("IcoGuide.png", 115, navod),
    ("IcoEgg.png", 150, zastrel),
    ("Nabyt.png", 185, nakupy)
]
 
for obrazek, y, funk in menu_items:
    btn = QPushButton(novak)
    btn.setGeometry(522, y, 100, 50)
    btn.setIcon(QIcon(obrazek))
    btn.setIconSize(QSize(40, 40))
    btn.setStyleSheet("""
    QPushButton {
        border: none;
        background: transparent;
    }
    QPushButton:hover {
        background: transparent;
    }
    QPushButton:pressed {
        background: transparent;
    }
""")
    btn.hide()
    btn.clicked.connect(funk)
    sub_buttons.append(btn)
 
menu_btn = QPushButton(novak)
menu_btn.setIcon(QIcon(r"Menu.png"))
menu_btn.setIconSize(QSize(40, 40))
menu_btn.move(550,10)
menu_btn.setStyleSheet("background: transparent; border: none;")
menu_btn.clicked.connect(toggle_menu)
 
def chud():
    global hlad
    global lock
    global start
    global mon
    global stav
    global nemoci
    global Iterator
    if not start:
        return
    if lock:
        return
    if stav == "noc" and not event == "E":
        return
    lock = True
    hlad += 1
    Iterator = 2
    Switcharoonie()
    if hlad < 6:
        HUBar.setIcon(QIcon(f"{hlad+1}H.png"))
        if hlad == 5:
            HPBar.setIcon(QIcon(f"{hlad-3}.png"))
    else:
        if not hlad == 8:
            HPBar.setIcon(QIcon(f"{hlad-3}.png"))
        else:
            chcipl()
    if random.randint(1,15) == 3:
        mon = mon + random.randint(10,50)
        zmena()
    if random.randint(1, 20) == 3:
        nemoci.append(random.choice(["Demence", "Nemoc", "Nemoc Šílených Krav", "ModraNemoc"]))
        print(nemoci)
    lock = False

konik = 10000

def houpatrozkaz():
    minik.hide()
    global konik
    global start
    global lock
    if not start:
        return
    lock = True
    hopkun.setIcon(QIcon(f"{konik}Kun.png"))
    if not konik == 7:
        konik = konik + 1
    else:
        konik = 1

def day_night():
    global stav
    global envir
    global event
    global mon
    global multi
    global Iterator
    global minarickabytost, prokleti
    minik.show()
    if envir == "Hriste":
        navod("Exit")
    if stav == "den":
        kladno.stop()
        noc.show()
        stav = "noc"
        nocniteror = ["B", "BL", "E"]
        if random.randint(1,2) == 2:
            event = random.choice(nocniteror)
        else:
            event = "N"
        novak.setStyleSheet(f"""
#Min {{
    border-image: url("Pikij{event}.png");
}}
""")
        if prokleti:
            event == "B"
        if event == "B":
            spawner.start(random.randint(6000,10000))
        elif event == "BL":
            multi = 0.5
        elif event == "E":
            multi = 1.5
        else:
            multi = 1
            cyklus.stop()
            cyklus.start(60000)
            minik.setIcon(QIcon("MinikSleep.png"))
    else:
        if random.randint(1,4) == 4:
            event = "Z"
        elif random.randint(1,4) == 3:
            event = "RN"
        else:
            event = ""
        psik = event
        if psik == "Z":
            psik = ""
        if random.randint(1,20) == 5:
            minarickabytost = True
            print("An Angel has descended from the heavens")
        Iterator = 2
        Switcharoonie()
        stav = "den"
        spawner.stop()
        novak.setStyleSheet(f"""
#Min {{
    border-image: url("Pikij{psik}.png");
}}
""")
        
        noc.hide()
        mon = mon + random.randint(20,70)
        zmena()


timer = QTimer(novak)
timer.timeout.connect(chud)
kladno = QTimer(novak)
kladno.timeout.connect(houpatrozkaz)
cyklus = QTimer(novak)
cyklus.timeout.connect(day_night)

def Eggon():
    timer.start(20000)
    cyklus.start(80000)
    hybaj.start(35)
    ani.start(300)

def hrajsi():
    global konik
    global lock
    if lock and konik == 10000:
        return
    if konik == 10000:
        lock = True
        konik = 0
        kladno.start(200)
    else:
        konik = 10000
        lock = False
        hopkun.setIcon(QIcon(f"HopKonik.png"))
        kladno.stop()
        minik.show()

def hatch():
    global age
    global povaha
    global hatchlvl
    global hlad
    global lock
    global start
    global event
    global Iterator
    global Hp
    global ZStoggle
    if lock:
        return
    lock = True
    if hatchlvl == 0:
        vajco.setIcon(QIcon(r"Crack2.png"))
    elif hatchlvl == 1:
        vajco.setIcon(QIcon(r"Crack3.png"))
    elif hatchlvl == 2:
        vajco.setIcon(QIcon(r"EggFinale.png"))
    elif hatchlvl == 10:
        vajco.setIcon(QIcon(r"Shot.png"))
        if povaha == "Mrštný" and random.randint(1,2) == 2:
            minik.setIcon(QIcon(f"MinVýmyk.png"))
            Iterator = 2
            QTimer.singleShot(300,Switcharoonie)
            ZStoggle = 0
            lock = False
            return
        minik.setIcon(QIcon(f"Min{random.randint(1,3)}.png"))
        Hp = 5
        QTimer.singleShot(320,chcipl)
    else:
        start = True
        Eggon()
        HPBar.setIcon(QIcon(f"1.png"))
        HUBar.setIcon(QIcon(f"1H.png"))
        minik.setIcon(QIcon(r"MinLilIdio.png"))
        minik.show()
        vajco.hide()
        age = 1
        hlad = 0
        if event == "B":
            spawner.start(random.randint(6000,10000))
            hybaj.start(35)
    hatchlvl = hatchlvl + 1
    lock = False

prokleti = False
def umf():
    global hatchlvl, Iterator, minarickabytost, prokleti
    if not hatchlvl == 10:
        um.setIcon(QIcon("UzuriMazuraLay.png"))
    else:
        um.setIcon(QIcon("UzuriMazuraMurder.png"))
        Iterator = 2
        QTimer.singleShot(300,Switcharoonie)
        minarickabytost = False
        prokleti = True

agedotaznik = False

def ageup():
    global agedotaznik
    if agedotaznik:
        return
    agedotaznik = True
    minik.setIcon(QIcon(f"Min{povaha}.png"))
 
def led():
    global LedSwitch
    global lock
    global UIstate
    if LedSwitch == 0:
        frigmenu.setIcon(QIcon(f"FrigiMenu.png"))
        UIstate = "Led"
        menuexit.show()
        frigmenu.show()
        for item in jidlicka:
            item["button"].show()
            item["label"].show()
        update("Led")
        LedSwitch = 1
    else:
        UIstate = "X"
        frip.hide()
        frigmenu.hide()
        menuexit.hide()
        for item in jidlicka:
            item["button"].hide()
            item["label"].hide()
        LedSwitch = 0
 
def masa():
    global UIstate
    if not frigmenu.isVisible():
        return
    if UIstate == "Hamu":
        hamu_papu()
    elif UIstate == "Led":
        led()
    elif UIstate == "Nakup":
        nakupy()
    else:
        zmrzf()
       
LedSwitch=0
RepublikaTaiwan = 0

vajco.clicked.connect(hatch)
minik.clicked.connect(ageup)
#minik.clicked.connect(day_night)
frig.clicked.connect(led)
menuexit.clicked.connect(masa)
hopkun.clicked.connect(hrajsi)
psik.clicked.connect(piskoviste)
zmrz.clicked.connect(zmrzf)
console.clicked.connect(consola)
frip.clicked.connect(lambda _, : hamu_papu("Kosova"))
um.clicked.connect(umf)

noc.raise_()
novak.show()
app.exec_()