from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    # Pass the nfl_standings dictionary to the template
    return render_template('index.html', nfl_standings=nfl_standings)

if __name__ == "__main__":
    app.run(debug=True)
