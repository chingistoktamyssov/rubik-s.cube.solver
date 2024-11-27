// Initialize a 1D list of 54 elements to keep track of the colors for each button
// Each button starts with a default color of "lightgray"
let buttonColors = Array(54).fill("lightgray");

// Variable to store the currently selected color
let selectedColor = "";

// Indices of the center buttons and their corresponding colors
let centerColors = [4, 22, 25, 28, 31, 49];
let indexColor = {
    4: 'white',
    22: 'green',
    25: 'red',
    28: 'blue',
    31: 'orange',
    49: 'yellow'
};

// Set up the initial colors for the center buttons
function initializeCenterColors() {
    document.querySelectorAll('.color-button').forEach((button, index) => {
        if (centerColors.includes(index)) {
            button.style.backgroundColor = indexColor[index];

            // Update the 1D list with the center color
            buttonColors[index] = indexColor[index];
        }
    });
    checkLayoutCompletion();  // Check if the layout is complete after initializing centers
}

// Add event listeners to the color options (the color picker buttons at the top)
document.querySelectorAll('.color-option').forEach(option => {
    option.addEventListener('click', function () {
        selectedColor = this.style.backgroundColor; // Set the selected color
    });
});

// Add event listeners to the cube buttons
function setupButtonListeners() {
    document.querySelectorAll('.color-button').forEach((button, index) => {
        button.addEventListener('click', function () {
            if (selectedColor && !centerColors.includes(index)) {
                this.style.backgroundColor = selectedColor;

                // Update the 1D list with the new color
                buttonColors[index] = selectedColor;

                console.log(buttonColors)

                checkLayoutCompletion();  // Check if the layout is complete after each color change
            }
        });
    });
}

// Check if all buttons have been colored (no "lightgray" left)
function checkLayoutCompletion() {
    const isComplete = !buttonColors.includes("lightgray");

    // Update the message displayed under the layout
    const messageElement = document.getElementById('completion-message');
    if (isComplete) {
        messageElement.textContent = "Layout is complete!";
        messageElement.style.color = "green";  // Style for complete

        // Send the buttonColors list to the Python server
        sendColorsToServer(buttonColors);
    } else {
        messageElement.textContent = "Layout is incomplete";
        messageElement.style.color = "red";    // Style for incomplete
    }
}

// Function to send the buttonColors list to the server
function sendColorsToServer(colors) {
    fetch('/submit-colors', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ buttonColors: colors })  // Send buttonColors as JSON
    })
    .then(response => response.json())
    .then(data => {
        console.log("Server response:", data);
    })
    .catch(error => {
        console.error("Error sending colors:", error);
    });
}

// Initialize the center button colors and event listeners
initializeCenterColors();
setupButtonListeners();