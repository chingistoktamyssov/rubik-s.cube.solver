from flask import Flask, request, jsonify, send_from_directory
import kociemba

app = Flask(__name__,
            static_url_path='', 
            static_folder='static')

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
    
    # Send a response back to JavaScript
    return jsonify({"message": "Colors received successfully", "status": "success"})

if __name__ == '__main__':
    app.run(debug=True)

# Map colors from the buttonColors array to the solver format
color_map = {
    "white": "U",  # Up face (White)
    "green": "F",  # Front face (Green)
    "red": "R",    # Right face (Red)
    "blue": "B",   # Back face (Blue)
    "orange": "L", # Left face (Orange)
    "yellow": "D"  # Down face (Yellow)
}

# A function that converts the buttonColors list into the format the solver expects
def convert_to_solver_format(buttonColors):
    # Mapping of buttonColors (54 items) to the solver's string (54 characters)
    solver_input = ""
    
    for color in buttonColors:
        solver_input += color_map[color]
        
    return solver_input

# Example buttonColors list (you should replace this with the actual list from the layout)
buttonColors = button_colors

# Convert the buttonColors to the string format expected by the solver
solver_input = convert_to_solver_format(buttonColors)

# Use the Kociemba solver to get the solution (a sequence of moves)
solution = kociemba.solve(solver_input)

print("Solution to the Rubik's Cube:")
print(solution)