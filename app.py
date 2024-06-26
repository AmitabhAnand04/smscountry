from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/sms", methods=['POST'])
def incoming_sms():
    """Handle incoming SMS messages"""
    # Log the entire request for debugging purposes
    print('Incoming request:')
    print(request.values)
    
    # Accessing form data
    mn = request.values.get('mobilenumber')
    msg = request.values.get('message')
    reeivedTime = request.values.get('received')
    
    # Process the data as needed
    print("Mobile number:", mn)
    print("Message:", msg)
    print("Message Time:", reeivedTime)
    
    # Return a 200 OK response code
    return jsonify({'status': 'Message received'}), 200

@app.route('/')
def hello_world():
    return 'Hello, World! This is my Flask app.'
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
