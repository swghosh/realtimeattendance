from flask import Flask, request, jsonify

app = Flask(__name__)

import csv, io

@app.route('/api/students')
def list_students():
    return "Not Implemented"

@app.route('/api/attendance/mark', methods = ['POST'])
def mark_attendance():
    return "Not Implemented"

@app.route('/api/attendance/export.csv')
def export_attendance():
    sio = io.StringIO()
    writer = csv.DictWriter(sio, fieldnames=['name', 'phone'])
    writer.writeheader()
    writer.writerow({'name': 'Swarup Ghosh', 'phone': 891517827})
    writer.writerow({'name': 'Naman Sharma', 'phone': 891517828})
    return sio.getvalue()

if __name__ == '__main__':
    app.run(debug=True)