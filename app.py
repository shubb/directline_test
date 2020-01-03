from flask import Flask, jsonify
from services.number_list_provider import get_list_of_numbers

app = Flask(__name__)

@app.route('/total')
def total():
    """Return the total sum of the list of numbers
       from the List Of Numbers service"""
    
    total = sum(get_list_of_numbers())
    return jsonify(total=total)

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5000)