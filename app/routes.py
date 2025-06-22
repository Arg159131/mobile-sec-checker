from flask import Blueprint, request, jsonify, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
     return render_template('index.html')

@main.route('/check-number', methods=['POST'])
def check_number():
    data = request.get_json()
    number = data.get('number')

    # Mock logic — later you can connect this to an actual scanner or API
    if number.startswith('+91'):
        status = 'Indian number – might be vulnerable to SIM swap if not protected.'
    else:
        status = 'Unknown region – proceed with caution.'

    return jsonify({'number': number, 'status': status})
