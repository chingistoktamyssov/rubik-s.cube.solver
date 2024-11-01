// Get all face elements
const faces = document.querySelectorAll('.face');

// Valid colors for the Rubik's cube
const validColors = ['yellow', 'blue', 'green', 'orange', 'white', 'red'];

const virtual_cube = [];
for (let i=0; i<6; i++) {
    for (let j=0; j<9; j++) {
        
    }
}

// Create 3x3 grid for each face (6 faces total)
faces.forEach(face => {
    for (let i = 0; i < 9; i++) {
        const button = document.createElement('button');
        button.classList.add('square-button');
        button.addEventListener('click', () => {
            const color = prompt("Choose a color: yellow, blue, green, orange, white, red");
            if (validColors.includes(color.toLowerCase())) {
                button.style.backgroundColor = color.toLowerCase();
            } else {
                alert("Invalid color! Please choose from yellow, blue, green, orange, white, or red.");
            }
        });
        face.appendChild(button);
    }
});