from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def select():

    sem_list = {
        "semester3":{
            "engineering math3": 4,
            "ei": 3,
            "ae": 4,
            "de": 4,
            "ee": 4,
            "ae lab": 2,
            "de lab": 2,
        },
        "semester4":{
            "math4": 4,
            "ss": 4,
            "cs": 4,
            "pcs": 4,
            "lic": 4,
            "mp": 3,
            "lic lab": 2,
            "mp lab": 2,
        },
        "semester5": {
            "mgmt": 4,
            "dsp": 4,
            "vhdl": 4,
            "itc": 4,
            "pe": 3,
            "oe": 3,
            "dsp lab": 2,
            "hdl lab": 2,
        }
    }

    if request.method == 'POST':
        semester = request.form['semester']
        if semester in sem_list:
            Key = sem_list[semester]
            return render_template('input.html', Key=Key)
    return render_template('base.html')

if __name__ == "__main__":
	app.run(debug=True)