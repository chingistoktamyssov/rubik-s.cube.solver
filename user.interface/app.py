from flask import Flask, request, jsonify, send_from_directory
import twophase.solver as sv
import serial
import time

app = Flask(__name__,
            static_url_path='', 
            static_folder='static')

# Define a function to map color names to cube notation (U, R, F, D, L, B)
def map_colors_to_notation(button_colors):
    # This is an example mapping of colors to cube sides

    color_map = {
        'white': 'U',
        'red': 'F',
        'green': 'L',
        'yellow': 'D',
        'orange': 'B',
        'blue': 'R'
    }

    new_colors = []
    for i in range(9):
        new_colors.append(color_map[button_colors[i]])
    for i in [15, 27, 39]:
        for j in range(i, i+3):
            new_colors.append(color_map[button_colors[j]])
    for i in [12, 24, 36]:
        for j in range(i, i+3):
            new_colors.append(color_map[button_colors[j]])
    for i in range(45, 54):
        new_colors.append(color_map[button_colors[i]])
    for i in [9, 21, 33]:
        for j in range(i, i+3):
            new_colors.append(color_map[button_colors[j]])
    for i in [18, 30, 42]:
        for j in range(i, i+3):
            new_colors.append(color_map[button_colors[j]])

    cube_state = ''
    for i in new_colors:
        cube_state += i
    
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
    cube_state = map_colors_to_notation(button_colors)
 
    # Solve the cube using rubik_solver
    solution = sv.solve(cube_state)
    print(solution)

    ser = serial.Serial('COM3', 9600)
    time.sleep(2)
    my_list = solution

    ser.write(str(my_list).encode('utf-8'))
    ser.write(b'\n')  # Send a newline character

    # Optional: wait for Arduino to respond
    while ser.in_waiting:
        response = ser.readline().decode('utf-8').strip()
        print(f"Arduino says: {response}")

    # Close the serial connection
    ser.close() 

    return jsonify({'status': 'success', 'message': 'Colors received and processed'})

if __name__ == '__main__':
    app.run(debug=True)