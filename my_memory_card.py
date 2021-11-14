#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QButtonGroup, QRadioButton, QMessageBox, QPushButton, QLabel, QVBoxLayout, QHBoxLayout ,QLabel, QGroupBox)
from random import shuffle, randint



class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

points = 0
question_count = 0

question_list = []
question_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
question_list.append(Question('Какого цвета нету на флаге России?', 'Зеленый', 'Красный','Белый', 'Синий'))
question_list.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))

app = QApplication([])

btnok = QPushButton('Ответить')
lbquestion = QLabel('Самый сложный вопрос в мире!')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn1 = QRadioButton('Вариант 1')
rbtn2 = QRadioButton('Вариант 2')
rbtn3 = QRadioButton('Вариант 3')
rbtn4 = QRadioButton('Вариант 4')

Radiogroup = QButtonGroup()
Radiogroup.addButton(rbtn1)
Radiogroup.addButton(rbtn2)
Radiogroup.addButton(rbtn3)
Radiogroup.addButton(rbtn4)

layoutans1 = QHBoxLayout()
layoutans2 = QVBoxLayout()
layoutans3 = QVBoxLayout()

layoutans2.addWidget(rbtn1)
layoutans2.addWidget(rbtn2)
layoutans3.addWidget(rbtn3)
layoutans3.addWidget(rbtn4)

layoutans1.addLayout(layoutans2)
layoutans1.addLayout(layoutans3)

RadioGroupBox.setLayout(layoutans1)

Ansgroupbox = QGroupBox('Результат теста')
lb_result = QLabel('прав ты или нет?')
lb_correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_result)
layout_res.addWidget(lb_correct, alignment=Qt.AlignHCenter, stretch = 2)
Ansgroupbox.setLayout(layout_res)

ResultGroupBox = ('Результат тестирования')
lb_Result_Test = QLabel('')
layout_test_res = QVBoxLayout()
layout_test_res.addWidget(lb_Result_Test)
ResultGroupBox.setLayout(layout_test_res)

layoutline1 = QHBoxLayout()
layoutline2 = QHBoxLayout()
layoutline3 = QHBoxLayout()

layoutline1.addWidget(lbquestion)
layoutline2.addWidget(RadioGroupBox)
layoutline2.addWidget(Ansgroupbox)
layout_line2.addWidget(ResultGroupBox)
Ansgroupbox.hide()
ResultGroupBox.hide()

layoutline3.addStretch(1)
layoutline3.addWidget(btnok, stretch=2)
layoutline3.addStretch(1)

layoutcard = QVBoxLayout()

layoutcard.addLayout(layoutline1, stretch=2)
layoutcard.addLayout(layoutline2, stretch=8)
layoutcard.addStretch(1)
layoutcard.addLayout(layoutline3, stretch=1)
layoutcard.addStretch(1)
layoutcard.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    Ansgroupbox.show()
    btnok.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    Ansgroupbox.hide()
    btnok.setText('Ответить')
    Radiogroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    Radiogroup.setExclusive(True)

answers = [rbtn1, rbtn2, rbtn3, rbtn4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lbquestion.setText(q.question)
    lb_correct.setText(q.right_answer)
    question_list.remove(q)
    show_question()

def show_correct(res):
    lb_result.setText(res)
    show_result()



def check_answer():
    global points, question_count
    if answers[0].isChecked():
        question_count += 1
        points += 1
        show_correct('Правильно. Счет:', str(points))
    else:
        question_count += 1
        if answers[1].isChecked() or answers[2].isChecked or answers[3].isChecked:
            show_correct('Неверно')

def next_question():
    if len(question_list) == 0:
        show_test_result()
    else:
        window.cur_question = window.cur_question = randint(0, len(question_list)-1)
        q = question_list[window.cur_question]
        ask(q)

def show_test_result():
    global points, question_count
    RadioGroupBox.hide()
    Ansgroupbox.hide()
    lb_Result_Test.setText('Ваш результат:' + str(points) + '/' + str(questions_count))
    ResultGroupBox.show()

def clickok():
    if btnok.text() == 'Ответить':
        check_answer()
    else:
        next_question 


window = QWidget()
window.setLayout(layoutcard)
window.setWindowTitle('Memo card')
window.cur_question = -1
btnok.clicked.connect(clickok)
next_question()
window.resize(400, 300)
window.show()
app.exec_()