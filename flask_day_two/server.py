from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hotdog():
    menu = [
        {"name": "Plain hotdog", "ingredients": ["hotdog, nothing else"]},
        {"name": "Chili dog", "ingredients": ["Hotdog", "chili"]},
        {"name": "Cheese dog", "ingredients": ["Hotdog", "cheese"]},
        {"name": "Chicago-style dog", "ingredients": ["Hotdog", "Onions", "Peppers", "Pickles"]},
        {"name": "Currywarst", "ingredients": ["Bratwurst"]},
        {"name": "Pizza dog", "ingredients": ["Hotdog", "Cheese", "Pepperoni"]}
    ]
    return render_template('index.html', my_menu=menu)


app.run(debug=True)