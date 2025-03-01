# QTextEdit in PyQt5: Attributes, Methods, and Example

`QTextEdit` is a widget in PyQt5 that provides a rich text editor. It allows users to input and display multiline text, supports rich formatting (such as bold, italics, and color), and can display images and HTML content.

## 1. Attributes of QTextEdit
Here are some key attributes of `QTextEdit`:

| **Attribute**                | **Description**                                                              |
|------------------------------|------------------------------------------------------------------------------|
| `text`                        | Returns the plain text of the editor.                                         |
| `toPlainText()`               | Returns the plain text of the text edit, excluding any formatting.            |
| `toHtml()`                    | Returns the HTML representation of the text in the editor.                   |
| `document()`                  | Returns the document object associated with the `QTextEdit` (used for advanced manipulation). |
| `cursorPosition()`            | Returns the current position of the cursor in the text edit.                  |
| `selectionStart()`            | Returns the starting position of the selected text.                           |
| `selectionEnd()`              | Returns the ending position of the selected text.                             |
| `isReadOnly()`                | Checks if the text edit is in read-only mode.                                 |
| `wordWrapMode()`              | Sets or returns the word wrap mode of the text edit.                          |
| `textInteractionFlags()`      | Returns the interaction flags set for text editing (e.g., allows text to be selectable, editable). |

## 2. Methods of QTextEdit
Here are some commonly used methods for `QTextEdit`:

| **Method**                                | **Description**                                                                 |
|-------------------------------------------|---------------------------------------------------------------------------------|
| `setText(text)`                           | Sets the plain text content in the editor.                                       |
| `text()`                                  | Returns the plain text in the editor.                                           |
| `setPlainText(text)`                      | Sets plain text, clearing any formatting.                                       |
| `setHtml(html)`                           | Sets the content in HTML format.                                                |
| `toPlainText()`                           | Retrieves plain text without any formatting.                                    |
| `toHtml()`                                | Retrieves HTML-formatted content from the editor.                               |
| `setReadOnly(bool)`                       | Sets the text edit widget to read-only mode if `True`.                           |
| `isReadOnly()`                            | Returns `True` if the widget is in read-only mode.                              |
| `setUndoRedoEnabled(bool)`                | Enables or disables undo/redo functionality.                                    |
| `setWordWrapMode(mode)`                   | Sets the word wrap mode for the text edit (e.g., no wrap, word wrap).           |
| `setTextInteractionFlags(flags)`         | Sets interaction flags (such as enabling text selection and editing).          |
| `append(text)`                            | Appends the provided text to the end of the current content.                    |
| `clear()`                                 | Clears the content in the text editor.                                          |
| `setAlignment(alignment)`                 | Sets the alignment of the text (e.g., left, center, right, justify).            |
| `setFont(font)`                           | Sets the font for the text.                                                     |
| `setPlainTextCursorPosition(pos)`         | Sets the cursor position to the given text position.                            |

## 3. Summary Table
| **Feature**                            | **Example**                                                                  |
|----------------------------------------|------------------------------------------------------------------------------|
| Set plain text content                 | `text_edit.setText("Hello World!")`                                           |
| Get plain text content                 | `text = text_edit.text()`                                                     |
| Set HTML content                       | `text_edit.setHtml("<b>Hello</b> World!")`                                    |
| Get HTML content                       | `html = text_edit.toHtml()`                                                   |
| Set read-only mode                     | `text_edit.setReadOnly(True)`                                                 |
| Check if read-only mode                | `is_read_only = text_edit.isReadOnly()`                                       |
| Enable undo/redo                       | `text_edit.setUndoRedoEnabled(True)`                                          |
| Set word wrap mode                     | `text_edit.setWordWrapMode(QTextOption.WordWrap)`                             |
| Set text alignment                     | `text_edit.setAlignment(Qt.AlignCenter)`                                     |
| Append text                            | `text_edit.append("New Text!")`                                               |
| Clear text                             | `text_edit.clear()`                                                           |
| Set text font                          | `text_edit.setFont(QFont("Arial", 12))`                                       |
| Set cursor position                    | `text_edit.setPlainTextCursorPosition(10)`                                    |

## 4. Example Code: Using All Attributes & Methods in One File

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

# Create the application
app = QApplication(sys.argv)

# Create the main window
window = QWidget()
window.setWindowTitle("QTextEdit Example")
window.setGeometry(100, 100, 400, 300)

# Create a QTextEdit widget
text_edit = QTextEdit(window)

# Set basic text properties
text_edit.setText("Hello World!")  # Set plain text
text_edit.setReadOnly(False)  # Make the text editable
text_edit.setWordWrapMode(True)  # Enable word wrap

# Set text in HTML format
html_content = "<h1>Welcome to PyQt5!</h1><p>This is <b>bold</b> text.</p>"
text_edit.setHtml(html_content)

# Set font style
text_edit.setFont(QFont("Arial", 12))

# Set alignment to center
text_edit.setAlignment(Qt.AlignCenter)

# Append new text to the editor
text_edit.append("\nNew content added!")

# Button click event to change content
def on_button_click():
    text_edit.setText("This is new text.")

# Layout
layout = QVBoxLayout()
layout.addWidget(text_edit)
window.setLayout(layout)

# Show the window
window.show()

# Run the application
sys.exit(app.exec_())
