# PyQt5 QLabel Widget Overview

`QLabel` is a versatile widget in PyQt5 that allows you to display text, images, or HTML content in your graphical user interface (GUI). It provides numerous methods and attributes to customize its appearance, alignment, text formatting, and interactivity.

## Common Methods and Attributes of `QLabel` in PyQt5

Below is a summary table of the most common attributes and methods of the `QLabel` class in PyQt5:

<h6>

| **Attribute/Method**              | **Description**                                                                                         | **Example/Usage**                                                                                              |
|-----------------------------------|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| `setText()`                       | Sets the text displayed on the label.                                                                    | `label.setText("Hello, PyQt5!")`                                                                               |
| `clear()`                         | Clears the text of the label.                                                                             | `label.clear()`                                                                                                 |
| `setFont()`                       | Sets the font for the label text.                                                                         | `label.setFont(QFont("Arial", 16))`                                                                             |
| `setAlignment()`                  | Sets the alignment of the text (e.g., left, right, center).                                               | `label.setAlignment(Qt.AlignCenter)`                                                                            |
| `setWordWrap()`                   | Enables or disables word wrapping. When enabled, text will wrap to the next line if it's too long.       | `label.setWordWrap(True)`                                                                                       |
| `setPixmap()`                     | Sets an image (QPixmap) to be displayed on the label.                                                    | `label.setPixmap(QPixmap("path_to_image.jpg"))`                                                                |
| `setTextFormat()`                 | Defines the format for the text (plain text or rich text like HTML).                                      | `label.setTextFormat(Qt.RichText)`                                                                              |
| `setStyleSheet()`                 | Applies custom CSS-like styling to the label (e.g., text color, background, padding, borders).            | `label.setStyleSheet("color: red; background-color: yellow;")`                                                 |
| `setIndent()`                     | Sets the indentation (spacing) of the label text.                                                        | `label.setIndent(20)`                                                                                          |
| `setAlignment(Qt.Alignment)`     | Defines how the text will be aligned inside the label (can be `Qt.AlignLeft`, `Qt.AlignCenter`, `Qt.AlignRight`, etc.). | `label.setAlignment(Qt.AlignRight)`                                                                            |
| `setMargin()`                     | Sets the margin (space) around the text or image inside the label.                                        | `label.setMargin(10)`                                                                                          |
| `setOpenExternalLinks()`          | When set to `True`, external links in the label's text (HTML) will open in the system's default browser.   | `label.setOpenExternalLinks(True)`                                                                             |
| `setToolTip()`                    | Sets a tooltip that appears when the user hovers over the label.                                          | `label.setToolTip("This is a tooltip.")`                                                                       |
| `setBuddy()`                      | Sets another widget as the "buddy" of this label, which can be focused when the label is clicked.         | `label.setBuddy(other_widget)`                                                                                 |
| `setAutoFillBackground()`         | Enables the label to automatically fill its background with a color.                                      | `label.setAutoFillBackground(True)`                                                                            |
| `setTextInteractionFlags()`       | Sets text interaction capabilities (e.g., selectable text).                                              | `label.setTextInteractionFlags(Qt.TextSelectableByMouse)`                                                     |
 </h6>
 
## Key Notes

- **Text-related Methods**:
  - `setText()`, `clear()`, `setWordWrap()`, `setTextFormat()`, and `setIndent()` control how the text is displayed, formatted, and aligned.
  
- **Style-related Methods**:
  - `setFont()`, `setAlignment()`, and `setStyleSheet()` allow you to customize the label's appearance by adjusting font size, alignment, and applying CSS-like styles.

- **Image-related Method**:
  - `setPixmap()` is used to display images on the label.

- **Event-related Methods**:
  - `setToolTip()` displays a tooltip when the user hovers over the label, and `setBuddy()` links the label to another widget for easier focus management.

## Example Code
 

```py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QLabel Example')
        self.setGeometry(100, 100, 400, 300)
        
        # Create a QLabel instance
        self.label = QLabel(self)

        # Set text content
        self.label.setText("Hello, PyQt5!\nThis is a QLabel example.\nClick to see more.")

        # Set font
        font = QFont("Arial", 16)
        self.label.setFont(font)

        # Set alignment
        self.label.setAlignment(Qt.AlignCenter)

        # Enable word wrap
        self.label.setWordWrap(True)

        # Set an image to QLabel (example)
        pixmap = QPixmap("your_image_path.jpg")  # Provide a valid image path
        self.label.setPixmap(pixmap)

        # Set text format to Rich Text (HTML)
        self.label.setText("<b><i>Hello, PyQt5!</i></b><br>This is <font color='blue'>rich text</font>.")

        # Set style with CSS (background color, text color, border, etc.)
        self.label.setStyleSheet("""
            color: white;
            background-color: darkblue;
            border: 2px solid yellow;
            padding: 10px;
            border-radius: 10px;
        """)

        # Set indent for multi-line text
        self.label.setIndent(20)

        # Create a layout and add the label
        layout = QVBoxLayout()
        layout.addWidget(self.label)

        self.setLayout(layout)

    def mousePressEvent(self, event):
        # Clear label content when clicked
        self.label.clear()

        # Set new content after click
        self.label.setText("Label clicked! Content cleared.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
```
