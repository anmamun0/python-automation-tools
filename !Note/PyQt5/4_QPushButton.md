# QPushButton in PyQt5

`QPushButton` is a widget in PyQt5 that creates a clickable button. It supports various features like setting text, adding icons, handling click events, enabling/disabling states, and customizing styles.

## 1. Attributes of QPushButton
Below are some essential attributes of `QPushButton`:

<h6>

| **Attribute**  | **Description** |
|--------------|----------------|
| `text` | Returns the current text on the button. |
| `icon` | Sets or gets the icon displayed on the button. |
| `shortcut` | Defines a keyboard shortcut for the button. |
| `checkable` | Determines whether the button is checkable (toggle on/off). |
| `checked` | Returns `True` if the button is currently checked (for toggle buttons). |
| `enabled` | Checks if the button is enabled (`True`) or disabled (`False`). |
| `autoDefault` | If `True`, the button is automatically the default button. |
| `default` | If `True`, the button is the default button in the window. |
| `flat` | If `True`, the button has a flat appearance (no border or background). |
| `styleSheet` | Allows CSS-like styling for custom button appearance. |

 </h6>
 
## 2. Methods of QPushButton
The table below lists common methods available in `QPushButton`:
<h6> 

| **Method**  | **Description** |
|------------|----------------|
| `setText(text)` | Sets the text on the button. |
| `text()` | Returns the button text. |
| `setIcon(QIcon(icon))` | Sets an icon on the button. |
| `icon()` | Returns the current icon. |
| `setShortcut(QKeySequence(seq))` | Assigns a keyboard shortcut. |
| `setCheckable(bool)` | Makes the button toggleable (checkable). |
| `isCheckable()` | Returns `True` if the button is checkable. |
| `setChecked(bool)` | Checks or unchecks a checkable button. |
| `isChecked()` | Returns `True` if the button is checked. |
| `setEnabled(bool)` | Enables or disables the button. |
| `isEnabled()` | Checks if the button is enabled. |
| `setFlat(bool)` | Makes the button flat (no borders). |
| `isFlat()` | Returns `True` if the button is flat. |
| `click()` | Simulates a button click. |
| `toggle()` | Toggles a checkable button. |
| `setStyleSheet(style)` | Applies custom styles to the button. |
| `setDefault(bool)` | Sets the button as the default button. |
| `setAutoDefault(bool)` | Sets whether the button should be automatically the default button. |

 </h6>
 
## 3. Summary Table

<h6> 
  
| **Feature** | **Example** |
|------------|------------|
| Set button text | `button.setText("Click Me")` |
| Get button text | `text = button.text()` |
| Set an icon | `button.setIcon(QIcon("icon.png"))` |
| Set shortcut key | `button.setShortcut("Ctrl+S")` |
| Make button checkable | `button.setCheckable(True)` |
| Check if button is checkable | `is_checkable = button.isCheckable()` |
| Check/uncheck button | `button.setChecked(True)` |
| Get button state | `is_checked = button.isChecked()` |
| Enable/disable button | `button.setEnabled(False)` |
| Check if button is enabled | `is_enabled = button.isEnabled()` |
| Make button flat | `button.setFlat(True)` |
| Check if button is flat | `is_flat = button.isFlat()` |
| Simulate click | `button.click()` |
| Apply custom styling | `button.setStyleSheet("background-color: blue; color: white;")` |
  
 </h6>
 
## 4. Example Code: Using All Attributes & Methods in One File
The following PyQt5 program demonstrates the use of `QPushButton` attributes and methods:

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

# Create the application
app = QApplication(sys.argv)

# Create the main window
window = QWidget()
window.setWindowTitle("QPushButton Example")
window.setGeometry(100, 100, 400, 300)

# Create a button
button = QPushButton("Click Me", window)

# Set button properties
button.setIcon(QIcon("icon.png"))  # Set an icon
button.setShortcut("Ctrl+S")  # Set a keyboard shortcut
button.setCheckable(True)  # Make the button checkable (toggle button)
button.setDefault(True)  # Set as default button
button.setAutoDefault(True)  # Auto default button
button.setFlat(False)  # Keep button with borders
button.setStyleSheet("background-color: blue; color: white; font-size: 14px; padding: 10px;")

# Button click event
def on_button_click():
    if button.isChecked():
        button.setText("Checked!")
    else:
        button.setText("Unchecked!")

button.clicked.connect(on_button_click)  # Connect the button click event

# Layout
layout = QVBoxLayout()
layout.addWidget(button)
window.setLayout(layout)

# Show the window
window.show()

# Run the application
sys.exit(app.exec_())
```

This example covers all major attributes and methods of `QPushButton`, allowing you to explore its full functionality in PyQt5. 🚀 Let me know if you need any modifications! 🎯