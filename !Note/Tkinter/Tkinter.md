# Getting Started with Tkinter
<h6>
  Tkinter is Python’s standard GUI (Graphical User Interface) library. It allows you to create desktop applications with windows, buttons, labels, text inputs, and more. Since you're already proficient in Python, learning Tkinter will be smooth for you.
</h6>

```py
import tkinter as tk
```

Basic Tkinter Window

```py
import tkinter as tk

root = tk.Tk()  # Create the main window
root.title("My First Tkinter App")  # Set window title
root.geometry("400x300")  # Set window size

root.mainloop()  # Run the Tkinter event loop
```

# Learn Path

- Root Control Methods [click](#root-control-methods) 
- tkinter all Widgets [click](#tkinter-all-widgets)
- Tkinter Geometry Management  pack(), grid(), and place() [click](#tkinter-geometry-management)
- Event Handling [click](#event-handling )
- Tkinter Variable Classes [click](#tkinter-variable-classes)
- Time and Date Handling [click](#time-and-date-handling)
- Validation in Tkinter [click](#validation-in-tkinter)

<br>
<br>

## Root control Methods
<h6> 
  
|  Tk methods           | Purpose                                  |  
|-----------------------|------------------------------------------| 
|1. `root.title(title_name)` | Sets the title of the Tkinter window. |  
|2.` root.geometry("widthxheight+x_offset+y_offset")` | Sets the title of the Tkinter window. | 
|3. `root.mainloop()` | Starts the Tkinter event loop and keeps the application running. | 
|4. `root.resizable(width, height)` |  Controls whether the user can resize the window. | 
|5. `root.iconbitmap("icon.ico")` , `root.iconphoto(True, image)` | Sets a custom icon for the Tkinter window (Windows only). | 
|6. `root.configure(bg="color")` | Changes the background color of the window. | 
|7. `root.attributes(attribute, value)` | Controls window attributes like transparency, full-screen mode, and top-most status. | 
|8. `root.iconify() & root.deiconify(), root.destroy()` | Minimize window, Restore window, Destroy window. | 
|9. `root.withdraw()` | Hides the window without closing it. | 
|10. `root.protocol("WM_DELETE_WINDOW", callback_function)` |  Controls the behavior when the user clicks the close (X) button. | 

</h6>
 
#### 1. `root.title(title_name)`
```py
root.title("My Tkinter App")  # Setting the window title
 ``` 

#### 2. `root.geometry("widthxheight+x_offset+y_offset")`
```py
root.geometry("500x400")  # Sets width=500px, height=400px
root.geometry("500x400+200+100")  # Width: 500px, Height: 400px, X=200px, Y=100px
```

#### 4. `root.mainloop()`
```py
root.mainloop()
```

#### 6. `root.resizable(width, height)`
```py
root.resizable(False, False)  # Prevents resizing
```
 
#### 7. `root.iconbitmap("icon.ico")`
```py
root.iconbitmap("myicon.ico")  # Replace with your .ico file path
 
icon = tk.PhotoImage(file="icon.png")
root.iconphoto(True, icon)
```
 
#### 6. `root.configure(bg="color")`
```py
root.configure(bg="lightblue")  # Sets background color to light blue
```


#### 7. `root.attributes(attribute, value)`

<h6> 
Common Attributes: <br> 
"fullscreen" → Enables full-screen mode (root.attributes("-fullscreen", True))  <br> 
"alpha" → Controls transparency (root.attributes("-alpha", 0.5)) (0.0 = fully transparent, 1.0 = fully opaque)  <br> 
"topmost" → Keeps the window on top (root.attributes("-topmost", True))  <br> 
</h6>

```py
root.attributes("-alpha", 0.8)  # 80% opacity
root.attributes("-topmost", True)  # Window stays on top
```

#### 8. `root.iconify(), root.deiconify() , root.destroy()` 
```py
 
import tkinter as tk
 
def minimize():
    root.iconify()  # Minimize window

def restore():
    root.deiconify()  # Restore window
 

btn1 = tk.Button(root, text="Minimize", command=minimize)
btn1.pack(pady=10)

btn2 = tk.Button(root, text="Restore", command=restore)
btn2.pack(pady=10)
 ```


#### 9. `root.withdraw()`
```py
root.withdraw()  # Hides the main window
```

#### 10. `root.protocol("WM_DELETE_WINDOW", callback_function)`

<h6>
Protocol: <br> 
`WM_DELETE_WINDOW` -> 	Handles window close (X button) <br> 
`WM_TAKE_FOCUS`	-> Called when the window receives focus <br> 
`WM_SAVE_YOURSELF` ->	Used for session persistence in X11 <br> 

 </h6>
 
```py
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

def on_closing():
    if messagebox.askyesno("Exit", "Do you really want to quit?"):
        root.destroy()  # Close the window
        
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
```



<br>
<br>


## tkinter all Widgets
 
| Widget	  | Purpose                  | Description |  
|-----------|--------------------------|------------| 
| `Label` | 	Displays text or images | [click](#label) | 
| `Button` | 	Creates a clickable button | [click](#button) |
| `Entry` | 	Single-line text input | [click](#entry) |
| `Text` | 	Multi-line text input | [click](#label) |
| `Frame` | 	Groups widgets together | [click](#frame) |
| `Checkbutton` | 	Checkbox for multiple selections | [click](#checkbutton) |
| `Radiobutton` | 	Radio button for single selection | [click](#radiobutton) |
| `Listbox` | 	Displays a list of items | [click](#listbox) |
| `Combobox` | 	Dropdown selection menu | [click](#combobox) |
| `Scale` | 	Slider for selecting values | [click](#scale) |
| `Progressbar` | 	Shows progress of a task | [click](#progressbar) |
| `Menu` | 	Creates a menu bar | [click](#menu) |

<br>
<br>

## Label
###### The Label widget in Tkinter is used to display text or images in a GUI application. It supports various customizations, such as font, color, size, alignment, and more.

### Label widget summary

<h6>
  
| Method	| Description| 	Usage| 
|----------------|-------------------------|------------------------|
| config()	| Configures or updates the label's properties.	| label.config(text="New Text", font=("Arial", 12))| 
| configure()	| Same as config(), updates label properties.| 	label.configure(bg="red", fg="white")| 
| cget()	| Retrieves the current value of a specific option of the label.	| label.cget("text")| 
| grid()	| Places the label in a grid layout (if used).| 	label.grid(row=0, column=0)| 
| pack()| 	Places the label in the parent widget using the pack geometry manager.	| label.pack(side="top", pady=10)| 
| place()| 	Places the label at a specific location with precise x and y coordinates.	| label.place(x=50, y=100)| 
| destroy()| 	Destroys the label widget (removes it from the interface).| 	label.destroy()| 
| bind()| 	Binds a function to a specific event (e.g., mouse hover, click).	| label.bind("<Button-1>", function)| 
| unbind()| 	Unbinds an event from the label widget.	| label.unbind("<Button-1>")| 
| after()| 	Calls a function after a specified amount of time.	| label.after(1000, function)| 
| update()| 	Updates the widget and redraws it (useful for dynamic content updates).| 	label.update()| 
| update_idletasks()| 	Forces the widget to process its pending tasks.| 	label.update_idletasks()| 
| focus_set()| 	Sets the focus to the label widget (if it can receive focus).	| label.focus_set()| 
  
</h6>

```py
hello = tk.Label(root,text="Hello AN Mamun", font=('Arial',16),fg="white" ,bg='blue',wraplength=2,cursor='hand2')
hello.pack(pady=10)

```
<h6> 
  
The Label widget supports several options that you can use to customize its appearance.

| Option | 	Description | 
|-------|--------------|
| text | 	Sets the text to display. | 
| font |  	Changes font type, size, and style.| 
| fg (foreground) | 	Sets the text color.| 
| bg (background) | 	Sets the background color.| 
| width | 	Sets the width of the label (in characters).| 
| height | 	Sets the height of the label (in lines).| 
| padx | 	Adds padding (horizontal).| 
| pady | Adds padding (vertical).| 
| borderwidth | 	Sets the border width.| 
| relief | 	Defines the border style (flat, raised, sunken, ridge, solid, groove).| 
| anchor | 	Aligns the text (n, ne, e, se, s, sw, w, nw, center).| 
| justify  | 	Aligns multi-line text (left, right, center).| 
| wraplength	 | Wraps text after the given width.| 
| bitmap | 	Displays built-in images (error, hourglass, etc.).| 
| image	 | Displays an image (PhotoImage or BitmapImage).| 
| cursor	 | Changes the mouse cursor. "hand1", "hand2" ...  | 


</h6>
 - Use `label.config()` whenever you need to update a widget dynamically.

```py 
label = tk.Label(root, text="Hello, AN Mamun!", font=("Arial", 16))
label.pack(pady=10)

def update_text():
    label.config(text="Text Updated!",font=("Courier", 20, "bold"), fg="red", bg="yellow")  # Changing the label's text

btn = tk.Button(root, text="Click Me", command=update_text)
btn.pack(pady=10) 
```

<br>
<br>

## Button
###### The Button widget in Tkinter is used to create clickable buttons in a GUI application. You can customize its text, color, font, size, command (function), and other properties.

### Button Widget Summary


<h6>

| Method	| Description	| Usage| 
|-----------------|----------------------|----------------------|
| config()| 	Configures or updates the button's properties (like text, font, etc.).| 	button.config(text="New Text", bg="red")| 
| configure()| 	Same as config(), updates button properties.	| button.configure(state="disabled")| 
| cget()	| Retrieves the current value of a specific option of the button.	| button.cget("text")| 
| grid()| 	Places the button in a grid layout (if used).| 	button.grid(row=0, column=0)| 
| pack()	| Places the button in the parent widget using the pack geometry manager.| 	button.pack(side="top", pady=10)| 
| place()| 	Places the button at a specific location with precise x and y coordinates.	| button.place(x=50, y=100)| 
| destroy()	| Destroys the button widget (removes it from the interface).| 	button.destroy()| 
| bind()	| Binds a function to a specific event (e.g., mouse click, hover).	| button.bind("<Button-1>", function)| 
| unbind()	| Unbinds an event from the button widget.	| button.unbind("<Button-1>")| 
| invoke()	| Simulates a button click programmatically.	| button.invoke()| 
| after()	| Calls a function after a specified amount of time.	| button.after(1000, function)| 
| update()	| Updates the widget and redraws it (useful for dynamic content updates).| 	button.update()| 
| update_idletasks()	| Forces the widget to process its pending tasks.| 	button.update_idletasks()| 
| flash()	| Flashes the button (briefly changes its background color).	| button.flash()| 
  
</h6>

```py
def say_hello():
    print("Hello, AN Mamun!")

btn = tk.Button(root, text="Click Me", command=say_hello)
btn.pack(pady=10)

```
###  Changing Button Properties Dynamically

- Toggle Button Text
```py
def toggle_text():
    if btn["text"] == "Click Me":
        btn.config(text="Clicked!")
    else:
        btn.config(text="Click Me")

btn = tk.Button(root, text="Click Me", command=toggle_text)
btn.pack(pady=10)
```
- 🔹 Change Button Color on Click

```py
def change_color():
    btn.config(bg="green", fg="white")

btn = tk.Button(root, text="Press Me", command=change_color, bg="red", fg="black")
btn.pack(pady=10)

```

- 🔹 Enable & Disable Button
```py
def disable_button():
    btn.config(state="disabled")  # Disable button

btn = tk.Button(root, text="Disable Me", command=disable_button)
btn.pack(pady=10)

```

- 🔹 Button with Hover Effect

```py
def on_enter(e):
    btn.config(bg="yellow")

def on_leave(e):
    btn.config(bg="blue")

btn = tk.Button(root, text="Hover Me", bg="blue", fg="white")
btn.bind("<Enter>", on_enter)  # Change color on hover
btn.bind("<Leave>", on_leave)  # Revert color on mouse leave
btn.pack(pady=10)

```

### Button bind() Method in Tkinter
###### widget.bind(event, function)






### 2. Button bind() Example - Right & Left Click
   
-  bind() with Mouse Events

<h6> 
  
| Event	| Description| 
|---------|--------------|
| \<Button-1\> | 	Left mouse click| 
| \<Button-2\> | 	Middle mouse click (rarely used)| 
| \<Button-3\>	| Right mouse click| 
| \<Double-Button-1\>	| Double left click| 
| \<B1-Motion\> | 	Dragging while holding left button| 
| \<Enter\> | 	Mouse enters widget| 
| \<Leave\> | 	Mouse leaves widget| 
  
</h6>
  
```py
import tkinter as tk

root = tk.Tk()
root.title("Button Bind Example")

def left_click(event):
    print("Left Button Clicked!")

def right_click(event):
    print("Right Button Clicked!")

btn = tk.Button(root, text="Click Me")
btn.pack(pady=10)

# Bind left click (Button-1) and right click (Button-3)
btn.bind("<Button-1>", left_click)
btn.bind("<Button-3>", right_click)

root.mainloop()

```
### 4. bind() with Keyboard Events

<h6> 
  
| Event  |	Description  |
|--------------|--------------|
| \<KeyPress\>	 | Any key press |
| \<KeyPress-a\>  | 	Pressing the "A" key  |
| \<KeyRelease\>	 |  Key release after pressing v
| \<Escape\>	 |  Pressing the ESC key  |
  
</h6>

```py

def change_text(event):
    btn.config(text="Key Pressed!")

root.bind("<KeyPress>", change_text)  # Detects any key press
```


## Entry
##### The Entry widget in Tkinter is used to create a single-line text input field. It is commonly used in forms, login pages, and user input fields.



### Entry Widget Summary
<h6>

| Method |  	Description | 	Usage | 
|----------------|----------------------|---------------------|
| config()| 	Configures or updates the Entry widget’s properties (like font, background, etc.).	| entry.config(bg="lightblue", font=("Arial", 12))| 
| configure()	| Same as config(), updates Entry widget properties.	| entry.configure(state="disabled")| 
| cget()| 	Retrieves the current value of a specific option of the Entry widget.	| entry.cget("textvariable")| 
| get()| 	Retrieves the current text in the Entry widget.| 	entry.get()| 
| insert()	| Inserts text at a specific position in the Entry widget.	| entry.insert(0, "Default Text")| 
| delete()| 	Deletes text from the Entry widget, either a specific index or the entire text.	| entry.delete(0, END)| 
| select_range()| 	Selects a range of text between two indices.| 	entry.select_range(0, 5)| 
| select_all()| 	Selects all text in the Entry widget.	| entry.select_all()| 
| focus()| 	Moves the focus to the Entry widget.	| entry.focus()| 
| focus_set()	| Sets the focus on the Entry widget (useful if Entry is not the default focus).| 	entry.focus_set()| 
| bind()	| Binds an event (e.g., key press, click) to the Entry widget.	| entry.bind("<Return>", function)| 
| unbind()	| Unbinds an event from the Entry widget. | 	entry.unbind("<Return>")| 
| validate()| 	Validates the input before inserting or modifying it.| 	entry.config(validate="key")| 
| delete()| 	Deletes a specific range or the entire content of the entry.	| entry.delete(0, tk.END)| 
| xview()	| Allows horizontal scrolling, retrieves or sets the view position.	| entry.xview()| 
| yview()	| Allows vertical scrolling (useful in case of multiline entry).| 	entry.yview()| 
| after()	| Calls a function after a specified amount of time.	| entry.after(1000, function)| 
| update()	| Updates the widget and redraws it.	| entry.update()| 
| update_idletasks()	| Forces the widget to process its pending tasks.| 	entry.update_idletasks()| 
  
</h6>



```py
entry = tk.Entry(root)
entry.pack(pady=10)
```


## 2️⃣ Common Entry Properties & Customization
<h6> 

| Property | 	Description | 
|--------------|----------------------------------|
| width | 	Width of the entry field (in characters)| 
| bg / background | 	Background color| 
| fg / foreground	 | Text color| 
| font | 	Font style and size| 
| bd / borderwidth | 	Border thickness| 
| relief	 | Border style (flat, raised, sunken, ridge, solid, groove)| 
| show| 	Masks input (useful for passwords)| 
| justify	| Align text (left, center, right)| 
| state	| normal, disabled, or readonly| 
| insertbackground | 	Color of the insertion cursor| 
| exportselection | 	Controls if selected text is copied to clipboard| 

</h6>

## 3️⃣ Getting & Setting Entry Text

- 🔹 get() – Retrieve Input
```py
entry = tk.Entry(root,width=30)
entry.pack(pady=10)

bttn = tk.Button(root,text="Enter Text",command=lambda : print(entry.get()))

bttn.pack(pady=10)
```
######  Retrieves the current text inside the Entry field.


- 🔹 insert() – Set Default Text

```py
entry.insert(0, "Enter Your Name.")
```
######  Inserts default text at the beginning (index=0).


- 🔹 delete() – Clear or Remove Text
  
```py
entry.delete(0, tk.END)  # Deletes all text
```
######  Removes text from the entry field.




## 4️⃣ Dynamic Entry Changes

```py
def change_text():
    entry.delete(0, tk.END)  
    entry.insert(0, "New Dynamic Text!")

btn = tk.Button(root, text="Change Text", command=change_text)
btn.pack(pady=10)

```
######  Clicking the button replaces the entry text dynamically.

## 5️⃣ Entry show for Password Fields
 
```py
password_entry = tk.Entry(root, show="*")  # Hides characters
password_entry.pack(pady=10)
```
###### Replaces input characters with * for passwords.


## 6️⃣ Handling Events with Entry.bind()

| Event | 	Description | 
|-------------|-------------|
| \<Return\> | 	Press Enter key | 
| \<FocusIn\> | 	When Entry is selected | 
| \<FocusOut\> |	When Entry loses focus | 
| \<KeyRelease\> |	When a key is released | 


- 🔹 Example: Press Enter to Get Text
```py
def on_enter(event):
    print("You entered:", entry.get())

entry.bind("<Return>", on_enter)
```

### 7️⃣ Entry Validation – Restricting Input
- 🔹 Allow Only Numbers 

```py
def validate_input(P):
    return P.isdigit()  # Returns True if input is a number

vcmd = root.register(validate_input)  
entry = tk.Entry(root, validate="key", validatecommand=(vcmd, "%P"))
entry.pack(pady=10)
```
######  Blocks non-numeric input dynamically.

<h6>
  isalpha() = just for text <br> 
  isdigit() = just for digit <br> 
  isalnum() =  Alphanumeric <br>
</h6>

## 8️⃣ Disabling & Enabling Entry
 
```py
entry.config(state="disabled")  # Makes entry non-editable
entry.config(state="normal")    # Enables entry again
entry.config(state="readonly")  # Readonly Entry (Uneditable)
```

<br>
<br>

## Text
###### The Text widget in Tkinter is used for multi-line text input and text display, unlike the Entry widget, which only supports single-line input.

### Text Widget Summary

<h6>

| Method	| Description| 	Usage| 
|------------|----------|----------------|
| config()| 	Configures or updates the Text widget’s properties (e.g., font, color).| 	text.config(font=("Arial", 12), bg="lightyellow")| 
| configure()	Same as config(),|  updates Text widget properties.| 	text.configure(state="disabled")| 
| cget()| 	Retrieves the current value of a specific option of the Text widget.| 	text.cget("height")| 
| get()	| Retrieves text from the Text widget from the specified range.	| text.get("1.0", tk.END)| 
| insert()	| Inserts text at a specified position in the Text widget.	| text.insert("1.0", "This is a test text")| 
| delete()	| Deletes text from the Text widget within a specific range.	| text.delete("1.0", "2.0")| 
| tag_add()	| Adds a tag to a portion of the text, useful for styling.	| text.tag_add("highlight", "1.0", "2.0")| 
| tag_remove()| 	Removes a tag from the text.	| text.tag_remove("highlight", "1.0", "2.0")| 
| tag_configure()	| Configures the style properties of a tag (e.g., foreground color).| 	text.tag_configure("highlight", foreground="red")| 
| tag_bind()	| Binds an event to a tag (e.g., click on a highlighted text).| 	text.tag_bind("highlight", "<Button-1>", callback)| 
| mark_set()| 	Sets the position of a text mark (position for cursor).	| text.mark_set("insert", "1.0")| 
| mark_gravity()| 	Sets the gravity (direction) of the insertion mark (cursor).	| text.mark_gravity("insert", "right")| 
| see()	| Scrolls the Text widget to make a given line visible.| 	text.see("1.0")| 
| window_create()| 	Creates a window inside the Text widget (for embedding widgets).	| text.window_create("1.0", window=my_button)| 
| index()| 	Returns the index of the character at a specific position in the text.	| text.index("insert")| 
| xview()	| Controls the horizontal view of the text widget (scrolling).	| text.xview("moveto", 0.5)| 
| yview()| 	Controls the vertical view of the text widget (scrolling).| 	text.yview("moveto", 0.5)| 
| bind()	| Binds an event (e.g., key press, mouse click) to the Text widget.	| text.bind("<KeyPress>", function)| 
| unbind()| 	Unbinds an event from the Text widget.| text.unbind("<KeyPress>")| 
| after()	| Calls a function after a specified amount of time.	| text.after(1000, function)| 
| update()	| Updates the widget and redraws it.	| text.update()| 
| update_idletasks()	| Forces the widget to process its pending tasks.	| text.update_idletasks()| 
  
</h6>

```py
text_widget = tk.Text(root, height=5, width=40)  # Multi-line input
text_widget.pack(pady=10)
```
<h6> 

2️⃣ Common Text Widget Properties
| Property | 	Description| 
| ---------|---------------|
| height	| Number of visible lines| 
| width	| Number of characters per line| 
| fg / foreground	| Text color| 
| bg / background	| Background color| 
| font	| Font style and size| 
| bd / borderwidth	| Border thickness| 
| relief	| Border style (flat, raised, sunken, etc.)| 
| state	| normal (editable) or disabled (read-only)| 
| wrap	| Controls text wrapping (none, word, char)| 
| insertbackground	| Color of the cursor| 
| exportselection	| Controls text copying to the clipboard| 


</h6>


### 3️⃣ Getting & Setting Text
- 🔹 Retrieve Text (get())

```py
def show_text():
    content = text_widget.get("1.0", tk.END)  # Get text from line 1, character 0
    print(content)

btn = tk.Button(root, text="Get Text", command=show_text)
btn.pack(pady=10)

```
######   Retrieves all text from the Text widget.


- 🔹 Insert Text (insert())
```py
text_widget.insert("1.0", "Hello AN Mamun!")  # Inserts at line 1, position 0
```
###### Inserts text at the beginning.

- 🔹 Delete Text (delete())
```
text_widget.delete("1.0", tk.END)  # Deletes all text
```
###### Clears the entire text box.



### 4️⃣ Dynamic Text Updates

- 🔹 Change Text Dynamically
```py
def change_text():
    text_widget.delete("1.0", tk.END)
    text_widget.insert("1.0", "New Dynamic Text!")

btn = tk.Button(root, text="Change Text", command=change_text)
btn.pack(pady=10) 
```
######  Replaces text dynamically when clicked.


  
### 5️⃣ Read-Only Text Widget
```py
text_widget.config(state="disabled")  # Makes it read-only
text_widget.config(state="normal")    # Enables editing again
```
### 6️⃣ Text Wrapping Options
<h6>

| Wrap Mode	 |  Description |
| -------------|------------|
| none	| No wrapping; horizontal scroll required | 
| word | 	Wraps only at word boundaries | 
| char | 	Wraps at any character | 
  
</h6>

```py
text_widget.config(wrap="word")  # Ensures clean word wrapping
```
######  Prevents words from being cut off mid-line.
 
### 8️⃣ Scrollbars for Large Text Areas

```py
scrollbar = tk.Scrollbar(root, command=text_widget.yview)
text_widget.config(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
text_widget.pack()
```
######  Adds a vertical scrollbar.


### 9️⃣ Changing Text Color Dynamically
```py
def change_text_color():
    text_widget.tag_configure("color", foreground="red")
    text_widget.tag_add("color", "1.0", "end")

btn = tk.Button(root, text="Change Color", command=change_text_color)
btn.pack(pady=10)

```
######  Changes all text to red dynamically.



### 🔟 Highlighting Specific Words
```py
def highlight_text():
    text_widget.tag_configure("highlight", background="yellow")
    text_widget.tag_add("highlight", "1.0", "1.5")  # Highlights first 5 characters

btn = tk.Button(root, text="Highlight Text", command=highlight_text)
btn.pack(pady=10)

```
######  Highlights a portion of the text.


 
<br>
<br>

## Frame
###### The Frame widget in Tkinter is a container widget used to group and organize other widgets inside it. It helps structure complex layouts and can be customized with borders, colors, and dynamic behavior.

### Frame Widget Summary
<h6>

| Method	| Description	|  Usage | 
|---------|-------------|------------|
| config()| 	Configures or updates the Frame's properties (e.g., background color, border).| 	frame.config(bg="lightblue", relief="solid")| 
| configure()	| Same as config(), updates Frame properties.| 	frame.configure(width=200, height=200)| 
| cget()	| Retrieves the current value of a specific option of the Frame.| 	frame.cget("bg")| 
| pack()	| Places the Frame widget in the parent widget using the pack geometry manager.| 	frame.pack(side="top", fill="x", padx=10)| 
| grid()| 	Places the Frame widget in a grid layout (if used).| 	frame.grid(row=0, column=0)| 
| place()	| Places the Frame widget at a specific location with precise x and y coordinates.| 	frame.place(x=50, y=100)| 
| destroy()	| Destroys the Frame widget (removes it from the interface).	| frame.destroy()| 
| bind()	| Binds a function to a specific event (e.g., mouse hover, click).	| frame.bind("<Button-1>", function)| 
| unbind()	| Unbinds an event from the Frame widget.| 	frame.unbind("<Button-1>")| 
| after()	| Calls a function after a specified amount of time.| 	frame.after(1000, function)| 
| update()	| Updates the widget and redraws it (useful for dynamic content updates).| 	frame.update()| 
| update_idletasks()	| Forces the widget to process its pending tasks.| 	frame.update_idletasks()| 
| focus_set()	| Sets the focus to the Frame widget (if it can receive focus).| 	frame.focus_set()| 
| tk_focusNext()	| Moves focus to the next widget in the tab order.	| frame.tk_focusNext()| | 
| tk_focusPrev()| 	Moves focus to the previous widget in the tab order.| 	frame.tk_focusPrev()
  
</h6>



## 1️⃣ Creating a Basic Frame

```py
import tkinter as tk

root = tk.Tk()
root.title("Basic Frame Example")

frame = tk.Frame(root, width=300, height=150, bg="lightblue")
frame.pack(pady=10)

root.mainloop()
```
## 2️⃣ Frame Widget Properties

<h6> 
  
| Property	|  Description | 
| ----------| --------------|
| bg / background	| Background color | 
| bd / borderwidth| Border thickness | 
| relief	| Border style (flat, raised, sunken, ridge, solid, groove) | 
| width| Frame width in pixels | 
| height	| Frame height in pixels | 
| padx / pady	| Internal padding inside the frame | 
| highlightbackground	| Border color | 
| highlightthickness	| Thickness of border highlight | 
</h6>

```py
frame = tk.Frame(root, width=300, height=150, bg="lightblue", bd=3, relief="ridge", highlightbackground="black", highlightthickness=2)
frame.pack(pady=10)
```

## 3️⃣ Adding Widgets Inside a Frame
```py
frame = tk.Frame(root, bg="lightgray", padx=10, pady=10)
frame.pack(pady=10)

label = tk.Label(frame, text="Inside Frame", font=("Arial", 14), bg="lightgray")
label.pack()

btn = tk.Button(frame, text="Click Me")
btn.pack(pady=5)

```
###### Groups multiple widgets inside a frame.


## 4️⃣ Changing Frame Properties Dynamically
```py
def change_color():
    frame.config(bg="yellow")

btn = tk.Button(root, text="Change Color", command=change_color)
btn.pack(pady=10)

```
######   Changes the frame’s background dynamically.

```py
outer_frame = tk.Frame(root, bg="blue", padx=10, pady=10)
outer_frame.pack(pady=10)

inner_frame = tk.Frame(outer_frame, bg="white", padx=10, pady=10, bd=2, relief="sunken")
inner_frame.pack()

tk.Label(inner_frame, text="I'm inside an inner frame").pack()

```
######  Creates a nested layout for better organization.


## 5️⃣ Nested Frames (Frames Inside Frames)
```py
frame = tk.Frame(root, bg="gray")
frame.pack(pady=10)

tk.Label(frame, text="Row 0, Col 0").grid(row=0, column=0, padx=5, pady=5)
tk.Label(frame, text="Row 0, Col 1").grid(row=0, column=1, padx=5, pady=5)
tk.Label(frame, text="Row 1, Col 0").grid(row=1, column=0, padx=5, pady=5)
tk.Label(frame, text="Row 1, Col 1").grid(row=1, column=1, padx=5, pady=5)

```
######  Uses grid() for structured layout inside a frame.
 
## 6️⃣ Using grid() Inside a Frame

```py
frame = tk.Frame(root, bg="gray")
frame.pack(pady=10)

tk.Label(frame, text="Row 0, Col 0").grid(row=0, column=0, padx=5, pady=5)
tk.Label(frame, text="Row 0, Col 1").grid(row=0, column=1, padx=5, pady=5)
tk.Label(frame, text="Row 1, Col 0").grid(row=1, column=0, padx=5, pady=5)
tk.Label(frame, text="Row 1, Col 1").grid(row=1, column=1, padx=5, pady=5)

```
######  Uses grid() for structured layout inside a frame.


## 7️⃣ Hiding & Showing Frames Dynamically
- 🔹 Hide Frame (pack_forget())
```py
def hide_frame():
    frame.pack_forget()

btn_hide = tk.Button(root, text="Hide Frame", command=hide_frame)
btn_hide.pack(pady=10)

```
###### Hides the frame but doesn’t destroy it.
- 🔹 Show Frame (pack())
```py
def show_frame():
    frame.pack(pady=10)

btn_show = tk.Button(root, text="Show Frame", command=show_frame)
btn_show.pack(pady=10)

```
###### Brings back the hidden frame.


## 8️⃣ Destroying a Frame
```py
def destroy_frame():
    frame.destroy()

btn_destroy = tk.Button(root, text="Destroy Frame", command=destroy_frame)
btn_destroy.pack(pady=10)

```
###### Permanently removes the frame and all its widgets.


## 9️⃣ Making a Resizable Frame
```py
frame.pack_propagate(False)  # Prevents frame from resizing
frame.config(width=300, height=200)

```
###### Keeps frame size fixed, preventing automatic resizing.


## 🔟 Example: Full Working App with Frame Toggle

```py
import tkinter as tk
root = tk.Tk()
root.title("Frame Toggle Example")

frame = tk.Frame(root, width=300, height=150, bg="lightgray", bd=2, relief="ridge")
frame.pack(pady=10)
tk.Label(frame, text="Hello, I'm inside a Frame!", font=("Arial", 14), bg="lightgray").pack()

def toggle_frame():
    if frame.winfo_ismapped():  # Check if frame is visible
        frame.pack_forget()
        btn_toggle.config(text="Show Frame")
    else:
        frame.pack(pady=10)
        btn_toggle.config(text="Hide Frame")

btn_toggle = tk.Button(root, text="Hide Frame", command=toggle_frame)
btn_toggle.pack(pady=10)

root.mainloop()

```
######  Toggles the visibility of the frame dynamically.




<br>
<br>

## Menu
###### The Menu widget in Tkinter is used to create drop-down menus, context menus (right-click menus), and menubars in GUI applications. It provides an easy way to add navigation and actions to your application.


#### Menu widget Summary
<h6> 

| Method	| Description	| Usage| 
|-----------|--------------|--------------|
| add_command()| 	Adds a command (action) to the menu.| 	menu.add_command(label="Option", command=function)| 
| add_separator()| 	Adds a separator line between menu items for better organization.	| menu.add_separator()| 
| add_checkbutton()| 	Adds a checkable item (checkbox).	| menu.add_checkbutton(label="Option", variable=variable, command=function)| 
| add_radiobutton()	| Adds a radio button (single option selection).	| menu.add_radiobutton(label="Option", variable=variable, value="value", command=function)| 
| entryconfig()	| Modifies or updates a menu item’s configuration (e.g., enabling/disabling).| 	menu.entryconfig(index_or_label, state="disabled", **kwargs)| 
| post()	| Displays a menu at specific screen coordinates (used in context menus).| 	menu.post(x, y)| 
| add_cascade()	| Adds a sub-menu (cascade menu) to a parent menu.| 	menu.add_cascade(label="Submenu", menu=submenu)| 
| delete()	| Deletes a menu item by its index or label.	| menu.delete(index_or_label)| 
| index()	| Returns the index of a menu item by label.| 	menu.index("Item Label")| 
| invoke()	| Simulates a click on a menu item programmatically.	| menu.invoke(index_or_label)| 
| type()	| Returns the type of the menu item (e.g., command, checkbutton, etc.).| 	menu.type(index_or_label)| 
| bind()	| Binds an event to a menu item (e.g., hover, click).| 	menu.bind("<Event>", function)
| tearoff()	| Disables or enables the dashed line separating the menu from the menu bar.| 	menu.config(tearoff=0) (Disable dashed line)| 


</h6>

## 1️⃣ Creating a Basic Menu Bar
##### The Menu widget is usually attached to the root window using root.config(menu=menu_bar).
```py
import tkinter as tk

root = tk.Tk()
root.title("Basic Menu Example")
root.geometry("300x200")

menu_bar = tk.Menu(root)

# Add File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

menu_bar.add_cascade(label="File", menu=file_menu)

# Attach menu to root window
root.config(menu=menu_bar)

root.mainloop()

```

## 2️⃣ Menu Widget Properties

<h6>

| Property	| Description| 
| -----------|--------------| 
| tearoff | 	Removes the dashed line if set to 0 (default is 1)| 
| bg / background	| Background color of the menu| 
| fg / foreground	| Text color of the menu items| 
| activebackground | 	Background color when an item is hovered| 
| activeforeground	| Text color when an item is hovered| 
| disabledforeground	| Color of disabled menu items| 
| font	| Font style of the menu items| 
| postcommand	| Function called before showing the menu| 
| cursor| 	Cursor style when hovering over menu| 

</h6>



## 3️⃣ Adding More Menu Items

- 🔹 Adding More Options
```py
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")

menu_bar.add_cascade(label="Edit", menu=edit_menu) 
```
######  Adds an "Edit" menu with Cut, Copy, and Paste options.

## 4️⃣ Adding Checkbuttons & Radiobuttons
- 🔹 Checkbutton Menu
- - Used to toggle an option on or off.

```py
show_status = tk.BooleanVar()

def toggle_status():
    print("Status Bar:", show_status.get())

view_menu = tk.Menu(menu_bar, tearoff=0)
view_menu.add_checkbutton(label="Show Status Bar", variable=show_status, command=toggle_status)

menu_bar.add_cascade(label="View", menu=view_menu)
```

###### ✅ Toggles a status bar when checked/unchecked.

- 🔹 Radiobutton Menu
- - Used when one option must be selected.

```py
theme_var = tk.StringVar(value="Light")

def change_theme():
    print("Selected Theme:", theme_var.get())

theme_menu = tk.Menu(menu_bar, tearoff=0)
theme_menu.add_radiobutton(label="Light Mode", variable=theme_var, value="Light", command=change_theme)
theme_menu.add_radiobutton(label="Dark Mode", variable=theme_var, value="Dark", command=change_theme)

menu_bar.add_cascade(label="Themes", menu=theme_menu)

```
######  Lets users select a theme (Light or Dark).





## 5️⃣ Dynamic Menu Changes
🔹 Add/Remove Menu Items at Runtime
```py
def add_menu_item():
    tools_menu.add_command(label="New Tool", command=lambda: print("New Tool Clicked"))

tools_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Tools", menu=tools_menu)

btn = tk.Button(root, text="Add Menu Item", command=add_menu_item)
btn.pack(pady=10)

```
###### Dynamically adds a menu item when the button is clicked.



## 6️⃣ Context (Right-Click) Menus
```py
context_menu = tk.Menu(root, tearoff=0)
context_menu.add_command(label="Cut")
context_menu.add_command(label="Copy")
context_menu.add_command(label="Paste")

def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)

root.bind("<Button-3>", show_context_menu)  # Right-click event

root.mainloop()

```
######   Opens a right-click menu when the user right-clicks.



## 7️⃣ Disabling & Enabling Menu Items
```py
def disable_save():
    file_menu.entryconfig("Save", state="disabled")

file_menu.add_command(label="Disable Save", command=disable_save)

```
###### Disables the "Save" menu item.


##8️⃣ Example: Full Working App with Menus

```py
import tkinter as tk

root = tk.Tk()
root.title("Full Menu Example")
root.geometry("400x300")

# Main Menu Bar
menu_bar = tk.Menu(root)

# File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=lambda: print("Open Clicked"))
file_menu.add_command(label="Save", command=lambda: print("Save Clicked"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Edit Menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# View Menu with Checkbutton
show_status = tk.BooleanVar()
view_menu = tk.Menu(menu_bar, tearoff=0)
view_menu.add_checkbutton(label="Show Status Bar", variable=show_status)
menu_bar.add_cascade(label="View", menu=view_menu)

# Theme Menu with Radiobutton
theme_var = tk.StringVar(value="Light")
theme_menu = tk.Menu(menu_bar, tearoff=0)
theme_menu.add_radiobutton(label="Light Mode", variable=theme_var, value="Light")
theme_menu.add_radiobutton(label="Dark Mode", variable=theme_var, value="Dark")
menu_bar.add_cascade(label="Themes", menu=theme_menu)

# Context (Right-Click) Menu
context_menu = tk.Menu(root, tearoff=0)
context_menu.add_command(label="Cut")
context_menu.add_command(label="Copy")
context_menu.add_command(label="Paste")

def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)

root.bind("<Button-3>", show_context_menu)  # Right-click event

# Attach menu to root window
root.config(menu=menu_bar)

root.mainloop()

```


<h6> 
✅ Features: <br> 

File, Edit, View, and Themes menu<br> 
Checkbutton (Show Status Bar)<br> 
Radiobuttons (Theme selection)<br> 
Right-click context menu<br> 

</h6>


## Checkbutton
## Radiobutton
## Listbox
## Combobox
## Scale
## Progressbar


<br>
<br>
<br>
<br>


## Tkinter Geometry Management 
##### Tkinter provides three geometry managers to position and arrange widgets inside a parent widget:

- pack() – Simple and easy to use, stacks widgets vertically or horizontally.
- grid() – Uses a table-like structure with rows and columns.
- place() – Provides absolute positioning using x and y coordinates.

1. pack() Geometry Manager
The pack() manager arranges widgets in a block-wise manner (either top-to-bottom or left-to-right).

### Common Options in pack()

| Option	| Description| 
|--------------|-----------------|
| side	| Specifies which side to place the widget (top, bottom, left, right).| 
| fill| 	Expands the widget to fill available space (x, y, or both).| 
| expand| 	Expands the widget within the available space (True or False).| 
| padx	| Adds horizontal padding (spacing).| 
| pady	| Adds vertical padding (spacing).| 


#### Example of pack()

```py
import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

# Create a frame with light blue background
frame = tk.Frame(root, bg="lightblue")
frame.pack(fill="both", expand=True, padx=10, pady=10)

# Button 1 at the top
btn1 = tk.Button(frame, text="Top Button")
btn1.pack(side="top", fill="x")

# Button 2 at the left
btn2 = tk.Button(frame, text="Left Button")
btn2.pack(side="left")

# Button 3 at the right
btn3 = tk.Button(frame, text="Right Button")
btn3.pack(side="right")

# Button 4 at the bottom
btn4 = tk.Button(frame, text="Bottom Button")
btn4.pack(side="bottom")

# Center button
center_button = tk.Button(frame, text="Center Button")
center_button.pack(side="top", expand=True)

# Add buttons to all four corners using place()
top_left_btn = tk.Button(frame, text="Top Left")
top_left_btn.place(relx=0.0, rely=0.0, anchor="nw")

top_right_btn = tk.Button(frame, text="Top Right")
top_right_btn.place(relx=1.0, rely=0.0, anchor="ne")

bottom_left_btn = tk.Button(frame, text="Bottom Left")
bottom_left_btn.place(relx=0.0, rely=1.0, anchor="sw")

bottom_right_btn = tk.Button(frame, text="Bottom Right")
bottom_right_btn.place(relx=1.0, rely=1.0, anchor="se")

root.mainloop()

```


## 2. grid() Geometry Manager
#### The grid() manager arranges widgets in a table format (rows and columns).

### Common Options in grid()

| Option | 	Description | 
|-------|-----------------|
| row	| Defines the row index (starting from 0).| 
| column | Defines the column index (starting from 0).| 
| padx	| Adds horizontal padding.| 
| pady	| Adds vertical padding.| 
| sticky | 	Aligns the widget within the grid cell (n, s, e, w).| 

Example of grid()
```py
import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Email:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)

submit_btn = tk.Button(root, text="Submit")
submit_btn.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()

```

- 🔹 sticky="w" aligns the widget to the left (west).
- 🔹 columnspan=2 makes the button span across two columns.







## 3. place() Geometry Manager
##### The place() manager positions widgets precisely using x and y coordinates.

Common Options in place()

| Option| 	Description| 
|-----------|------------------|
| x| 	X-coordinate for the widget.| 
| y| 	Y-coordinate for the widget.| 
| relx	| Relative X-position (0.0 to 1.0).| 
| rely| 	Relative Y-position (0.0 to 1.0).| 
| anchor| 	Controls the positioning (center, nw, se, etc.).| 


##Example of place()
```py
import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

label = tk.Label(root, text="Hello AN Mamun!", font=("Arial", 14))
label.place(x=50, y=50)

button = tk.Button(root, text="Click Me")
button.place(relx=0.5, rely=0.7, anchor="center")  # Center the button at (50%, 70%)

root.mainloop()

```

- 🔹 place(x=50, y=50) positions the label at exact coordinates.
- 🔹 relx=0.5, rely=0.7 places the button at 50% width and 70% height relative to the window.





Comparison of Geometry Managers
| Feature	| pack()| 	grid()	| place()| 
|-----------|--------|-----------|-------------|
| Uses table layout?| 	❌| 	✅| 	❌| 
| Absolute positioning?| 	❌| 	❌| 	✅| 
| Best for complex layouts?| 	❌| 	✅	| ❌| 
| Best for simple UI?	| ✅| 	✅| 	❌| 
| Widgets can overlap?	| ❌	| ❌	| ✅| 


<br>
<br>
<br>
<br>

## Event Handling 

#### Event Handling in Tkinter
###### Event handling in Tkinter is essential for creating interactive applications. It allows you to handle various actions (such as button clicks, keyboard presses, mouse movement, etc.) and associate them with specific functions.

#### Event Binding in Tkinter
###### In Tkinter, events are triggered by user actions like clicking a button, pressing a key, or moving the mouse. To handle these events, you use the bind() method to associate an event with a handler function.

#### Event Handling Basics
###### An event handler is a function that is executed when an event occurs. You bind an event to a widget, so when that event occurs on the widget, the handler function is called.



### Tkinter Event Handling

- This document provides a summary of the common events in Tkinter, their descriptions, and usage examples.

<h6> 
  
| **Event Name**              | **Description**                                                   | **Example**                                                      |
|-----------------------------|-------------------------------------------------------------------|------------------------------------------------------------------|
| `<Button-1>`                | Left mouse button click                                           | `btn.bind("<Button-1>", on_click)`                               |
| `<Button-2>`                | Middle mouse button click                                         | `btn.bind("<Button-2>", on_click)`                               |
| `<Button-3>`                | Right mouse button click                                          | `btn.bind("<Button-3>", on_click)`                               |
| `<ButtonRelease-1>`         | Left mouse button release                                         | `btn.bind("<ButtonRelease-1>", on_release)`                      |
| `<ButtonRelease-2>`         | Middle mouse button release                                       | `btn.bind("<ButtonRelease-2>", on_release)`                      |
| `<ButtonRelease-3>`         | Right mouse button release                                        | `btn.bind("<ButtonRelease-3>", on_release)`                      |
| `<Motion>`                  | Mouse movement over the widget                                    | `widget.bind("<Motion>", on_move)`                               |
| `<Enter>`                   | Mouse enters the widget                                           | `widget.bind("<Enter>", on_enter)`                               |
| `<Leave>`                   | Mouse leaves the widget                                           | `widget.bind("<Leave>", on_leave)`                               |
| `<KeyPress>`                | Key press event                                                   | `entry.bind("<KeyPress>", on_key)`                               |
| `<KeyRelease>`              | Key release event                                                 | `entry.bind("<KeyRelease>", on_key_release)`                     |
| `<KeyPress-<key>>`          | Specific key press (e.g., `<KeyPress-a>`)                          | `entry.bind("<KeyPress-a>", on_key_a)`                           |
| `<FocusIn>`                 | Widget gains focus                                                | `entry.bind("<FocusIn>", on_focus_in)`                           |
| `<FocusOut>`                | Widget loses focus                                                | `entry.bind("<FocusOut>", on_focus_out)`                         |
| `<MouseWheel>`              | Mouse wheel scroll event                                          | `root.bind("<MouseWheel>", on_scroll)`                           |
| `<Destroy>`                 | Widget or window is destroyed (closed)                             | `root.bind("<Destroy>", on_destroy)`                             |
| `<Configure>`               | Widget's size or position is changed                               | `widget.bind("<Configure>", on_resize)`                          |
| `<Expose>`                  | Widget is exposed after being obscured by other widgets           | `widget.bind("<Expose>", on_expose)`                             |
| `<Deactivate>`              | Window is deactivated                                             | `root.bind("<Deactivate>", on_deactivate)`                       |
| `<Activate>`                | Window is activated                                               | `root.bind("<Activate>", on_activate)`                           |
| `<Map>`                     | Widget is mapped to the screen                                    | `widget.bind("<Map>", on_map)`                                    |
| `<Unmap>`                   | Widget is unmapped (removed from the screen)                      | `widget.bind("<Unmap>", on_unmap)`                               |
| `<Visibility>`              | Widget's visibility is changed                                    | `widget.bind("<Visibility>", on_visibility_change)`              |
| `<VirtualEvent>`            | Custom event (programmatically generated)                         | `widget.bind("<CustomEvent>", on_custom_event)`                   |
| `<Delete>`                  | Delete operation on widget                                        | `widget.bind("<Delete>", on_delete)`                              |
| `<Shift-Left>`              | Shift + Left arrow key press                                      | `root.bind("<Shift-Left>", on_shift_left)`                        |
| `<Alt-Up>`                  | Alt + Up arrow key press                                          | `root.bind("<Alt-Up>", on_alt_up)`                                |

</h6>

<br>
<br>


### Syntax of bind()
```py
 widget.bind("<event>", handler_function)
```
- widget: The widget that will listen for events (e.g., button, entry, etc.).
- "\<event\>": The event to listen for (e.g., \<Button-1\>, \<KeyPress\>, etc.).
- handler_function: The function to be executed when the event occurs.


Common Events
- Button Click: \<Button-1\> (Left mouse button), \<Button-2\> (Middle button), \<Button-3\> (Right button).
- Key Press: \<KeyPress-A\>, \<KeyPress-Return\>.
- Mouse Movement: \<Motion\>.
- Window Close: \<Destroy\>.






### 1. Handling Mouse Events
##### You can use mouse events such as clicks and movements to trigger functions.

### Example: Mouse Click Event
```py
import tkinter as tk

def on_click(event):
    print("Mouse clicked at:", event.x, event.y)

root = tk.Tk()
root.geometry("300x200")

btn = tk.Button(root, text="Click me")
btn.pack(pady=20)

# Bind the left mouse button click event to the button
btn.bind("<Button-1>", on_click)

root.mainloop()

```
 

 
### Explanation:  
- When the button is clicked, the on_click() function will be called. The event object contains information about the click, such as the mouse coordinates (event.x, event.y).
 



### Example: Mouse Movement Event
```py
import tkinter as tk

def on_move(event):
    print(f"Mouse moved to ({event.x}, {event.y})")

root = tk.Tk()
root.geometry("300x200")

# Bind the mouse movement event to the root window
root.bind("<Motion>", on_move)

root.mainloop()

```

### Explanation:
- Every time the mouse moves within the window, the on_move() function will print the mouse's coordinates.




## 2. Handling Keyboard Events
##### Keyboard events allow you to handle key presses and releases.

```py
import tkinter as tk

def on_key_press(event):
    print(f"Key pressed: {event.keysym}")

root = tk.Tk()
root.geometry("300x200")

# Bind a key press event to the root window
root.bind("<KeyPress>", on_key_press)

root.mainloop()

```

### Explanation:
- Whenever a key is pressed, the on_key_press() function will be triggered. The event.keysym contains the name of the key that was pressed.

## Example: Specific Key Press
 
```py
import tkinter as tk

def on_space_key(event):
    print("Space key pressed!")

root = tk.Tk()
root.geometry("300x200")

# Bind the space key to a specific handler
root.bind("<KeyPress-space>", on_space_key)

root.mainloop()

```

### Explanation:
- The on_space_key() function is triggered when the spacebar key is pressed.







## 3. Handling Window Events
#### You can bind events to the window (root) itself to handle actions like resizing or closing the window.

### Example: Window Close Event
 
```py
import tkinter as tk

def on_close(event):
    print("Window is closing!")

root = tk.Tk()
root.geometry("300x200")

# Bind the window close event
root.bind("<Destroy>", on_close)

root.mainloop()

```
### Explanation:
- The on_close() function will be executed when the window is about to be destroyed (closed).



## 4. Event Object
#### The event object is passed to the event handler. It contains useful information such as the type of event, mouse coordinates, key pressed, etc.

- Here are some useful attributes of the event object:

- event.x, event.y: Mouse coordinates when the event is triggered.
- event.keysym: The symbolic name of the key pressed (e.g., "a", "space").
- event.widget: The widget that triggered the event.


## 5. Event Handling for Widgets
#### You can bind events to specific widgets like Button, Label, Entry, etc.

### Example: Handling Button Click

```py
import tkinter as tk

def on_button_click(event):
    print("Button clicked!")

root = tk.Tk()
root.geometry("300x200")

# Create a button and bind the click event
btn = tk.Button(root, text="Click me")
btn.pack(pady=20)
btn.bind("<Button-1>", on_button_click)

root.mainloop()

```
### Explanation:
- The on_button_click() function will be triggered when the button is clicked with the left mouse button.


## 6. Handling Multiple Events
#### You can bind multiple events to the same widget or window.

### Example: Handling Multiple Events
```py
import tkinter as tk

def on_click(event):
    print(f"Clicked at ({event.x}, {event.y})")

def on_key(event):
    print(f"Key pressed: {event.keysym}")

root = tk.Tk()
root.geometry("300x200")

# Bind mouse click and key press events
root.bind("<Button-1>", on_click)
root.bind("<KeyPress>", on_key)

root.mainloop()

```
### Explanation:
- The window will listen for both mouse click and key press events, and trigger the respective handler functions.

### Example: Handling Mouse Wheel Scroll Event
```py
import tkinter as tk

def on_scroll(event):
    if event.delta > 0:
        print("Scrolled Up!")
    else:
        print("Scrolled Down!")

root = tk.Tk()
root.geometry("300x200")

# Bind mouse wheel scroll event to the root window
root.bind("<MouseWheel>", on_scroll)

root.mainloop()

```
### Explanation:
- The on_scroll() function checks the event.delta value. Positive values indicate scrolling up, and negative values indicate scrolling down.

  
   
### Best Practices
- Event handlers should be concise: Keep your event handler functions short and focused on one task.
- Use bind() for flexible event handling: bind() is more flexible than directly using widget commands for simple actions (e.g., button clicks).
- Clean up event bindings: If necessary, you can unbind events using widget.unbind("<event>").

<br>
<br>
<br>
<br>
<br>


# Tkinter Variable Classes

<h6> 
In Tkinter, variable classes provide a way to manage and interact with widget data in a more efficient and flexible manner. These variables are tied to Tkinter widgets and can be used to track changes in widget states, making it easier to read or update widget values programmatically. Tkinter provides several variable classes to handle different types of data, and they are particularly useful when creating dynamic or interactive applications.
</h6>


## Tkinter Variable Classes

Tkinter provides variable classes that are tied to widgets, allowing for easier management and dynamic updates of widget data. These variables are essential when you want to interact programmatically with widget values.

## Variable Classes

<h6> 
  
| **Variable Class** | **Description**                                      | **Common Usage**                           | **Example**                                  |
|--------------------|------------------------------------------------------|--------------------------------------------|----------------------------------------------|
| `StringVar`        | Manages string values                                | `Entry`, `Label`, `Text`                   | `textvariable=my_string`                     |
| `IntVar`           | Manages integer values                               | `Radiobutton`, `Checkbutton`, `Scale`      | `variable=selected`                          |
| `DoubleVar`        | Manages floating-point (double) values               | `Scale`, `Entry`                           | `variable=slider_value`                      |
| `BooleanVar`       | Manages boolean (True/False) values                  | `Checkbutton`, `Radiobutton`               | `variable=check_var`                         |
| `BitmapVar`        | Manages bitmap (image) values (not commonly used)    | Widgets with bitmap support                | `variable=bitmap_var`                        |
| `CursorVar`        | Manages cursor values (not commonly used)            | Widget cursor state                        | `variable=cursor_var`                        |
  
</h6>

## Key Features of Tkinter Variables
- **`get()`**: Fetches the current value of the variable.
- **`set(value)`**: Sets a new value for the variable.
- **`trace_add(mode, callback)`**: Adds a callback function to be triggered on variable changes.
- **`trace_remove(mode, callback)`**: Removes the callback function added by `trace_add()`.


<br>
<br>
<br>


### 1. Tkinter Variable Classes
- The main Tkinter variable classes are:

- `StringVar`: Used for managing strings.
- `IntVar`: Used for managing integer values.
- `DoubleVar`: Used for managing floating-point values.
- `BooleanVar`: Used for managing boolean values (True/False).
- `BitmapVar`: Used for managing bitmap values (not commonly used).
- `CursorVar`: Used for managing cursor values (not commonly used).
- Each of these variable classes provides methods for setting, getting, and tracking changes to the data they hold.

### 2. Common Methods for Tkinter Variables
- All Tkinter variable classes (like StringVar, IntVar, etc.) have common methods:

- get(): Returns the current value of the variable.
- set(value): Sets a new value to the variable.
- trace_add(mode, callback): Adds a callback function that is triggered when the variable changes (can be "write" or "read" mode).
- trace_remove(mode, callback): Removes the callback function added by trace_add().


## 3. StringVar Example
- StringVar is used for handling string data, and it's most often used with widgets like Entry, Label, Text, etc.

### Example: Using StringVar

```py
import tkinter as tk

def update_label():
    label.config(text=my_string.get())

root = tk.Tk()

# Create a StringVar
my_string = tk.StringVar()

# Create a label that will show the value of my_string
label = tk.Label(root, textvariable=my_string, font=("Arial", 16))
label.pack(pady=20)

# Create an entry widget where the user can type text
entry = tk.Entry(root, textvariable=my_string, font=("Arial", 14))
entry.pack(pady=20)

# Button to update the label with the entry text
btn = tk.Button(root, text="Update Label", command=update_label)
btn.pack(pady=20)

root.mainloop()
```

#### Explanation:
- In this example, the value of my_string is bound to both the Label and the Entry. When the user types in the Entry, the Label updates automatically.








## 4. IntVar Example
- IntVar is used for managing integer values. It's commonly used with checkboxes, radiobuttons, or anywhere integers are needed.

#### Example: Using IntVar 

```py
import tkinter as tk

def show_value():
    print("Selected Value:", selected.get())

root = tk.Tk()

# Create an IntVar
selected = tk.IntVar()

# Create radio buttons that update the IntVar
radio1 = tk.Radiobutton(root, text="Option 1", variable=selected, value=1)
radio2 = tk.Radiobutton(root, text="Option 2", variable=selected, value=2)
radio3 = tk.Radiobutton(root, text="Option 3", variable=selected, value=3)

radio1.pack(pady=10)
radio2.pack(pady=10)
radio3.pack(pady=10)

# Button to show the selected value
btn = tk.Button(root, text="Show Selected Value", command=show_value)
btn.pack(pady=20)

root.mainloop()

```


#### Explanation: 
- Here, the IntVar selected is tied to the radio buttons. When one of the radio buttons is clicked, the corresponding value (1, 2, or 3) is set in selected.






5. DoubleVar Example
- DoubleVar is used for managing floating-point values. This is useful for numeric inputs, such as sliders or any widget requiring decimal values.

#### Example: Using DoubleVar

```py
import tkinter as tk

def update_value():
    print("Slider Value:", slider_value.get())

root = tk.Tk()

# Create a DoubleVar
slider_value = tk.DoubleVar()

# Create a scale (slider) widget
slider = tk.Scale(root, variable=slider_value, from_=0, to_=100, orient="horizontal")
slider.pack(pady=20)

# Button to display the current value of the slider
btn = tk.Button(root, text="Show Slider Value", command=update_value)
btn.pack(pady=20)

root.mainloop()

```
#### Explanation: 
- In this example, the DoubleVar slider_value holds the value of the slider. When the user moves the slider, the slider_value updates accordingly.







6. BooleanVar Example
- BooleanVar is used for managing boolean values (True/False). This is commonly used with Checkbutton or Radiobutton.

#### Example: Using BooleanVar



```py
import tkinter as tk

def show_check_status():
    print("Checkbox Checked:", check_var.get())

root = tk.Tk()

# Create a BooleanVar
check_var = tk.BooleanVar()

# Create a checkbutton widget
checkbutton = tk.Checkbutton(root, text="Agree to Terms", variable=check_var)
checkbutton.pack(pady=20)

# Button to show the checkbutton state
btn = tk.Button(root, text="Show Check Status", command=show_check_status)
btn.pack(pady=20)

root.mainloop()
```

#### Explanation: 
- The BooleanVar check_var tracks the state of the Checkbutton. When the user clicks the button, it prints whether the checkbox is checked (True) or unchecked (False).




7. Tracing Variable Changes
- You can use the trace mechanism to bind callback functions that are called whenever the value of a Tkinter variable changes.

#### Example: Using trace_add to Track Changes
```py
import tkinter as tk

def on_value_change(*args):
    print("The value has changed to:", string_var.get())

root = tk.Tk()

# Create a StringVar
string_var = tk.StringVar()

# Bind the trace to the StringVar
string_var.trace_add("write", on_value_change)

# Create an entry widget that modifies the StringVar
entry = tk.Entry(root, textvariable=string_var, font=("Arial", 14))
entry.pack(pady=20)

root.mainloop()

```
#### Explanation:
- The on_value_change callback is triggered every time the StringVar changes its value (e.g., when the user types in the Entry widget).


<br>
<br>
<br>
<br>

# Time and Date Handling

<h6> 
In Tkinter, handling time and date can be done using Python's built-in datetime module along with Tkinter widgets. You can display the current time or date, allow the user to input time or date, or even implement a countdown or timer.
</h6>

### Time and Date Handling in Tkinter
- Here are some of the main ways to handle time and date in Tkinter:

## 1. Displaying Current Time/Date
- You can display the current time or date in your application using the datetime module. You can update the time dynamically using the after() method in Tkinter to create a clock that updates every second.


Example: Display Current Time

```py
import tkinter as tk
from time import strftime

def time():
    string = strftime('%H:%M:%S %p')  # Current time in hours, minutes, seconds and AM/PM
    lbl.config(text=string)
    lbl.after(1000, time)  # Update the time every second (1000 ms)

root = tk.Tk()
root.title("Clock")

lbl = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
lbl.pack(anchor='center')

time()  # Call the function to start the clock

root.mainloop()

```
#### In this example:
- We used strftime('%H:%M:%S %p') to get the current time in hours, minutes, seconds, and AM/PM format.
- The after(1000, time) method ensures that the time updates every second.



## 2. Date Picker using DateEntry Widget (from tkcalendar library)
#### Tkinter doesn't have a built-in date picker widget, but you can use the tkcalendar module to add a DateEntry widget for selecting dates.

### Installing tkcalendar:
```py
import tkinter as tk
from tkcalendar import DateEntry

root = tk.Tk()
root.title("Date Picker")

cal = DateEntry(root, width=12, background="darkblue", foreground="white", borderwidth=2)
cal.pack(padx=20, pady=20)

root.mainloop()

```

#### In this example:
- The DateEntry widget from the tkcalendar library provides a calendar popup to choose a date.



## 3. Timer using after() method
##### You can implement a countdown timer or a stopwatch by using the after() method to update the time every second.
### Example: Countdown Timer

```py
import tkinter as tk

def countdown(time_left):
    mins, secs = divmod(time_left, 60)
    time_format = '{:02d}:{:02d}'.format(mins, secs)
    lbl.config(text=time_format)
    
    if time_left > 0:
        root.after(1000, countdown, time_left - 1)
    else:
        lbl.config(text="Time's up!")

root = tk.Tk()
root.title("Countdown Timer")

lbl = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
lbl.pack(anchor='center')

countdown(60)  # Start the countdown for 1 minute (60 seconds)

root.mainloop()

```

#### Here:

- divmod(time_left, 60) is used to convert seconds into minutes and seconds.
- after(1000, countdown, time_left - 1) ensures that the timer updates every second.




<br>
<br>
<br>
<br>
# Validation in Tkinter

## 1. Using validate and validatecommand Parameters in Entry Widgets
- The Entry widget in Tkinter has a validate and validatecommand option that allows you to validate user input dynamically.

- validate: Specifies when to validate (e.g., key, focusin, focusout).
- validatecommand: A callback function that is called to perform the validation.
- Example: Allow Only Numeric Input in Entry Widget

```py
import tkinter as tk

def validate_input(char, entry_value):
    if char.isdigit() or char == '':
        return True
    else:
        return False

root = tk.Tk()
root.title("Validation Example")

vcmd = (root.register(validate_input), '%S', '%P')  # Register the validate function

entry = tk.Entry(root, validate='key', validatecommand=vcmd)
entry.pack(pady=20)

root.mainloop()

```
#### Explanation:

- %S represents the character typed by the user.
- %P represents the current value of the entry widget.
- The validate_input function checks if the typed character is a digit or not. If it's not a digit, the validation will fail and prevent the user from entering the character.




2. Validation Using Trace Method in StringVar, IntVar, DoubleVar, and BooleanVar
- You can also use Tkinter's variable classes (StringVar, IntVar, DoubleVar, etc.) and trace the variable changes to apply validation.

- Example: Validate Integer Input Using IntVar

```PY
import tkinter as tk

def on_validate_input(*args):
    value = var.get()
    if value.isdigit():
        lbl.config(text="Valid input")
    else:
        lbl.config(text="Invalid input")

root = tk.Tk()
root.title("Variable Validation Example")

var = tk.StringVar()
var.trace("w", on_validate_input)  # Trace the variable and call on_validate_input

entry = tk.Entry(root, textvariable=var)
entry.pack(pady=20)

lbl = tk.Label(root, text="Enter an integer")
lbl.pack(pady=20)

root.mainloop()

```
### Explanation:

- var.trace("w", on_validate_input) traces any changes to the StringVar and calls on_validate_input when the value changes.
- The function checks if the value entered is a digit and updates the label accordingly.






