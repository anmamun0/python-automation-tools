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
- tkinter all Widgets


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
 
| Widget	  | Purpose                  | 
|-----------|--------------------------|
| `Label` | 	Displays text or images | 
| `Button` | 	Creates a clickable button | 
| `Entry` | 	Single-line text input | 
| `Text` | 	Multi-line text input | 
| `Frame` | 	Groups widgets together | 
| `Checkbutton` | 	Checkbox for multiple selections | 
| `Radiobutton` | 	Radio button for single selection | 
| `Listbox` | 	Displays a list of items | 
| `Combobox` | 	Dropdown selection menu | 
| `Scale` | 	Slider for selecting values | 
| `Progressbar` | 	Shows progress of a task | 
| `Menu` | 	Creates a menu bar | 


## Label

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



# Button


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







































