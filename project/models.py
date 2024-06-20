import sqlite3
from ai_predictions import predict_num_of_spots

DATABASE = 'parking_management.db'

def connect_db():
    conn = sqlite3.connect(DATABASE)
    return conn

def init_db():
    with connect_db() as conn:
        conn.execute('''
        CREATE TABLE IF NOT EXISTS parking_spots (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            spot_number TEXT UNIQUE NOT NULL,
            occupied BOOLEAN NOT NULL
        )
        ''')
        conn.commit()

def add_examples():
    with connect_db() as conn:
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("A1", false)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("A2", false)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("A3", true)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("A4", false)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("A5", false)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("A6", true)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("A7", false)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("A8", false)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("A9", true)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("A10", false)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("A11", false)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("A12", true)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("B1", true)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("B2", true)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("B3", true)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("B4", true)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("B5", false)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("B6", true)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("B7", true)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("B8", false)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("B9", false)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("B10", true)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("B11", true)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("B12", true)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("C1", false)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("C2", true)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("C3", false)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("C4", false)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("C5", false)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("C6", false)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("C7", false)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("C8", true)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("C9", false)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("C10", false)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("C11", false)')
        conn.execute('INSERT INTO parking_spots (spot_number, occupied) VALUES ("C12", true)')
        conn.commit()

def get_all_parking_spots():
    with connect_db() as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM parking_spots')
        rows = cur.fetchall()
        spots = [{'id': row[0], 'spot_number': row[1], 'occupied': bool(row[2])} for row in rows]
    return spots

def add_parking_spot(spot_number, occupied):
    with connect_db() as conn:
        conn.execute(
            'INSERT INTO parking_spots (spot_number, occupied) VALUES (?, ?)',
            (spot_number, occupied)
        )
        conn.commit()

def remove_parking_spot(spot_number):
    with connect_db() as conn:
        conn.execute(
            'DELETE FROM parking_spots WHERE spot_number = ?',
            (spot_number,)
        )
        conn.commit()

def change_parking_spot(spot_number, occupied):
    with connect_db() as conn:
        conn.execute(
            'UPDATE parking_spots SET occupied = ? WHERE spot_number = ?',
            (occupied, spot_number)
        )
        conn.commit()

def check_parameters(day_of_week, hour, is_holiday):
    if day_of_week < 0 or day_of_week > 6 or hour < 0 or hour > 22 or is_holiday < 0 or is_holiday > 1:
        return False

    return True

def predict_availability(day_of_week, hour, is_holiday):
    prediction = predict_num_of_spots(
        day_of_week,
        hour,
        is_holiday
    )

    return prediction
