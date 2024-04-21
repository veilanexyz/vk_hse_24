from flask import Flask, render_template,request, redirect, url_for
import re
from utils.parsing import parsePageArticles
import sqlite3

app = Flask(__name__)

URL_REGEX = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prediction', methods=['POST'])
def print_input():
    conn = sqlite3.connect('database.db')
    prompt = request.form.get('prompt')
    if 'http' in prompt:
        conn.execute("INSERT INTO content (link, timestampdata) VALUES (?, DATETIME('now'))", (prompt,))
    else:
        conn.execute("INSERT INTO content (text, timestampdata) VALUES (?, DATETIME('now'))", (prompt,))
    conn.commit()
    conn.close()
    if URL_REGEX.match(prompt):
        return parsePageArticles(prompt)
    else:
        return render_template('prediction.html')

@app.route('/button_clicked', methods=['POST'])
def button_clicked():
    conn = sqlite3.connect('database.db')
    prompt = request.form.get('prompt')
    if 'http' in prompt:
        conn.execute("INSERT INTO content (link, timestampdata) VALUES (?, DATETIME('now'))", (prompt,))
    else:
        conn.execute("INSERT INTO content (text, timestampdata) VALUES (?, DATETIME('now'))", (prompt,))
    conn.commit()
    conn.close()
        
    print("Кнопка была нажата!")
    return render_template('new_page.html')
    
if __name__ == '__main__':
    app.run(debug=True)
