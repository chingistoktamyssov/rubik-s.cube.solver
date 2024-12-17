from flask import Flask, request, jsonify, send_from_directory
from rubik_solver import utils

app = Flask(__name__,
            static_url_path='', 
            static_folder='static')

# Define a function to map color names to cube notation (U, R, F, D, L, B)
def map_colors_to_notation(button_colors):
    # This is an example mapping of colors to cube sides
    color_map = {
        'white': 'U',
        'red': 'R',
        'green': 'F',
        'yellow': 'D',
        'orange': 'L',
        'blue': 'B'
    }
    
    # Convert the color list to the cube notation (54 characters)
    cube_state = ''.join([color_map[color] for color in button_colors])
    
    return cube_state

@app.route("/")
def index():
    return send_from_directory("static", 'index.html')

# Route to receive the buttonColors list
@app.route('/submit-colors', methods=['POST'])
def receive_colors():
    data = request.json  # Receive the JSON data sent from JavaScript
    button_colors = data.get('buttonColors', [])
    
    # Process the button_colors here (save to a file, database, etc.)
    print("Received buttonColors:", button_colors)

    cube_state = map_colors_to_notation(button_colors)
        
    # Solve the cube using rubik_solver
    solution = utils.solve(cube_state)
    print(solution)

    return jsonify({'status': 'success', 'message': 'Colors received and processed'})

if __name__ == '__main__':
    app.run(debug=True)