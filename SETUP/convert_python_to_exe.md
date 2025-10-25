## Convert Python Script to Executable (.exe) File

You can convert a Python script into an executable file using several tools like `PyInstaller`, `cx_Freeze`, `Py2exe`, or `PyOxidizer`.
Below is a simple guide using `PyInstaller`.

<br>
<br>

**Step 1: Install PyInstaller**
```py
pip install pyinstaller
```

**Step 2: Navigate to Your Script Directory**

Use the command prompt or terminal to navigate to the folder that contains your Python script:

```sh
cd path\to\your\script
```

**Step 3: Create Executable File**
<br>

*Command* Run the following command to create the executable file:

```py
pyinstaller your_script_name.py
```
<br>

*Create a Single Executable File*
If you want to create a single .exe file, use:

```py
pyinstaller --onefile your_script_name.py
``` 
<br>

**(Optional) Add a Custom Icon**
If you want to add an icon to your executable file, use:
```py
pyinstaller -w -F -i "picture.ico" your_script_name.py
```


**Step 4: Locate the Output**

After running the command, a dist folder will be created in your project directory.
Inside this folder, you’ll find your standalone .exe file.

