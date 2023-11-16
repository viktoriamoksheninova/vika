import sqlite3
from random import randint

db_name = 'quiz.sqlite'
conn = None
cursor = None

def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

def close():
    cursor.close()
    conn.close()

def do(query):
    cursor.execute(query)
    conn.commit()

def clear_db():
    ''' удаляет все таблицы '''
    open()
    query = '''DROP TABLE IF EXISTS quiz_content'''
    do(query)
    query = '''DROP TABLE IF EXISTS questions'''
    do(query)
    query = '''DROP TABLE IF EXISTS quiz'''
    do(query)
    close()

def create():
    open()
    cursor.execute('''PRAGMA foreign_keys=on''')

    do('''CEATE TABLE IF NOT EXISTS quiz (
            id INTEGER PRIMARY KEY, 
            name VARCHAR)''')

    do('''CEATE TABLE IF NOT EXISTS question(
            id INTEGER PRIMARY KEY,
            question VARCHAR,
            answer VARCHAR,
            wrong1 VARCHAR,
            wrong2 VARCHAR,
            wrong3 VARCHAR)''')

    do('''CEATE TABLE IF NOT EXISTS quiz_content(
            id INTEGER PRIMARY KEY,
            quiz_id INTEGER,
            question_id INTEGER,
            FOREIGN KEY (quiz_id) REFERENCES quiz (id),
            FOREIGN KEY (question_id) REFERENCES question (id))''')

    close()

def add_questions():
    questions = [
        ('Сколько месяцев в году имеют 28 дней?', 'Все', 'Один', 'Ни одного', 'Два'),
        ('Каким станет зеленый утес, если упадет в Красное море?', 'Мокрым', 'Красным', 'Не изменится', 'Фиолетовым'),
        ('Какой рукой лучше размешивать чай?', 'Ложкой', 'Правой', 'Левой', 'Любой'),
        ('Что не имеет длины, глубины, ширины, высоты, а можно измерить?', 'Время', 'Глупость', 'Море', 'Воздух'),
        ('Когда сетью можно вытянуть воду?', 'Когда вода замерзла', 'Когда нет рыбы', 'Когда уплыла золотая рыбка', 'Когда сеть порвалась'),
        ('Что больше слона и ничего не весит?', 'Тень слона', 'Воздушный шар', 'Парашют', 'Облако')
    ]
     
    open()
    cursor.executemany('''INSERT INTO question (question,answer,wrong1,wrong2,wrong3) VALUES (?,?,?,?,?)''',questions)
    conn.commit()
    close()

def add_quiz():
    quizes = [
        ('Своя игра', ),
        ('Кто хочет стать миллионером?', ),
        ('Самый умный', )
    ]

    open()
    cursor.executemany('''INSERT INTO quiz (name) VALUES (?)''',quizes )
    conn.commit()
    close()

def add_links():
    open()
    cursor.execute('''PRAGMA foreign_keys=on''')
    query = 'INSERT INTO quiz_content (quiz_id,question_id) VALUES (?,?)'
    answer = input('Добавить связь (y/n)?')
    while answer != 'n':
        quiz_id = int(input('id векторины:'))
        question_id = int(input('id вопросы:'))
        cursor.execute(query,[quiz_id,question_id])
        conn.commit()
        answer = input('Добавить связь (y/n)?')
    close()

def show(table):
    query = 'SELECT * FROM ' + table
    open()
    cursor.execute(query)
    print(cursor.fetchall())
    close()

def show_tables():
    show('question')
    show('quiz')
    show('quiz_content')

def get_question_after(question_id = 0,quiz_id = 1):
    open()
    query = '''
    SELECT quiz_content.id,question.question,question.answer,question.wrong1,question.wrong2,question.wrong3
    FROM question,quiz_content
    WHERE quiz_content.question_id == question.id
    AND quiz_content > ? AND quiz_content.quiz_id == ?
    ORDER BY quiz_content.id'''
    cursor.execute(query,[last_id,vict_id])
    result = cursor.fetchone()
    close()
    return result

def main():
    clear_db()
    create()
    add_questions()
    add_quiz()
    add_links()
    show_tables()

if __name__ == "__main__":
    main()
