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
        marks_list = request.form
        
        marks = []
        
        for value in marks_list.values():
            marks.append(int(value))

        return results(marks, list(Key.values()))
    return render_template('input.html', Key=Key)

def results(marks, grade_points):
    sgpa = 0
    marks_credit = []

    for i in range(0, len(marks)):
        marks_credit.append(marks[i] // 10 + 1)

    for i in range(0, len(marks)):
        sgpa += marks_credit[i] * grade_points[i]
    sgpa = round(sgpa / sum(grade_points), 3)
    return render_template('result.html', sgpa=sgpa)

if __name__ == "__main__":
	app.run(debug=True)