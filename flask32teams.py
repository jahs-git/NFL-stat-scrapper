from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    # Pass the nfl_standings dictionary to the template
    return render_template('Team.Grid.html')

if __name__ == "__main__":
    app.run(debug=True)
