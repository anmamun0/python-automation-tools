# PyQt5 Fundamentals

This repository covers the fundamental elements of PyQt5 for creating graphical user interfaces (GUIs). PyQt5 is a powerful library used to create desktop applications with Python.

## 2. Basic Concepts
### Application Flow
A PyQt5 application follows the following flow:
1. Create an instance of `QApplication`.
2. Create the main window or widgets.
3. Show the window with `show()`.
4. Enter the event loop with `app.exec_()`.

## Table of Contents

1. [Widgets](#widgets)
2. [Layout Management](#layout-management)
3. [Signals and Slots](#signals-and-slots)
4. [Event Handling](#event-handling)
5. [QtCore (Core Classes)](#qtcore-core-classes)
6. [QtGui (Graphics and Images)](#qtgui-graphics-and-images)
7. [QtWidgets (Windowing)](#qtwidgets-windowing)
8. [Other Elements](#other-elements)
9. [Example Code](#example-code)

## 1. Widgets

Widgets are the building blocks of PyQt5 applications. A widget is an element in the GUI such as a button, text box, or label.

### Common Widgets:

- **QWidget**: The base class for all UI elements.
- **QPushButton**: A button that users can click.
- **QLabel**: A widget used for displaying text or images.
- **QLineEdit**: A widget for text input, where the user can type something.
- **QTextEdit**: A multi-line text input widget.
- **QComboBox**: A drop-down list that allows users to select an item from a list.
- **QRadioButton**: A widget that allows the user to select one option from a group of options.
- **QCheckBox**: A widget that allows the user to select or deselect a checkable option.
- **QListWidget**: A list widget that displays a list of items.
- **QSpinBox**: A widget for selecting numeric values within a defined range.
- **QSlider**: A widget for selecting a value by sliding a handle.
- **QProgressBar**: A widget that shows progress through a task.

### Attributes/Methods of `QWidget`:
- `setWindowTitle()`: Sets the window's title.
- `resize()`: Changes the widget’s size.
- `move()`: Moves the widget to the specified location.
- `setStyleSheet()`: Applies CSS-like styling to the widget.
- `show()`: Displays the widget on the screen.
- `hide()`: Hides the widget.

## 2. Layout Management

Layouts help in arranging widgets on the window in a clean and responsive manner.

### Common Layouts:
- **QVBoxLayout**: A vertical layout manager that arranges widgets in a column.
- **QHBoxLayout**: A horizontal layout manager that arranges widgets in a row.
- **QGridLayout**: A grid layout manager that arranges widgets in a grid of rows and columns.
- **QFormLayout**: A layout manager used for creating forms, where fields are placed in a label-to-field manner.

### Attributes/Methods:
- `addWidget(widget)`: Adds a widget to the layout.
- `addStretch()`: Adds a stretchable space to a layout.
- `setAlignment()`: Aligns widgets inside the layout.
- `setContentsMargins()`: Sets the margins around the layout.

## 3. Signals and Slots

Signals and slots are used for communication between objects. Signals are emitted by widgets when certain actions occur (e.g., a button is clicked), and slots are methods that handle these signals.

### Common Methods:
- **Signals**:
  - `clicked()`: A signal that is emitted when a button is clicked.
  - `textChanged()`: A signal emitted when the text in a `QLineEdit` changes.
- **Slots**: Any method or function that can be connected to a signal. Slots are called when a corresponding signal is emitted.
  - `connect()`: Used to connect a signal to a slot (method).
  - `disconnect()`: Disconnects a signal from its connected slot.

Example:
```python
button.clicked.connect(some_function)
```

## 4. Event Handling
Events represent actions that happen during the lifetime of an application, like key presses, mouse movements, and window resizes. PyQt5 handles events by using event handlers (methods that handle the events).

### Common Events:
- **QMouseEvent**: Represents a mouse event (e.g., button press, movement).
- **QKeyEvent**: Represents a keyboard event (e.g., key press, release).
- **QResizeEvent**: Represents a window resize event.
- **QCloseEvent**: Represents a window close event.

### Methods:
- `event(event)`: A method to handle any event.
- `mousePressEvent(event)`: Handles mouse button press events.
- `keyPressEvent(event)`: Handles keyboard button press events.
- `resizeEvent(event)`: Handles window resize events.

### Example:
```python
def mousePressEvent(self, event):
    print(f"Mouse pressed at ({event.x()}, {event.y()})")
```









## 5. PyQt5.QtCore (Core Classes)
QtCore provides basic functionality such as time handling, threads, signals, and event loops.

### Common Classes:
- **QTimer**: A class used for creating time-based events. It triggers a signal after a specified time interval.
- **QThread**: A class used for managing threads in PyQt5, allowing multitasking.
- **QDateTime**: Used for handling date and time operations.
- **QSignal**: For defining custom signals that can be emitted from any class.
- **QEvent**: Used to create custom events.

## 6. PyQt5.QtGui (Graphics and Images)
QtGui provides classes for handling fonts, colors, images, and other graphical operations.

### Common Classes:
- **QFont**: A class for defining and manipulating font styles.
- **QColor**: A class used to define and manipulate colors.
- **QPixmap**: A class used to handle images.
- **QIcon**: A class used for handling icons.
- **QPainter**: A class used for drawing shapes and text on widgets.

### Common Methods:
- `setFont(font)`: Sets the font for a widget.
- `setColor(color)`: Sets the color for a widget or painter.
- `load(file)`: Loads an image file into a QPixmap.

## 7. PyQt5.QtWidgets (Windowing)
The QtWidgets module deals with windowing elements in the application, like windows, dialogs, and other widget-based containers.

### Common Classes:
- **QMainWindow**: A main window that serves as the central widget for an application.
- **QDialog**: A dialog box used for interaction with the user.
- **QFileDialog**: A dialog for file selection.
- **QMessageBox**: A dialog for showing messages to the user (information, warning, etc.).

## 8. Other Elements

### Graphics View Framework:
- **QGraphicsScene**: Represents the scene or the canvas where graphical items are placed.
- **QGraphicsView**: A view of the scene used for visual representation.

### Custom Widgets:
PyQt5 allows for creating custom widgets by subclassing existing widget classes and reimplementing methods like `paintEvent()` for custom drawing, or `mousePressEvent()` for custom behavior.


9. Example Code
Here is an example of creating a simple PyQt5 application with a button and a label:

```py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

def on_button_click():
    label.setText("Hello, PyQt5!")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("PyQt5 Example")
window.resize(300, 200)

label = QLabel("Click the button", window)
label.move(100, 50)

button = QPushButton("Click Me", window)
button.move(100, 100)
button.clicked.connect(on_button_click)

window.show()
sys.exit(app.exec_())
```
This code creates a window with a button. When the button is clicked, the text of the label is updated.

By understanding these elements, you can create complex and interactive desktop applications with PyQt5. Happy coding!
 

### File: `main.py`

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

def on_button_click():
    label.setText("Hello, PyQt5!")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("PyQt5 Example")
window.resize(300, 200)

label = QLabel("Click the button", window)
label.move(100, 50)

button = QPushButton("Click Me", window)
button.move(100, 100)
button.clicked.connect(on_button_click)

window.show()
sys.exit(app.exec_())
```