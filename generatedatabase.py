import sqlite3


def generate_db():
    conn = sqlite3.connect('rasa.db')
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS booking")

    cursor.execute('''CREATE TABLE IF NOT EXISTS booking (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        booking_name TEXT,
        booking_date TEXT,
        booking_time TEXT,
        nb_people INTEGER,
        nb_phone TEXT
    )''')

    conn.commit()
    conn.close()


if __name__ == '__main__':
    generate_db()
