from flask import Flask, render_template

app = Flask(__name__)

# Sample data structure for NFL standings (replace this with actual scraped data)
nfl_standings = nfl_standings = {
    "AFC East": [
        {"Tm": "BUF", "W": 7, "L": 2, "W-L%": ".778"},
        {"Tm": "NYJ", "W": 3, "L": 6, "W-L%": ".333"},
        {"Tm": "MIA", "W": 2, "L": 6, "W-L%": ".250"},
        {"Tm": "NWE", "W": 2, "L": 7, "W-L%": ".222"}
    ],
    "AFC North": [
        {"Tm": "PIT", "W": 6, "L": 2, "W-L%": ".750"},
        {"Tm": "BAL", "W": 6, "L": 3, "W-L%": ".667"},
        {"Tm": "CIN", "W": 5, "L": 4, "W-L%": ".444"},
        {"Tm": "CLE", "W": 2, "L": 7, "W-L%": ".222"}
    ],
    "AFC South": [
        {"Tm": "HOU", "W": 6, "L": 3, "W-L%": ".667"},
        {"Tm": "IND", "W": 5, "L": 4, "W-L%": ".556"},
        {"Tm": "TEN", "W": 2, "L": 7, "W-L%": ".222"},
        {"Tm": "JAX", "W": 2, "L": 7, "W-L%": ".222"}
    ],
    "AFC West": [
        {"Tm": "KAN", "W": 8, "L": 1, "W-L%": ".889"},
        {"Tm": "LAC", "W": 5, "L": 4, "W-L%": ".556"},
        {"Tm": "DEN", "W": 5, "L": 4, "W-L%": ".556"},
        {"Tm": "LVR", "W": 2, "L": 7, "W-L%": ".222"}
    ],
    "NFC East": [
        {"Tm": "WAS", "W": 7, "L": 2, "W-L%": ".778"},
        {"Tm": "PHI", "W": 6, "L": 2, "W-L%": ".750"},
        {"Tm": "DAL", "W": 3, "L": 5, "W-L%": ".375"},
        {"Tm": "NYG", "W": 2, "L": 7, "W-L%": ".222"}
    ],
    "NFC North": [
        {"Tm": "DET", "W": 7, "L": 1, "W-L%": ".875"},
        {"Tm": "MIN", "W": 6, "L": 2, "W-L%": ".750"},
        {"Tm": "GNB", "W": 6, "L": 3, "W-L%": ".667"},
        {"Tm": "CHI", "W": 4, "L": 4, "W-L%": ".500"}
    ],
    "NFC South": [
        {"Tm": "ATL", "W": 3, "L": 3, "W-L%": ".500"},
        {"Tm": "TAM", "W": 5, "L": 4, "W-L%": ".556"},
        {"Tm": "NOR", "W": 4, "L": 5, "W-L%": ".444"},
        {"Tm": "CAR", "W": 2, "L": 7, "W-L%": ".222"}
    ],
    "NFC West": [
        {"Tm": "ARI", "W": 5, "L": 4, "W-L%": ".556"},
        {"Tm": "LAR", "W": 4, "L": 4, "W-L%": ".500"},
        {"Tm": "SFO", "W": 4, "L": 4, "W-L%": ".500"},
        {"Tm": "SEA", "W": 4, "L": 5, "W-L%": ".444"}
    ]
}


@app.route('/')
def index():
    # Pass the nfl_standings dictionary to the template
    return render_template('index.html', nfl_standings=nfl_standings)

if __name__ == "__main__":
    app.run(debug=True)