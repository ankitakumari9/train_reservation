from flask import Flask, render_template, request, redirect
from database import Database

app = Flask(__name__)
db = Database()

@app.route('/')
def index():
    seats = db.get_seat_status()
    return render_template('index.html', seats=seats)

@app.route('/reserve', methods=['POST'])
def reserve():
    num_seats = int(request.form['num_seats'])
    reserved = db.reserve_seats(num_seats)
    if reserved:
        message = f"Successfully reserved {num_seats} seats."
    else:
        message = "Not enough seats available."
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
