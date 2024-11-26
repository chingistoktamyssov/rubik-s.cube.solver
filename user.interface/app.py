from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to receive the buttonColors list
@app.route('/submit-colors', methods=['POST'])
def receive_colors():
    data = request.json  # Receive the JSON data sent from JavaScript
    button_colors = data.get('buttonColors', [])
    
    # Process the button_colors here (save to a file, database, etc.)
    print("Received buttonColors:", button_colors)
    
    # Send a response back to JavaScript
    return jsonify({"message": "Colors received successfully", "status": "success"})

if __name__ == '__main__':
    app.run(debug=True)