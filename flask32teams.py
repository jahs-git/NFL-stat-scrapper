from flask import Flask, render_template

app = Flask(__name__)

# Define the NFL standings data
nfl_standings = {
    "AFC East": [
        {"Tm": "BUF", "W": 9, "L": 2, "W-L%": ".818"},
        {"Tm": "MIA", "W": 5, "L": 7, "W-L%": ".417"},
        {"Tm": "NYJ", "W": 3, "L": 8, "W-L%": ".273"},
        {"Tm": "NWE", "W": 3, "L": 9, "W-L%": ".250"}
    ],
    "AFC North": [
        {"Tm": "PIT", "W": 8, "L": 3, "W-L%": ".727"},
        {"Tm": "BAL", "W": 8, "L": 4, "W-L%": ".667"},
        {"Tm": "CIN", "W": 4, "L": 7, "W-L%": ".364"},
        {"Tm": "CLE", "W": 3, "L": 8, "W-L%": ".273"}
    ],
    "AFC South": [
        {"Tm": "HOU", "W": 7, "L": 5, "W-L%": ".583"},
        {"Tm": "IND", "W": 5, "L": 7, "W-L%": ".417"},
        {"Tm": "TEN", "W": 4, "L": 7, "W-L%": ".364"},
        {"Tm": "JAX", "W": 2, "L": 9, "W-L%": ".182"}
    ],
    "AFC West": [
        {"Tm": "KAN", "W": 9, "L": 2, "W-L%": ".818"},
        {"Tm": "LAC", "W": 7, "L": 4, "W-L%": ".636"},
        {"Tm": "DEN", "W": 4, "L": 7, "W-L%": ".364"},
        {"Tm": "LVR", "W": 2, "L": 10, "W-L%": ".167"}
    ],
    "NFC East": [
        {"Tm": "PHI", "W": 9, "L": 2, "W-L%": ".818"},
        {"Tm": "WAS", "W": 7, "L": 5, "W-L%": ".583"},
        {"Tm": "DAL", "W": 5, "L": 7, "W-L%": ".417"},
        {"Tm": "NYG", "W": 2, "L": 10, "W-L%": ".167"}
    ],
    "NFC North": [
        {"Tm": "DET", "W": 11, "L": 1, "W-L%": ".917"},
        {"Tm": "MIN", "W": 9, "L": 2, "W-L%": ".818"},
        {"Tm": "GNB", "W": 6, "L": 2, "W-L%": ".750"},
        {"Tm": "CHI", "W": 4, "L": 8, "W-L%": ".333"}
    ],
    "NFC South": [
        {"Tm": "ATL", "W": 6, "L": 5, "W-L%": ".545"},
        {"Tm": "TAM", "W": 5, "L": 6, "W-L%": ".454"},
        {"Tm": "NOR", "W": 4, "L": 7, "W-L%": ".364"},
        {"Tm": "CAR", "W": 3, "L": 8, "W-L%": ".273"}
    ],
    "NFC West": [
        {"Tm": "SEA", "W": 6, "L": 5, "W-L%": ".545"},
        {"Tm": "ARI", "W": 5, "L": 6, "W-L%": ".454"},
        {"Tm": "LAR", "W": 4, "L": 7, "W-L%": ".364"},
        {"Tm": "SFO", "W": 5, "L": 6, "W-L%": ".455"}
    ]
}

@app.route('/')
def index():
    # Pass the standings data to the template
    return render_template('index.html', nfl_standings=nfl_standings)

if __name__ == "__main__":
    app.run(debug=True)
