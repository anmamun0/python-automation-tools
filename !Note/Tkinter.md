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

- Root Control Methods [click](#root-control-methods)
- tkinter all Widgets [click](#tkinter-all-Widgets)


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





