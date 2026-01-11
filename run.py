from flask import Flask, render_template, request
from admin import Admin
from passengerinfo import PassengerDataCsv
from TicketShow import TicketShow

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    admin = Admin()
    username = request.form['username']
    password = request.form['password']

    if admin.adminLoginWeb(username, password):
        return render_template('passenger.html')
    else:
        return "Invalid Login"

@app.route('/registerPassenger', methods=['POST'])
def registerPassenger():
    p = PassengerDataCsv()
    p.passengerName = request.form['name']
    p.noOfPassenger = request.form['count']
    p.departureLocation = request.form['from']
    p.destinationLocation = request.form['to']
    p.selectBusType = request.form['bus']
    p.busFare = int(p.noOfPassenger) * (500 if p.selectBusType == "AC" else 300)
    p.saveInfo()
    return "Passenger Registered Successfully"

@app.route('/ticket', methods=['POST'])
def ticket():
    booking_id = request.form['booking_id']
    return TicketShow().ticketShowWeb(booking_id)

if __name__ == '__main__':
    app.run(debug=True)
3