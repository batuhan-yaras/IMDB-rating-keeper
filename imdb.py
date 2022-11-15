import requests
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QWidget, QTextEdit
import sys

class Imdb(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.info = QLabel("""Write down an IMDB Rating\n
        You'll see the TOP 250 movies which has higher IMDB Rating than what you wrote.\n
        (Please use '.' for a float)\n""")
        self.rating = QLabel("IMDB")
        self.linetext = QLineEdit()
        self.button = QPushButton("Ara")
        self.results = QTextEdit()

        h_box = QHBoxLayout()
        h_box.addWidget(self.rating)
        h_box.addWidget(self.linetext)
        h_box.addWidget(self.button)
        h_box.addStretch()

        v_box = QVBoxLayout()
        v_box.addWidget(self.info)
        v_box.addLayout(h_box)
        v_box.addWidget(self.results)

        self.setWindowTitle("IMDB TOP 250 Movies From Website")

        self.setLayout(v_box)

        self.button.clicked.connect(self.datas)
        self.show()


    def datas(self):
        url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
        response = requests.get(url)

        html = response.content

        soup = BeautifulSoup(html, "html.parser")

        titles = soup.find_all("td", {"class": "titleColumn"})
        ratings = soup.find_all("td", {"class": "ratingColumn imdbRating"})

        text2 = str("")
        for i, j in zip(titles, ratings):
            i = i.text
            j = j.text

            i = i.strip()
            i = i.replace("\n", "")

            j = j.strip()
            j = j.replace("\n", "")

            if j > self.linetext.text():
                text2 += "Film: " + i + "\nIMDB: " + j + "\n\n"

        self.results.setText(text2)


app = QApplication(sys.argv)
imdb = Imdb()
sys.exit(app.exec_())
