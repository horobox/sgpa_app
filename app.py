from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def select():
    if request.method == 'POST':
        semester = request.form['semester']
        return render_template('sgpa.html', value=semester)
    return render_template('base.html')

if __name__ == "__main__":
	app.run(debug=True)