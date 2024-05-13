# Подключить нужные модули (QtCore и QtWidgets и их элементы)
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,
QHBoxLayout, QRadioButton, QGroupBox, QButtonGroup)
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
question_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
question_list.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))


# Создать объект-приложение ( app )
app = QApplication([])
# Создать окно приложения ( window )
window = QWidget()
# Задать заголовок
window.setWindowTitle('Memory Card')
# Можно задать размеры ( resize )
window.resize(400, 300)
# Создать виджеты - вопрос ( lb_Question ) и кнопку «Ответить» ( btn_OK )
lb_Question = QLabel('Какой национальности не существует?')
btn_OK = QPushButton('Ответить')

# СОЗДАТЬ НАБОР ПЕРЕКЛЮЧАТЕЛЕЙ С ВАРИАНТАМИ ОТВЕТОВ ( RadioGroupBox )
RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton("Энцы")
rbtn_2 = QRadioButton("Смурфы")
rbtn_3 = QRadioButton("Чулымцы")
rbtn_4 = QRadioButton("Алеуты")

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox. setLayout(layout_ans1)

# Создать группу на экране для переключателей с ответами ( RadioGroupBox )
# Создать набор переключателей с вариантами ответов ( rbtn_1 ... rbtn_4 )
# Создать горизонтальную направляющую линию ( layout_ans1 )
# Создать 2 вертикальные направляющие линии ( layout_ans2 и layout_ans3 )
# Добавить виджеты к направляющей линии ( rbtn_1 и rbtn_2 -> layout_ans2 )
# Добавить виджеты к направляющей линии ( rbtn_3 и rbtn_4 -> layout_ans3 )
# Добавить 2 вертикальных лэйаута к горизонтальному ( layout_ans2 и layout_ans3 -> layout_ans1 )
# Сделать лэйаут содержимым группы ( layout_ans1 -> RadioGroupBox )


# Создать группу на экране для результата ( AnsGroupBox )
AnsGroupBox = QGroupBox('Результат теста')

# Создать надпись с результатом ( lb_Result )
lb_Result = QLabel('Прав ты или уволен?')

# Создать надпись с правильным ответом ( lb_Correct )
lb_Correct = QLabel('Ответ будет тут!')

# Создать вертикальную направляющую линию ( layout_res )
layout_res = QVBoxLayout()

# Добавить к лэйауту надписи с результатом и правильным ответом ( lb_Result и lb_Correct -> layout_res )
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)

# Сделать лэйаут содержимым группы ( layout_res -> AnsGroupBox )
AnsGroupBox.setLayout(layout_res)

# Создать 3 горизонтальные направляющие линии ( layout_line1 ... layout_line3 )
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
# Добавить виджеты к направляющим:
# lb_Question -> layout_line1
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
# RadioGroupBox -> layout_line2
layout_line2.addWidget(RadioGroupBox)

# AnsGroupBox -> layout_line2
layout_line2.addWidget(AnsGroupBox)

AnsGroupBox.hide()

# btn_OK -> layout_line3
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

# Создать главный вертикальный лэйаут ( layout_card )
layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

window.setLayout(layout_card)

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')

    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4] #создание списка вопросов

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()


def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов:', window.score)
        print('Рейтинг: ', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked or answers[3].isChecked():
            show_correct('Неверно')
            print('Рейтинг: ',(window.score/window.total*100), '%')

def next_question():
    window.total += 1
    print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов:', window.score)
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window.cur_question = -1

btn_OK.clicked.connect(click_OK)

window.score = 0
window.total = 0
    # Добавить по очереди 3 горизонтальных лэйаута с виджетами к главному лэйауту ( layout_line1 ... layout_line3 -> layout_card )

# Добавить главный вертикальный лэйаут с объектами в окно приложения ( layout_card -> window )
window.setLayout(layout_card)
# Сделать окно ( window ) видимым и оставить приложение ( app ) открытым
window.show()
app.exec()
