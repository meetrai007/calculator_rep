# Calculator Application

This is a simple GUI-based calculator application built using Python's Tkinter library. It is a basic calculator capable of performing arithmetic operations such as addition, subtraction, multiplication, and division, along with additional features like exponentiation (`^`) and double-zero input (`00`).

## Features

- User-friendly graphical interface.
- Supports basic arithmetic operations:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`)
  - Division (`/`)
- Additional functionality:
  - Exponentiation (`^`)
  - Double-zero input (`00`)
  - Clear screen (`c`)
- Displays results instantly with the `=` button.

## Requirements

- Python 3.x
- Tkinter library (comes pre-installed with Python on most platforms)

## How to Run the Application

1. Ensure you have Python installed on your system.
2. Copy the code into a file named `calculator.py`.
3. Open a terminal or command prompt and navigate to the directory where `calculator.py` is saved.
4. Run the following command:

   ```bash
   python calculator.py
   ```

5. The calculator GUI will appear, and you can start performing calculations.

## Code Overview

The application uses the following components:

- **Tkinter library**: For creating the GUI.
- **Buttons and Entry widgets**: To take user input and display results.
- **Event Binding**: To handle button click events.

## Functionality

1. **Button Clicks**:
   - Each button is bound to the `click` function, which updates the input field or evaluates the expression based on the button pressed.
2. **Evaluation**:
   - The `=` button evaluates the mathematical expression entered in the input field using Python's `eval()` function.
3. **Error Handling**:
   - If the user enters an invalid expression, the calculator displays `Error` in the input field.
4. **Clearing Input**:
   - The `c` button clears the input field.

## Future Improvements

- Add support for additional operations like square root, percentage, etc.
- Improve the user interface with better design and color schemes.
- Include memory functions (M+, M-, MC).
- Add keyboard input support for faster interaction.

## Acknowledgments

This is my first project in Python, and I am excited to share it. Special thanks to the Python and Tkinter communities for their amazing resources and tutorials.

