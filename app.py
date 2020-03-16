from flask import Flask, render_template, request, url_for, redirect
import json
app = Flask(__name__)

with open('course_list.json') as f:
    data = json.load(f)

@app.route('/', methods=['GET', 'POST'])
def select():
    if request.method == 'POST':
        semester = request.form['semester']
        return redirect(url_for('input_marks', semester=semester))
    
    return render_template('base.html')


@app.route('/<semester>', methods=['GET', 'POST'])
def input_marks(semester):
    if semester in data:
        Key = data[semester]

    if request.method == 'POST':
        marks = request.form
        return render_template('result.html', marks=marks)
    return render_template('input.html', Key=Key)

if __name__ == "__main__":
	app.run(debug=True)