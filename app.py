from flask import Flask, render_template, request
import json
app = Flask(__name__)

with open('course_list.json') as f:
    data = json.load(f)

@app.route('/', methods=['GET', 'POST'])
def select():
    if request.method == 'POST':
        semester = request.form['semester']
        if semester in data:
            Key = data[semester]
            return render_template('input.html', Key=Key)
    return render_template('base.html')

if __name__ == "__main__":
	app.run(debug=True)