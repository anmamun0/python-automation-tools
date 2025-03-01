# QLineEdit in PyQt5

QLineEdit is a single-line text input widget in PyQt5 that allows users to enter and edit text. It provides various attributes and methods to manipulate text, apply constraints, and improve user interaction.

## 1. Attributes of QLineEdit
<h6>

| Attribute          | Description |
|-------------------|-------------|
| `text`           | Returns the current text inside the QLineEdit. |
| `placeholderText` | Sets or gets the placeholder text (hint text). |
| `maxLength`      | Limits the number of characters that can be entered. |
| `readOnly`       | If True, the input field becomes read-only. |
| `echoMode`       | Controls how the text is displayed (Normal, Password, NoEcho). |
| `alignment`      | Sets the text alignment inside the input box. |
| `cursorPosition` | Gets or sets the cursor position inside the text field. |
| `inputMask`      | Defines an input mask for formatted input (e.g., phone numbers). |
| `frame`          | Enables or disables the frame around the input box. |
| `styleSheet`     | Sets custom styling for the input field. |

</h6>

## 2. Methods of QLineEdit

<h6>  
  
| Method | Description |
|-------------------------|------------------------------------------------|
| `setText(text)`         | Sets the text inside the QLineEdit. |
| `text()`                | Returns the current text inside the input field. |
| `clear()`               | Clears the text from the input field. |
| `setPlaceholderText(text)` | Sets a placeholder (hint text). |
| `setMaxLength(n)`       | Limits the number of characters that can be entered. |
| `setReadOnly(bool)`     | Makes the input field read-only. |
| `setEchoMode(mode)`     | Changes how the text is displayed (Normal, Password, NoEcho). |
| `setAlignment(alignment)` | Aligns the text (e.g., `Qt.AlignRight`). |
| `cursorPosition()`      | Returns the current cursor position. |
| `setCursorPosition(pos)` | Moves the cursor to a specific position. |
| `setInputMask(mask)`    | Applies an input mask (e.g., "999-999-999" for a phone number). |
| `setFrame(bool)`        | Enables or disables the border frame. |
| `setStyleSheet(style)`  | Sets custom CSS styles for the input field. |
| `setValidator(validator)` | Applies an input validator to restrict input values. |
| `editingFinished()`     | Signal emitted when editing is completed. |
| `returnPressed()`       | Signal emitted when Enter is pressed. |
| `selectAll()`           | Selects all text inside the input field. |
| `setDragEnabled(bool)`  | Enables or disables drag-and-drop support. |
| `undo()`                | Undoes the last text change. |
| `redo()`                | Redoes the last undone change. |
| `copy()`                | Copies selected text to the clipboard. |
| `cut()`                 | Cuts selected text and copies it to the clipboard. |
| `paste()`               | Pastes text from the clipboard into the field. |

 </h6>

```py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

def update_label():
    """Updates the label text with the entered text in QLineEdit"""
    label.setText(f'Entered Text: {entry.text()}')

def clear_text():
    """Clears the QLineEdit text"""
    entry.clear()

# Create the application
app = QApplication(sys.argv)

# Create the main window
window = QWidget()
window.setWindowTitle('QLineEdit Functional Example')
window.setGeometry(100, 100, 400, 300)

# Create the layout
layout = QVBoxLayout()

# QLabel to display the entered text
label = QLabel('Entered Text:', window)
label.setFont(QFont('Arial', 12))
layout.addWidget(label)

# Create QLineEdit
entry = QLineEdit(window)
entry.setPlaceholderText('Enter something...')
entry.setMaxLength(20)
entry.setAlignment(Qt.AlignRight)  # Align text to right
entry.setEchoMode(QLineEdit.Normal)  # Normal text input mode
entry.setInputMask("999-999-999")  # Example: Phone number format (###-###-###)
entry.setFrame(True)  # Enable the frame
entry.setStyleSheet("border: 2px solid blue; padding: 5px; font-size: 14px;")

# Connect signal to update label text
entry.textChanged.connect(update_label)

# Add QLineEdit to layout
layout.addWidget(entry)

# Button to clear text
clear_button = QPushButton('Clear', window)
clear_button.clicked.connect(clear_text)
layout.addWidget(clear_button)

# Set layout to the window
window.setLayout(layout)

# Show the window
window.show()

# Run the application event loop
sys.exit(app.exec_())
```

# Run the application

app = QApplication(sys.argv)
window = LineEditExample()
window.show()
sys.exit(app.exec_())
## 4. Summary Table
<h6>

| Feature | Example |
|------------|------------------|
| Set text | `entry.setText("Hello!")` |
| Get text | `text = entry.text()` |
| Clear text | `entry.clear()` |
| Set placeholder | `entry.setPlaceholderText("Enter name...")` |
| Set max length | `entry.setMaxLength(10)` |
| Set read-only | `entry.setReadOnly(True)` |
| Set password mode | `entry.setEchoMode(QLineEdit.Password)` |
| Align text to right | `entry.setAlignment(Qt.AlignRight)` |
| Set cursor position | `entry.setCursorPosition(3)` |
| Set input mask | `entry.setInputMask("999-999-999")` |
| Remove frame | `entry.setFrame(False)` |
| Apply CSS styling | `entry.setStyleSheet("border: 1px solid red;")` |
| Select all text | `entry.selectAll()` |
| Enable drag-and-drop | `entry.setDragEnabled(True)` |
| Undo action | `entry.undo()` |
| Redo action | `entry.redo()` |
| Copy text | `entry.copy()` |
| Cut text | `entry.cut()` |
| Paste text | `entry.paste()` |
| Signal on enter press | `entry.returnPressed.connect(your_function)` |
| Signal on edit complete | `entry.editingFinished.connect(your_function)` |
 </h6>

Conclusion
- QLineEdit is a powerful widget for text input.
- You can control appearance, behavior, and validation.
- It provides various attributes and methods to enhance user experience.
- The example demonstrates practical usage of QLineEdit.
- Would you like any modifications or a more advanced UI for this example? 🚀

 
