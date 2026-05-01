from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, QTimer
import random

veci = {
    "Horkopes": 0,
    "Pizza": 0,
    "Nuggetky": 0,
    "Monster": 0,
    "Drogy": 0,
    "Vroci": 0
}

mon = 100
age = 0
hatchlvl = 0
lock = False
start = False

personaliii = ["Chrabry", "Zbabeli", "Mrštný", "Obžerství"]
povaha = random.choice(personaliii)

hlad = 0
Hp = 1

jidlo_btns = []
jidlo_labels = []

app = QtWidgets.QApplication([])

novak = QtWidgets.QWidget()
novak.resize(600, 300)
novak.setWindowTitle("Minigotchi")
novak.setFixedSize(600, 300)
novak.setObjectName("Min")

novak.setStyleSheet("""
#Min {
    border-image: url("Pikij.png") 0 0 0 0 stretch stretch;
}
""")

minik = QPushButton(novak)
minik.hide()
minik.setIcon(QIcon("MinLilIdio.png"))
minik.move(204, 0)
minik.setIconSize(QSize(180, 380))
minik.setStyleSheet("border:none;background:transparent;")

vajco = QPushButton(novak)
vajco.setIcon(QIcon("MinEgg.png"))
vajco.setIconSize(QSize(160, 200))
vajco.move(200, 110)
vajco.setStyleSheet("border:none;background:transparent;")

frig = QPushButton(novak)
frig.setIcon(QIcon("Frigider.png"))
frig.move(430, 140)
frig.setIconSize(QSize(60, 80))
frig.setStyleSheet("border:none;background:transparent;")

mon_label = QLabel(novak)
mon_label.setStyleSheet("color:white;font-size:18px;background:transparent;")
mon_label.setText(str(mon))
mon_label.adjustSize()
mon_label.move((600 - mon_label.width()) // 2, 5)


def update_money():
    mon_label.setText(str(mon))
    mon_label.adjustSize()
    mon_label.move((600 - mon_label.width()) // 2, 5)


HPBar = QPushButton(novak)
HPBar.setIcon(QIcon("1.png"))
HPBar.setIconSize(QSize(250, 300))
HPBar.move(0, -130)
HPBar.setStyleSheet("border:none;background:transparent;")

HUBar = QPushButton(novak)
HUBar.setIcon(QIcon("1H.png"))
HUBar.setIconSize(QSize(250, 300))
HUBar.move(0, -100)
HUBar.setStyleSheet("border:none;background:transparent;")

frigmenu = QPushButton(novak)
frigmenu.setIcon(QIcon("Frigimenu.png"))
frigmenu.setIconSize(QSize(450, 500))
frigmenu.move(67, -50)
frigmenu.hide()
frigmenu.setStyleSheet("border:none;background:transparent;")


veci_names = ["Horkopes", "Pizza", "Nuggetky", "Monster", "Drogy", "Vroci"]

jidlo = [
    ("Horkopes", "Horkopes.png", 211, 240),
    ("Pizza", "Pizza.png", 211, 340),
    ("Nuggetky", "Nuggetky.png", 140, 340),
    ("Monster", "Monster.png", 211, 140),
    ("Drogy", "Drogy.png", 140, 240),
    ("Vroci", "Vroci.png", 140, 140)
]


def update_inventory():
    for name, label in jidlo_labels:
        label.setText(f"count {name} in Veci ({veci[name]})")


def eat_item(name):
    veci[name] += 1
    update_inventory()


for name, img, y, x in jidlo:

    btn = QPushButton(novak)
    btn.setIcon(QIcon(img))
    btn.setGeometry(x, y, 115, 50)
    btn.setIconSize(QSize(60, 60))
    btn.hide()
    btn.setStyleSheet("border:none;background:transparent;")

    label = QLabel(novak)
    label.setGeometry(x + 85, y + 10, 150, 30)
    label.setStyleSheet("color:white;font-size:14px;background:transparent;")
    label.setText(f"count {name} in Veci (0)")
    label.hide()

    btn.clicked.connect(lambda _, n=name: eat_item(n))

    jidlo_btns.append((btn, name))
    jidlo_labels.append((name, label))


LedSwitch = 0


def hamu_papu():
    global LedSwitch, start

    if not start:
        return

    if LedSwitch == 0:
        frigmenu.show()

        for (btn, name), (n2, label) in zip(jidlo_btns, jidlo_labels):
            btn.show()
            label.show()

        update_inventory()
        LedSwitch = 1

    else:
        frigmenu.hide()

        for (btn, _), (_, label) in zip(jidlo_btns, jidlo_labels):
            btn.hide()
            label.hide()

        LedSwitch = 0


def led():
    hamu_papu()


def hatch():
    global start, hatchlvl

    hatchlvl += 1

    if hatchlvl > 2:
        start = True
        vajco.hide()
        minik.show()


vajco.clicked.connect(hatch)
frig.clicked.connect(led)
frigmenu.clicked.connect(led)

novak.show()
app.exec_()