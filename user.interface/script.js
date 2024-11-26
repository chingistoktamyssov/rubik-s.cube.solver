let selectedButton = null;

// Get all the color buttons
const colorButtons = document.querySelectorAll(".color-button");

// When a button is clicked, mark it as the selected button
colorButtons.forEach(button => {
    button.addEventListener("click", () => {
        selectedButton = button;
    });
});

// Get all the color options
const colorOptions = document.querySelectorAll(".color-option");

// Add click event listener for each color option
colorOptions.forEach(option => {
    option.addEventListener("click", () => {
        if (selectedButton) {
            const selectedColor = option.style.backgroundColor;
            selectedButton.style.backgroundColor = selectedColor;
        }
    });
});
