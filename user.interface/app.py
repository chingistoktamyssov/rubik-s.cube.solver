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


def faceOrienter(face):
    faceIndex = {'W': 0, 'G': 1, 'R': 2, 'B': 3, 'O':4, 'Y': 5}
    centerIndex = faceIndex[face]
    rightIndex = centerIndex+1
    leftIndex = centerIndex-1
    topIndex = 0
    botIndex = 5

    if face == 'W':
        topIndex = 4
        rightIndex = 3
        botIndex = 2
        leftIndex = 1
    if face == 'O':
        rightIndex = 1
    if face == 'G':
        leftIndex = 4
    if face == 'Y':
        topIndex = 2
        rightIndex = 3
        leftIndex = 1
        botIndex = 4

    return (centerIndex, topIndex, rightIndex, botIndex, leftIndex)

# simualtes a front turn of the cube (red center)
def turn(cube, face, direction):

    centerIndex, topIndex, rightIndex, botIndex, leftIndex = faceOrienter(face)

    # for clockwise rotations
    CenterCW = {0: 6, 1: 3, 2: 0, 3: 7, 5: 1, 6: 8, 7: 5, 8: 2}
    # for counterclockwise rotations
    CenterCCW = {6: 0, 3:1, 0:2, 7:3, 1:5, 8: 6, 5: 7, 2:8}

    # center change

    toChange = []
    if direction == 'clockwise':
        for i in range(9):
            if i == 4: continue
            toChange.append(cube[centerIndex][CenterCW[i]])
    else:
        for i in range(9):
            if i == 4: continue
            toChange.append(cube[centerIndex][CenterCCW[i]])
    k = 0
    for i in range(9):
        if i == 4: continue
        cube[centerIndex][i] = toChange[k]
        k += 1
    
    edges = [topIndex, rightIndex, botIndex, leftIndex]
    if face == 'G':
        edgePiece = [[0, 3, 6], [0, 3, 6], [8, 5, 2], [8, 5, 2]]
    if face == 'R':
        edgePiece = [[6,7, 8], [0, 3, 6], [2, 1, 0], [8, 5, 2]]
    if face == 'B':
        edgePiece = [[8, 5, 2], [0, 3, 6], [8, 5, 2], [8, 5, 2]]
    if face == 'O':
        edgePiece = [[0, 1, 2], [0, 1, 2], [6, 7, 8], [8, 5, 2]]
    if face == 'Y':
        edgePiece = [[6,7, 8], [6,7, 8], [6,7, 8], [6,7, 8]]

    middleOutsideCW = {0:6, 1:3, 2:0, 3:7, 5:1, 6: 8, 7:5, 8:2}
    middleOutsideCCW = {6:0, 3:1, 0:2, 7:3, 1:5, 8:6, 5:7, 2:8}
    CWFace = {topIndex: leftIndex, rightIndex: topIndex, botIndex: rightIndex, leftIndex: botIndex}
    CCWFace = {leftIndex: topIndex, topIndex: rightIndex, rightIndex: botIndex, botIndex: leftIndex}
    # side change
    toChange = []
    for i in range(4):
        workingFace = edges[i]
        workingSet = edgePiece[i]
    
        if direction == 'clockwise':
            for j in range(3):
                print(CWFace[workingFace], middleOutsideCW[workingSet[j]], cube[CWFace[workingFace]][middleOutsideCW[workingSet[j]]])
                toChange.append(cube[CWFace[workingFace]][middleOutsideCW[workingSet[j]]])
        else:
            for j in range(3):
                toChange.append(cube[CCWFace[workingFace]][middleOutsideCCW[workingSet[j]]])
    k = 0
    for i in range(4):
        workingFace = edges[i]
        workingSet = edgePiece[i]
        for j in range(3):
            cube[workingFace][workingSet[j]] = toChange[k]
            k += 1    

    return cube

def search(cube, piece, colors):
    edgeIndexTranslation = {1: 7, 3: 5, 5: 3, 7: 1}
    cornerIndexTranslation = {0: (2, 6), 2: (0, 8), 6: (8, 0), 8: (2, 6)}

    if piece == 'edge':
        c1, c2 = colors
        for face in ('W', 'G', 'R', 'B', 'O', 'Y'):
            centerIndex, topIndex, rightIndex, botIndex, leftIndex = faceOrienter(face)
            edgeIndexToFace = {1: topIndex, 3: leftIndex, 5: rightIndex, 7: botIndex}
            cornerIndexFace = {0: (leftIndex, topIndex), 2: (rightIndex, topIndex), 6: (leftIndex, botIndex), 8: (botIndex, rightIndex)}
            for index in range(1, 8, 2):
                for a, b in ((c1, c2), (c2, c1)):
                    if cube[centerIndex][index] == a and cube[edgeIndexToFace[index]][edgeIndexTranslation[index]] == b:
                        return ((a, centerIndex, index), (b, edgeIndexToFace[index], edgeIndexTranslation[index]))
           
    else: #here, the de facto piece is corner
        c1, c2, c3 = colors
        for face in ('W', 'G', 'R', 'B', 'O', 'Y'):
            centerIndex, topIndex, rightIndex, botIndex, leftIndex = faceOrienter(face)
            for index in range(0, 9, 2):
                p1, p2 = cornerIndexTranslation[index]
                f1, f2 = cornerIndexFace[index]

                for a, b, c in ((c1, c2, c3), (c1, c3, c2), (c2, c1, c3), (c2, c3, c1), (c3, c1, c2), (c3, c2, c1)):
                    if cube[centerIndex][index] == a and cube[f1][p1] == b and cube[f2][p2] == c:
                        return ((a, centerIndex, index), (b, f1, p1), (c, f2, p2))

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

    # cube = turn(cube, 'R', 'clockwise')
    # print('turn1', cube)
    cube = turn(cube, 'Y', 'counterclockwise')
    print('turn2', cube)
    cube = turn(cube, 'R', 'clockwise')
    print('turn3', cube)
    cube = turn(cube, 'Y', 'counterclockwise')
    print('turn4', cube)

    print(search(cube, 'edge', ('W', 'R')))

    return jsonify({'status': 'success', 'message': 'Colors received and processed'})

if __name__ == '__main__':
    app.run(debug=True)