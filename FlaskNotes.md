# Flask Setup and Notes

### So you want to start a Flask project? Here's what you need:
* In your terminal, cd to your environments folder
* If you have not already done so, create a virtual environment specifically for running Flask (if you already have a VE with Flask installed, you do not need to do this step)
    * Mac/Linux: python3 -m venv pyEnv
    * Windows: python -m venv pyEnv
* Activate your virtual environment using the proper syntax of your OS
    * Mac/Linux: source pyEnv/bin/activate
    * Windows Cmd Prompt: call pyEnv/Scripts/activate
    * Widnows git bash: source pyEnv/Scripts/activate
* You should see (pyEnv) at the front of your command line now
* Run `pip list` to check if Flask is installed or not
* If Flask isn't installed, install it with `pip install Flask`
* cd over to where you want your project to be (NOT inside your my_environments folder)
* Create a folder named for your project (mkdir folderName)
* Open the folder in VS Code (code .)

#### Basic project setup
* Make a file called `server.py` -- this is the file where your routes and logic live
* Make a folder called `templates` for your html files
* Add an `index.html` file to your templates folder
* If you're planning on using CSS or images, make a folder called `static` 
    * Add another folder inside static called `img`
    * Create a `style.css` file inside static but outside img
* Once all your files are created, go to `server.py` and set up your initial project:
```
from flask import Flask, render_template

app = Flask()

@app.route('/)
def index:
    return render_template('index.html')

app.run(debug=True)
```
* Add something into the body of your `index.html` file
* Run your project from the terminal using `python server.py`
* Go to localhost:5000 and you should now see your first page!