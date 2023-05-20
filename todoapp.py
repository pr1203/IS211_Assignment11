from flask import Flask, render_template, redirect, url_for, request
import re
import pickle

app = Flask(__name__)

todo_list = []


@app.route('/')
def display_list():
    return render_template('todo.html', todo_list=todo_list)


@app.route('/submit', methods=["POST"])
def submit():
    global todo_list

    task = request.form['task']
    print(task)
    email = request.form['email']
    priority = request.form['priority']
    if (priority == "Low" or priority == "Medium" or priority == "High") and re.search(r"\w+[@]\w+[.]\w+", email):
        todo_list.append((task, email, priority))
        return redirect(url_for('display_list'))
    else:
        return redirect(url_for('display_list'))


@app.route('/clear', methods=["POST"])
def clear():
    global todo_list

    todo_list = []
    return redirect(url_for('display_list'))


# Extra Credit I

@app.route('/save', methods=["POST"])
def save():
    with open('todo_list.pickle', 'wb') as f:
        pickle.dump(todo_list, f)

    return redirect(url_for('display_list'))


@app.route('/load', methods=["POST"])
def load():
    global todo_list

    with open('todo_list.pickle', 'rb') as f:
        todo_list = pickle.load(f)

    return render_template('todo.html', todo_list=todo_list)


if __name__ == '__main__':
    app.run(debug=True)
