from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QRadioButton, QGroupBox, QVBoxLayout, \
    QHBoxLayout, QButtonGroup
from PyQt5.QtGui import QFont
from random import *

app = QApplication([])
main_window = QWidget()
main_window.resize(1000, 1000)
main_window.setWindowTitle('Irregular verbs')
main_window.setWindowState(Qt.WindowFullScreen)

main_font = QFont('Castellar', 8)
bold_font = QFont('Artifakt Element Heavy', 10)
group_font = QFont('Arial', 8)

main_layout = QHBoxLayout()

layoutV1 = QVBoxLayout()
layoutV2 = QVBoxLayout()


def make_group(group, group_main_layout, group_layoutH1, group_layoutV1, group_dict, layoutH1or2, words):
    groups_layoutH1_text1 = QLabel('Перевод')
    groups_layoutH1_text1.setFont(bold_font)
    groups_layoutH1_text1.setStyleSheet('color: rgb(255, 25, 25);')
    groups_layoutH1_text2 = QLabel('Infinitive')
    groups_layoutH1_text2.setFont(bold_font)
    groups_layoutH1_text2.setStyleSheet('color: rgb(255, 25, 25);')
    groups_layoutH1_text3 = QLabel('Past Simple')
    groups_layoutH1_text3.setFont(bold_font)
    groups_layoutH1_text3.setStyleSheet('color: rgb(255, 25, 25);')
    groups_layoutH1_text4 = QLabel('Past Participle')
    groups_layoutH1_text4.setFont(bold_font)
    groups_layoutH1_text4.setStyleSheet('color: rgb(255, 25, 25);')

    groups_layoutH1_texts_list = [groups_layoutH1_text1, groups_layoutH1_text2, groups_layoutH1_text3,
                                  groups_layoutH1_text4]

    for groups_layoutH1_text in groups_layoutH1_texts_list:
        group_layoutH1.addWidget(groups_layoutH1_text, alignment=Qt.AlignVCenter | Qt.AlignHCenter)

    group_layoutV1.addLayout(group_layoutH1)

    for i in range(1, words + 1):
        group_layoutH = QHBoxLayout()

        group_layoutH_text1 = QLabel(group_dict[i]['rus'])
        group_layoutH_text1.setFont(main_font)
        group_layoutH_text1.setStyleSheet('color: rgb(25, 200, 25);')

        group_layoutH_texts_list = [group_layoutH_text1]

        for q in range(1, 4):
            group_layoutH_text = QLabel(group_dict[i][q])
            group_layoutH_text.setFont(main_font)

            group_layoutH_texts_list.append(group_layoutH_text)

        for group_layoutH_text in group_layoutH_texts_list:
            group_layoutH.addWidget(group_layoutH_text, alignment=Qt.AlignVCenter | Qt.AlignHCenter)

        group_layoutV1.addLayout(group_layoutH)

    group_main_layout.addLayout(group_layoutV1)

    group.setLayout(group_main_layout)

    layoutH1or2.addWidget(group)


# start group_all
group_all = QGroupBox('First = Second = Third')
group_all.setFont(group_font)
group_all_main_layout = QHBoxLayout()
group_all_layoutV1 = QVBoxLayout()
group_all_layoutH1 = QHBoxLayout()

group_all_dict = {
    1: {
        'rus': 'Окружать',
        1: 'beset',
        2: 'beset',
        3: 'beset'
    },
    2: {
        'rus': 'Предлагать',
        1: 'bid',
        2: 'bid',
        3: 'bid'
    },
    3: {
        'rus': 'Взрываться',
        1: 'burst',
        2: 'burst',
        3: 'burst'
    },
    4: {
        'rus': 'Бросать',
        1: 'cast',
        2: 'cast',
        3: 'cast'
    },
    5: {
        'rus': 'Стоить',
        1: 'cost',
        2: 'cost',
        3: 'cost'
    },
    6: {
        'rus': 'Резать',
        1: 'cut',
        2: 'cut',
        3: 'cut'
    },
    7: {
        'rus': 'Прогнозировать',
        1: 'forecast',
        2: 'forecast',
        3: 'forecast'
    },
    8: {
        'rus': 'Нагружать',
        1: 'fraught',
        2: 'fraught',
        3: 'fraught'
    },
    9: {
        'rus': 'Ударять',
        1: 'hit',
        2: 'hit',
        3: 'hit'
    },
    10: {
        'rus': 'Ранить',
        1: 'hurt',
        2: 'hurt',
        3: 'hurt'
    },
    11: {
        'rus': 'Вставлять',
        1: 'inset',
        2: 'inset',
        3: 'inset'
    },
    12: {
        'rus': 'Разрешать',
        1: 'let',
        2: 'let',
        3: 'let'
    }
}

make_group(group_all, group_all_main_layout, group_all_layoutH1, group_all_layoutV1, group_all_dict, layoutV1, 12)
# finish group_all
button_all = QPushButton('↑↑↑Проверить себя по этой карточке↑↑↑')
button_all.setFont(group_font)
layoutV1.addWidget(button_all)
# start group_i_a_u
group_none_a_u = QGroupBox('..., -a-, -u-')
group_none_a_u.setFont(group_font)
group_group_none_a_u_a_u_main_layout = QHBoxLayout()
group_group_none_a_u_a_u_layoutV1 = QVBoxLayout()
group_group_none_a_u_a_u_layoutH1 = QHBoxLayout()

group_group_none_a_u_a_u_dict = {
    1: {
        'rus': 'Начинать',
        1: 'begin',
        2: 'began',
        3: 'begun'
    },
    2: {
        'rus': 'Пить',
        1: 'drink',
        2: 'drank',
        3: 'drunk'
    },
    3: {
        'rus': 'Обгонять',
        1: 'outrun',
        2: 'outran',
        3: 'outrun'
    },
    4: {
        'rus': 'Захватывать',
        1: 'overrun',
        2: 'overran',
        3: 'overrun'
    },
    5: {
        'rus': 'Перезапускать',
        1: 'rerun',
        2: 'reran',
        3: 'rerun'
    },
    6: {
        'rus': 'Звонить',
        1: 'ring',
        2: 'rang',
        3: 'rung'
    },
    7: {
        'rus': 'Бегать',
        1: 'run',
        2: 'ran',
        3: 'run'
    },
    8: {
        'rus': 'Сокращать',
        1: 'shrink',
        2: 'shrank',
        3: 'shrunk'
    },
    9: {
        'rus': 'Петь',
        1: 'sing',
        2: 'sang',
        3: 'sung'
    },
    10: {
        'rus': 'Тонуть',
        1: 'sink',
        2: 'sank',
        3: 'sunk'
    },
    11: {
        'rus': 'Прыгать',
        1: 'spring',
        2: 'sprang',
        3: 'sprung'
    },
    12: {
        'rus': 'Вонять',
        1: 'stink',
        2: 'stank',
        3: 'stunk'
    }
}

make_group(group_none_a_u, group_group_none_a_u_a_u_main_layout, group_group_none_a_u_a_u_layoutH1,
           group_group_none_a_u_a_u_layoutV1, group_group_none_a_u_a_u_dict, layoutV1, 12)
# finish group_i_a_u
button_none_a_u = QPushButton('↑↑↑Проверить себя по этой карточке↑↑↑')
button_none_a_u.setFont(group_font)
layoutV1.addWidget(button_none_a_u)
# start group_e_o_en
group_none_o_en = QGroupBox('..., -o-, -en')
group_none_o_en.setFont(group_font)
group_none_o_en_main_layout = QHBoxLayout()
group_none_o_en_layoutV1 = QVBoxLayout()
group_none_o_en_layoutH1 = QHBoxLayout()

group_none_o_en_dict = {
    1: {
        'rus': 'Просыпаться',
        1: 'awake',
        2: 'awoke',
        3: 'awoken'
    },
    2: {
        'rus': 'Рождаться',
        1: 'beget',
        2: 'begot',
        3: 'begotten'
    },
    3: {
        'rus': 'Ломать',
        1: 'break',
        2: 'broke',
        3: 'broken'
    },
    4: {
        'rus': 'Выбирать',
        1: 'choose',
        2: 'chose',
        3: 'chosen'
    },
    5: {
        'rus': 'Забывать',
        1: 'forget',
        2: 'forgot',
        3: 'forgotten'
    },
    6: {
        'rus': 'Замораживать',
        1: 'freeze',
        2: 'froze',
        3: 'frozen'
    },
    7: {
        'rus': 'Получать',
        1: 'get',
        2: 'got',
        3: 'gotten'
    },
    8: {
        'rus': 'Оговариваться',
        1: 'misspeak',
        2: 'misspoke',
        3: 'misspoken'
    },
    9: {
        'rus': 'Говорить',
        1: 'speak',
        2: 'spoke',
        3: 'spoken'
    },
    10: {
        'rus': 'Воровать',
        1: 'steal',
        2: 'stole',
        3: 'stolen'
    },
    11: {
        'rus': 'Шагать',
        1: 'tread',
        2: 'trode',
        3: 'troden'
    },
    12: {
        'rus': 'Размораживать',
        1: 'unfreeze',
        2: 'unfroze',
        3: 'unfrozen'
    }
}

make_group(group_none_o_en, group_none_o_en_main_layout, group_none_o_en_layoutH1, group_none_o_en_layoutV1,
           group_none_o_en_dict,
           layoutV2, 12)
# finish group_i_o_en
button_i_o_en = QPushButton('↑↑↑Проверить себя по этой карточке↑↑↑')
button_i_o_en.setFont(group_font)
layoutV2.addWidget(button_i_o_en)
# start group_none_ught_ught

group_none_ught_ught = QGroupBox('..., -ught, -ught')
group_none_ught_ught.setFont(group_font)
group_none_ught_ught_main_layout = QHBoxLayout()
group_none_ught_ught_layoutV1 = QVBoxLayout()
group_none_ught_ught_layoutH1 = QHBoxLayout()

group_none_ught_ught_dict = {
    1: {
        'rus': 'Приносить',
        1: 'bring',
        2: 'brought',
        3: 'brought'
    },
    2: {
        'rus': 'Покупать',
        1: 'buy',
        2: 'bought',
        3: 'bought'
    },
    3: {
        'rus': 'Ловить',
        1: 'catch',
        2: 'caught',
        3: 'caught'
    },
    4: {
        'rus': 'Бороться',
        1: 'fight',
        2: 'fought',
        3: 'fought'
    },
    5: {
        'rus': 'Перебороть',
        1: 'outfight',
        2: 'outfought',
        3: 'outfought'
    },
    6: {
        'rus': 'Переобучать',
        1: 'reteach',
        2: 'retaught',
        3: 'retaught'
    },
    7: {
        'rus': 'Переосмлысливать',
        1: 'rethink',
        2: 'rethought',
        3: 'rethought'
    },
    8: {
        'rus': 'Искать',
        1: 'seek',
        2: 'sought',
        3: 'sought'
    },
    9: {
        'rus': 'Преподавать',
        1: 'teach',
        2: 'taught',
        3: 'taught'
    },
    10: {
        'rus': 'Думать',
        1: 'think',
        2: 'thought',
        3: 'thought'
    },
    11: {
        'rus': 'Недооценивать',
        1: 'underbuy',
        2: 'underbought',
        3: 'underbought'
    },
    12: {
        'rus': 'Отучивать',
        1: 'unteach',
        2: 'untaught',
        3: 'untaught'
    }
}

make_group(group_none_ught_ught, group_none_ught_ught_main_layout, group_none_ught_ught_layoutH1,
           group_none_ught_ught_layoutV1, group_none_ught_ught_dict, layoutV2, 12)
# finish group_none_ught_ught
button_none_ught_ught = QPushButton('↑↑↑Проверить себя по этой карточке↑↑↑')
button_none_ught_ught.setFont(group_font)
layoutV2.addWidget(button_none_ught_ught)

main_layout.addLayout(layoutV1)
main_layout.addLayout(layoutV2)

main_window.setLayout(main_layout)


def after_click(listq, Question):
    group_all.hide()
    group_none_a_u.hide()
    group_none_o_en.hide()
    group_none_ught_ught.hide()

    button_all.hide()
    button_none_a_u.hide()
    button_i_o_en.hide()
    button_none_ught_ught.hide()

    main_layoutH = QHBoxLayout()

    font = QFont('Arial', 18)
    group_font = QFont('Arial', 8)
    question_font = QFont('Arial', 23)

    past_questions = list()

    question = QLabel('Question')
    question.setFont(question_font)
    question.setStyleSheet('color: rgb(255, 25, 25);')
    button_reply = QPushButton('Ответить')
    button_reply.setFont(font)

    first_answer = QRadioButton('First')
    first_answer.setFont(font)
    second_answer = QRadioButton('Second')
    second_answer.setFont(font)
    third_answer = QRadioButton('Third')
    third_answer.setFont(font)
    fourth_answer = QRadioButton('Fourth')
    fourth_answer.setFont(font)

    radiogroup_answers = QButtonGroup()
    radiogroup_answers.addButton(first_answer)
    radiogroup_answers.addButton(second_answer)
    radiogroup_answers.addButton(third_answer)
    radiogroup_answers.addButton(fourth_answer)

    group_answers = QGroupBox('Варинты ответов')
    group_answers.setFont(group_font)

    group_main_layout = QHBoxLayout()

    group_layoutV1 = QVBoxLayout()
    group_layoutV2 = QVBoxLayout()

    group_layoutV1.addWidget(first_answer, alignment=Qt.AlignVCenter | Qt.AlignHCenter)
    group_layoutV1.addWidget(second_answer, alignment=Qt.AlignVCenter | Qt.AlignHCenter)

    group_layoutV2.addWidget(third_answer, alignment=Qt.AlignCenter)
    group_layoutV2.addWidget(fourth_answer, alignment=Qt.AlignCenter)

    group_main_layout.addLayout(group_layoutV1)
    group_main_layout.addLayout(group_layoutV2)

    group_answers.setLayout(group_main_layout)

    layoutH1 = QHBoxLayout()
    layoutH2 = QHBoxLayout()
    layoutHgroup = QHBoxLayout()

    layoutH1.addWidget(question, alignment=Qt.AlignCenter)

    layoutH2.addWidget(button_reply)

    layoutHgroup.addWidget(group_answers)

    main_window.setLayout(main_layoutH)

    group_result = QGroupBox('Результат теста')
    group_result.setFont(group_font)

    group_result_main_layout = QVBoxLayout()

    win_lose = QLabel('Правильно/Неправильно')
    win_lose.setFont(font)
    victory_text = QLabel('Правильный вариант ответа')
    victory_text.setFont(font)

    group_result_main_layout.addWidget(win_lose, alignment=Qt.AlignLeft)
    group_result_main_layout.addWidget(victory_text, alignment=Qt.AlignHCenter)

    layoutHgroup.addWidget(group_result)

    group_result.setLayout(group_result_main_layout)

    main_layout.addLayout(layoutH1)
    main_layout.addLayout(layoutHgroup)
    main_layout.addLayout(layoutH2)

    group_result.hide()

    def show_question():
        group_result.hide()
        group_answers.show()

        radiogroup_answers.setExclusive(False)
        first_answer.setChecked(False)
        second_answer.setChecked(False)
        third_answer.setChecked(False)
        fourth_answer.setChecked(False)
        radiogroup_answers.setExclusive(True)

        button_reply.setText('Ответить')

    def show_result():
        group_answers.hide()
        group_result.show()

        if len(past_questions) == len(listq):
            button_reply.setText('Показать результат проверки')
        else:
            button_reply.setText('Следующий вопрос')

    answers = [first_answer, second_answer, third_answer, fourth_answer]

    def ask(new_question: Question):
        shuffle(answers)
        answers[0].setText(new_question.right)
        answers[1].setText(new_question.wrong1)
        answers[2].setText(new_question.wrong2)
        answers[3].setText(new_question.wrong3)
        question.setText(new_question.class_question)
        victory_text.setText(new_question.right)
        show_question()

    def next_question():
        main_window.total += 1

        cur_questions = randint(0, len(listq) - 1)

        while True:
            if not (cur_questions in past_questions):
                break
            else:
                cur_questions = randint(0, len(listq) - 1)

        past_questions.append(cur_questions)

        new_question = listq[cur_questions]
        ask(new_question)

    wrong_answers = list()
    right_wrong_answer = list()

    def check_answer():
        if answers[0].isChecked():
            show_correct('Верно!')
            main_window.score += 1
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно...')
            if answers[1].isChecked():
                wrong_answers.append(answers[1].text())
            elif answers[2].isChecked():
                wrong_answers.append(answers[2].text())
            elif answers[3].isChecked():
                wrong_answers.append(answers[3].text())

            right_wrong_answer.append(answers[0])

    def click_OK():
        if button_reply.text() == 'Ответить':
            check_answer()
        elif button_reply.text() == 'Следующий вопрос':
            next_question()
        elif button_reply.text() == 'Показать результат проверки':
            question.setText('Результат')
            group_result.setTitle('Результат')

            win_lose.hide()
            victory_text.hide()

            result_text1 = QLabel('Количество вопросов:\n' + str(main_window.total))
            result_text1.setFont(font)
            result_text1.setStyleSheet('color: rgb(0, 150, 0);')
            group_result_main_layout.addWidget(result_text1, alignment=Qt.AlignVCenter | Qt.AlignHCenter)
            result_text2 = QLabel('Количество правильных ответов:\n' + str(main_window.score))
            result_text2.setFont(font)
            result_text2.setStyleSheet('color: rgb(0, 150, 0);')
            group_result_main_layout.addWidget(result_text2, alignment=Qt.AlignVCenter | Qt.AlignHCenter)
            result_text3 = QLabel(
                'Количество неправильных ответов:\n' + str(main_window.total - main_window.score) + '\n')
            result_text3.setFont(font)
            result_text3.setStyleSheet('color: rgb(0, 150, 0);')
            group_result_main_layout.addWidget(result_text3, alignment=Qt.AlignVCenter | Qt.AlignHCenter)
            result_text4 = QLabel('Рейтинг:\n' + str(round((main_window.score / main_window.total * 100), 2)) + '%')
            result_text4.setFont(font)
            result_text4.setStyleSheet('color: rgb(0, 150, 0);')
            group_result_main_layout.addWidget(result_text4, alignment=Qt.AlignVCenter | Qt.AlignHCenter)

            button_reply.setText('Вернуться на Главную страницу')
        elif button_reply.text() == 'Вернуться на Главную страницу':
            question.hide()
            group_result.hide()
            button_reply.hide()

            group_all.show()
            group_none_a_u.show()
            group_none_o_en.show()
            group_none_ught_ught.show()

            button_all.show()
            button_none_a_u.show()
            button_i_o_en.show()
            button_none_ught_ught.show()

    def show_correct(result):
        win_lose.setText(result)
        show_result()

    button_reply.clicked.connect(click_OK)

    main_window.total = 0
    main_window.score = 0

    next_question()


def class_question():
    class Question():
        def __init__(self, question, right, wrong1, wrong2, wrong3):
            self.class_question = question
            self.right = right
            self.wrong1 = wrong1
            self.wrong2 = wrong2
            self.wrong3 = wrong3

    return Question


def after_click_all():
    class_question()

    Question = class_question()

    listq = []
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'beset - beset - beset\n(Окружать)', 'beset - bezet - beseten\n(Окружать)',
        'beset - beseted - beset\n(Окружать)', 'beset - beseted - beseten\n(Окружать)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'bid - bid - bid\n(Предлагать)', 'bid - bad - bud\n(Предлагать)', 'bid - bided - biden\n(Предлагать)',
        'bid - bed - boght\n(Предлагать)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'burst - burst - burst\n(Взрываться)', 'burst - bursted - bursten\n(Взрываться)',
        'burst - birst - barst\n(Взрываться)', 'burst - bursted - borst\n(Взрываться)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'cast - cast - cast\n(Бросать)', 'cast - cost - cost\n(Бросать)', 'cast - casted - casten\n(Бросать)',
        'cast - cast - cost\n(Бросать)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'cost - cost - cost\n(Стоить)', 'cost - costed - costen\n(Стоить)', 'cost - cast - cost\n(Стоить)',
        'cost - costed - cast\n(Стоить)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'forecast - forecast -\nforecast\n(Прогнозировать)', 'forecast - forecasted -\nforecasten\n(Прогнозировать)',
        'forecast - forecost -\nforecast\n(Прогнозировать)', 'forecast - forecost -\nforecost\n(Прогнозировать)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'fraught - fraught - fraight\n(Нагружать)', 'fraught - fraughted - fraughten\n(Нагружать)',
        'fraught - frought - fraught\n(Нагружать)', 'fraught - fraughted - frought\n(Нагружать)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'hit - hit - hit\n(Ударять)', 'hit - hitted - hitten\n(Ударять)', 'hit - hat - hut\n(Ударять)',
        'hit - hut - hitten\n(Ударять)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'hurt - hurt - hurt\n(Ранить)', 'hurt - hurted - hurten\n(Ранить)', 'hurt - hirt - hart\n(Ранить)',
        'hurt - hurted - hirt\n(Ранить)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'inset - inset - inset\n(Вставлять)', 'inset - inseted - inseten\n(Вставлять)',
        'inset - insot - insut\n(Вставлять)',
        'inset - insut - inset\n(Вставлять)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'cut - cut - cut\n(Резать)', 'cut - cutted - cutten\n(Резать)', 'cut - cot - cotten\n(Резать)',
        'cut - cot - cut\n(Резать)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'let - let - let\n(Разрешать)', 'let - letted - letten\n(Разрешать)', 'let - lat - lut\n(Разрешать)',
        'let - let - lot\n(Разрешать)'))

    after_click(listq, Question)


def after_click_none_a_u():
    class_question()

    Question = class_question()

    listq = []
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'begin - began - begun\n(Начинать)', 'begin - begun - began\n(Начинать)', 'begin - begined - began\n(Начинать)',
        'begin - began - beginen\n(Начинать)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'drink - drank - drunk\n(Пить)', 'drink - drunk - drank\n(Пить)', 'drink - drinked - drink\n(Пить)',
        'drink - drink - drink\n(Пить)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'ring - rang - rung\n(Звонить)', 'ring - ringed - ringen\n(Звонить)', 'ring - rung - rang\n(Звонить)',
        'ring - ringed - ring\n(Звонить)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'shrink - shrank - shrunk\n(Сжимать)', 'shrink - shrinked - shriken\n(Сжимать)',
        'shrink - shrunk - shrank\n(Сжимать)',
        'shrink - shrinked - shrunk\n(Сжимать)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'sing - sang - sung\n(Петь)', 'sing - sung - sang\n(Петь)', 'sing - singed - singen\n(Петь)',
        'sing - sung - singen\n(Петь)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'sink - sank - sunk\n(Тонуть)', 'sink - sunk - sank\n(Тонуть)', 'sink - sinked - sinken\n(Тонуть)',
        'sink - sank - sinken\n(Тонуть)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'spring - sprang - sprung\n(Прыгать)', 'spring - sprung - sprang\n(Прыгать)',
        'spring - springed - springen\n(Прыгать)',
        'spring - springed - spring\n(Прыгать)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'stink - stank - stunk\n(Вонять)', 'stink - stunk - stank\n(Вонять)', 'stink - stinked - stinken\n(Вонять)',
        'stink - stank - stink\n(Вонять)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'outrun - outran - outrun\n(Обгонять)', 'outrun - outrunned - outrunnen\n(Обгонять)',
        'outrun - outrun - outran\n(Обгонять)',
        'outrun - outron - outronnen\n(Обгонять)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'overrun - overran -\noverrun\n(Захватывать)', 'overun - overrunned -\noverrunnen\n(Захватывать)',
        'overrun - overron -\noverronnen\n(Захватывать)', 'overrun - overrought -\noverrouht\n(Захватывать)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'rerun - rerun - rerun\n(Перезапускать)', 'rerun - rerunned - rerunnen\n(Перезапускать)',
        'rerun - reron - reronen\n(Перезапускать)',
        'rerun - rerought - rerought\n(Перезапускать)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'run - ran - run\n(Бегать)', 'run - runned - runnen\n(Бегать)', 'run - rought - rought\n(Бегать)',
        'run - ron - ronnen\n(Бегать)'))

    after_click(listq, Question)


def after_click_none_o_en():
    class_question()

    Question = class_question()

    listq = []
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'awake - awoke - awoken\n(Просыпаться)', 'awake - awake - awake\n(Просыпаться)', 'awake - awaked - awaken\n('
                                                                                         'Просыпаться)',
        'awake - awake - awuke\n(Просыпаться)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'beget - begot - begotten\n(Рождаться)', 'beget - begetted - begetten\n(Рождаться)',
        'beget - begat - begut\n(Рождаться)',
        'beget - begought - begought\n(Рождаться)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'break - broke - broken\n(Ломать)', 'break - break - break\n(Ломать)', 'break - brought - brought\n(Ломать)',
        'break - breaked - breaken\n(Ломать)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'choose - chose - chosen\n(Выбирать)', 'choose - choosed - choosen\n(Выбирать)',
        'choose - choose - choose\n(Выбирать)',
        'choose - chase - chuse\n(Выбирать)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'forget - forgot - forgotten\n(Забывать)', 'forget - forgought - forgought\n(Забывать)',
        'forget - forgat - forgut\n(Забывать)',
        'forget - forget - forget\n(Забывать)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'freeze - froze - frozen\n(Замораживать)', 'freeze - freeze - freeze\n(Замораживать)',
        'freeze - freezed - freezen\n(Замораживать)',
        'freeze - fraze - fruze\n(Замораживать)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'get - got - gotten\n(Получать)', 'get - getted - getten\n(Получать)', 'get - gat - gut\n(Получать)',
        'get - get - get\n(Получать)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'misspeak - missproke -\nmisspoken\n(Оговариваться)', 'misspeak - misspought -\nmisspought\n(Оговариваться)',
        'misspeak - misspeak -\nmissspeak\n(Оговариваться)', 'misspeak - misspake -\nmisspuke\n(Оговариваться)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'speak - spoke - spoken\n(Говорить)', 'speak - speak - speak\n(Говорить)',
        'speak - spought - spught\n(Говорить)',
        'speak - spake - spuke\n(Говорить)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'steal - stole - stolen\n(Воровать)', 'steal - stealed - stealen\n(Воровать)',
        'steal - stale - stale\n(Воровать)',
        'steal - steal - steal\n(Воровать)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'tread - trode - troden\n(Шагать)', 'tread - tread - tread\n(Шагать)', 'tread - treaded - treaden\n(Шагать)',
        'tread - trade - trude\n(Шагать)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'unfreeze - unfroze -\nunfrozen\n(Размораживать)', 'unfreeze - unfreeze -\nunfreeze\n(Размораживать)',
        'unfreeze - unfreezed -\nunfreezen\n(Размораживать)', 'unfreeze - unfraze -\nunfruze\n(Размораживать)'))

    after_click(listq, Question)


def after_click_none_ught_ught():
    class_question()

    Question = class_question()

    listq = []
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'bring - broght - brought\n(Приносить)', 'bring - bring - bring\n(Приносить)',
        'bring - brang - brung\n(Приносить)',
        'bring - brong - bringen\n(Приносить)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'buy - bought - bought\n(Покупать)', 'buy - buy - bought\n(Покупать)', 'buy - bought - buy\n(Покупать)',
        'buy - buyed - buyen\n(Покупать)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'catch - caught - caught\n(Ловить)', 'catch - catch - catch\n(Ловить)', 'catch - caught - catchen\n(Ловить)',
        'catch - catched - catchen\n(Ловить)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'fight - fought - fought\n(Бороться)', 'fight - fight - fought\n(Бороться)',
        'fight - fought - fight\n(Бороться)',
        'fight - fighted - fighten\n(Бороться)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'outfight - outfought -\noutfought\n(Перебороть)', 'outfight - outfight -\noutfight\n(Перебороть)',
        'outfight - outfight -\noutfoght\n(Перебороть)', 'outfight - outfought -\noutfight\n(Перебороть)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'reteach - retaught - retaught\n(Переобучать)', 'reteach - retaught - reteach\n(Переобучать)',
        'reteach - reteach - retaught\n(Переобучать)', 'retech - reteached - reteachen\n(Переобучать)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'seek - sought - sought\n(Искать)', 'seek - seek - seek\n(Искать)', 'seek - sought - seek\n(Искать)',
        'seek - seek - sought\n(Искать)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'teach - taught - taught\n(Преподавать)', 'teach - taught - teach\n(Преподавать)',
        'teach - teach - taught\n(Преподавать)', 'teach - teached - teachen\n(Преподавать)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'think - thought - thought\n(Думать)', 'think - think - think\n(Думать)', 'think - thank - thunk\n(Думать)',
        'think - think - thought\n(Думать)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'unteach - untaught -\nuntaught\n(Отучивать)', 'unteach - untaught -\nunteach\n(Отучивать)',
        'unteach - unteach -\nuntaught\n(Отучивать)', 'unteach - unteached -\nunteachen\n(Отучивать)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'rethink - rethought -\nrethought\n(Переосмысливать)', 'rethink - rethinked -\nrethinked\n(Переосмысливать)',
        'rethink - rethink -\nrethink\n(Переосмысливать)', 'rethink - rethonk -\nrethonken\n(Переосмысливать)'))
    listq.append(Question(
        'Выберите верное\nсоставление\nтрёх форм неправильных\nглаголов (Infinitive -\nPast Simple - Past Participle)',
        'underbuy - underbought -\nunderbought\n(Недооценивать)',
        'underbuy - underbuyed -\nunderbuyen\n(Недооценивать)',
        'underbuy - ubderbuy -\nunderbuy\n(Недооценивать)', 'underbuy - underbuyed -\nunderbuy\n(Недооценивать)'))

    after_click(listq, Question)


button_all.clicked.connect(after_click_all)
button_none_a_u.clicked.connect(after_click_none_a_u)
button_i_o_en.clicked.connect(after_click_none_o_en)
button_none_ught_ught.clicked.connect(after_click_none_ught_ught)

main_window.show()
app.exec_()
