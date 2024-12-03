from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__,
            static_url_path='', 
            static_folder='static')

buttonColors = []

@app.route("/")
def index():
    return send_from_directory("static", 'index.html')

def populateCube(buttonColors):
    # New list to organize the buttonColors list
    cube = [[1 for j in range(9)] for i in range(6)]
    # Hashmap to abbreviate colors into letters, more compact list --> easier to read
    
    shortenColor = {'white': 'W', 'blue': 'B', 'red': 'R', 'orange': 'O', 'green': 'G', 'yellow': 'Y'}

    # This brute force is very stupid but easy --> I like :D

    # Populate the white center at index 0
    for i in range(9):
        cube[0][i] = shortenColor[buttonColors[i]]

    # Layer 1 Middle Section
    face = 1
    counter = 0
    for i in range(9, 21):
        cube[face][counter] = shortenColor[buttonColors[i]]
        counter += 1
        if counter == 3:
            counter = 0
            face += 1
    
    # Layer 2 Middle Section
    face = 1
    counter = 3
    for i in range(21, 33):
        cube[face][counter] = shortenColor[buttonColors[i]]
        counter += 1
        if counter == 6:
            counter = 3
            face += 1

    # Layer 3 Middle Section
    face = 1
    counter = 6
    for i in range(33, 45):
        cube[face][counter] = shortenColor[buttonColors[i]]
        counter += 1
        if counter == 9:
            counter = 6
            face += 1

    # Populate the yellow center at index 5
    k = 0
    for i in range(45, 54):
        cube[5][k] = shortenColor[buttonColors[i]]
        k += 1

    return cube

# simualtes a front turn of the cube (red center)
def turn(cube, face, direction):
    faceIndex = {'W': 0, 'G': 1, 'R': 2, 'B': 3, 'O':4, 'Y': 5}
    centerIndex = faceIndex[face]

    rightIndex = centerIndex+1
    leftIndex = centerIndex-1
    topIndex = 0
    botIndex = 5

    if face == 'O':
        rightIndex = 1
    if face == 'G':
        leftIndex = 4
    if face == 'Y':
        topIndex = 2
        rightIndex = 3
        leftIndex = 1
        botIndex = 4

    # for clockwise rotations
    CenterCW = {0: 6, 1: 3, 2: 0, 3: 7, 5: 1, 6: 8, 7: 5, 8: 2}
    # for counterclockwise rotations
    CenterCCW = {6: 0, 3:1, 0:2, 7:3, 1:5, 8: 6, 5: 7, 2:8}

    middleOutsideCW = {0:6, 1:3, 2:0, 3:7, 5:1, 6: 8, 7:5, 8:2}
    middleOutsideCCW = {6:0, 3:1, 0:2, 7:3, 1:5, 8:6, 5:7, 2:8}


    for i in range(9):
        center


    cube[]

# Route to receive the buttonColors list
@app.route('/submit-colors', methods=['POST'])
def receive_colors():
    global buttonColors

    data = request.json  # Receive the JSON data sent from JavaScript
    buttonColors = data.get('buttonColors', [])
    
    # Process the button_colors here (save to a file, database, etc.)
    print("Received buttonColors:", buttonColors)

    cube = populateCube(buttonColors)
    # Print out the new list
    print("Reorganized buttonColors:", cube)

if __name__ == '__main__':
    app.run(debug=True)