from flask import Flask, jsonify
from services.number_list_provider import get_list_of_numbers

app = Flask(__name__)

@app.route('/total')
def total():
    """Return the total sum of the list of numbers
       from the List Of Numbers service"""
    
    total = sum(get_list_of_numbers())
    return jsonify(total=total)