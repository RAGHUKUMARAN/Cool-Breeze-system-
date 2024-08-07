from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def create_table():
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            mobile_number TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

create_table()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/buy_now', methods=['GET', 'POST'])
def buy_now():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        mobile_number = request.form['mobile_number']

    
        conn = sqlite3.connect('user_data.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, address, mobile_number) VALUES (?, ?, ?)',
                       (name, address, mobile_number))
        conn.commit()
        conn.close()

        return redirect(url_for('home'))

    return render_template('buy_now.html')

@app.route('/free_trial', methods=['GET', 'POST'])
def free_trial():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        mobile_number = request.form['mobile_number']

        conn = sqlite3.connect('user_data.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, address, mobile_number) VALUES (?, ?, ?)',
                       (name, address, mobile_number))
        conn.commit()
        conn.close()

        return redirect(url_for('home'))

    return render_template('free_trial.html')

if __name__ == '__main__':
    app.run(debug=True)
