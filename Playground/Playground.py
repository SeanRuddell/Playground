from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def initial_render():
    return "go to http://localhost:5000/play"

@app.route("/play")
def block_render():
    return render_template('play1.html')

@app.route("/play/<numboxes>")
def block_repeat(numboxes):
    repeat = int(numboxes)
    return render_template('play2.html', repeat=repeat)

@app.route("/play/<numboxes>/<color_change>")
def box_color(numboxes,color_change):
    repeat = (int(numboxes))
    colorChange = color_change
    return render_template('play3.html', repeat = repeat, colorChange = colorChange )


if __name__ == "__main__":
    app.run(debug = True)