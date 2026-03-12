from flask import Flask, render_template, request
import json
from datetime import date

app = Flask(__name__)

def get_advice(sleep, study, sport, mood, phone):
    
    advice = []

    if sleep < 7:
        analysis.append("Your sleep is below optimal level.")

    if study >= 4:
        analysis.append("Great focus on studying today.")

    if sport == 0:
        analysis.append("Physical activity can increase productivity.")

    if phone > 5:
        analysis.append("High phone usage detected. Consider digital detox.")

    if mood < 5:
        analysis.append("Low mood can affect productivity.")

    if sleep >= 7 and study >= 4 and phone < 4:
        analysis.append("Excellent daily balance.")


    return advice
 
def ai_analysis(sleep, study, sport, mood, phone):

    analysis = []

    if sleep < 7:
        analysis.append("Your sleep is below optimal level")

    if study >= 4:
        analysis.append("Great studying today")

    if sport == 0:
        analysis.append("Try adding physical activity")

    if phone > 5:
        analysis.append("Too much phone usage")

    if mood < 5:
        analysis.append("Your mood is low today")

    return analysis
@app.route("/", methods=["GET", "POST"])

def index():

    score = None
    advice = None
    level = None
    analysis = None

    try:
        with open("history.json", "r") as file:
            history = json.load(file)

            if not isinstance(history, dict):
                history = {}

    except:
        history = {}

    if request.method == "POST":

        sleep = float(request.form["sleep"])
        study = float(request.form["study"])
        sport = float(request.form["sport"])
        mood = int(request.form["mood"])
        phone = float(request.form["phone"])

        score = sleep + study + sport + mood - phone

        today = str(date.today())
        history[today] = score

        with open("history.json", "w") as file:
            json.dump(history, file)

        advice = get_advice(sleep, study, sport, mood, phone)
        
        analysis = ai_analysis(sleep, study, sport, mood, phone)
        if score >= 80:
            level = "Excellent productivity"
        elif score >= 50:
            level = "Good but can improve"
        else:
            level = "Low productivity"
       

    return render_template(
        "index.html",
        score=score,
        advice=advice,
        level=level,
        history=history,
        analysis=analysis
    )


if __name__ == "__main__":
    app.run(debug=True)