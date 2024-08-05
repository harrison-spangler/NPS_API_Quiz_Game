from flask import Flask, request

from park_collection import ParkCollection
import json

app = Flask(__name__)

with open("nps.json", 'r') as nps:
    nps_json = json.load(nps)
    park_list = ParkCollection(nps_json)
@app.route("/")
def homepage():
    return """
    <h1>Welcome to the Parks Quizzes</h1>
    <hr>
    <p><a href="/quiz">Take the Quiz</a></p>
    <p><a href="/custom_quiz">Create Custom Quiz</a></p>
    <p><a href="/Info">Information about the Parks</a></p>
    """

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "GET":
        return """
        <h2>Parks Quiz</h2>
        <hr>
        <form method="post">
            <p>What park has the most total activities?</p>
            <input type="text" name="activities_question"><br><br>
            <p>What park has the most topics?</p>
            <input type="text" name="topics_question"><br><br>
            <p>What is the total amount of parks in the JSON?</p>
            <input type="text" name="total_parks_question"><br><br>
            <input type="submit" value="Submit">
        </form>
        """
    elif request.method == "POST":
        correct = 0
        wrong = 0
        user_choice1 = request.form.get("activities_question")
        most_activities_park = park_list.most_activities()
        if user_choice1 == most_activities_park:
            correct += 1
        else:
            wrong += 1
        user_choice2 = request.form.get("topics_question")
        most_topics_park = park_list.most_topics()
        if user_choice2 == most_topics_park:
            correct += 1
        else:
            wrong += 1
        user_choice3 = request.form.get("total_parks_question")
        total_parks = park_list.len_park_list()
        if user_choice3 == str(total_parks) or user_choice3 == "5":
            correct += 1
        else:
            wrong += 1
        score_percent = float(correct / 3) * 100
        result_html = f"""
        <h2>Quiz Result</h2>
        <hr>
        <p>Correct Answers: {correct}</p>
        <p>Total Questions: 3</p>
        <p>Score: {score_percent}%</p>
        <p><br><a href="/">Return to Homepage</a></p>
        """
        return result_html

@app.route("/custom_quiz", methods=["GET", "POST"])
def custom_quiz():
    if request.method == "GET":
        sorted_parks = park_list.sort_parks()
        park_names_html = "<h2>Park Names</h2>"
        park_names_html += "<ul>"
        for park in sorted_parks:
            park_names_html += f"<li>{park.fullName}</li>"
        park_names_html += "</ul>"
        return f"""
            <h2>Park Quiz</h2>
            <hr>
            {park_names_html}
            <form method="post" action="/start_quiz">
                <p>Enter the park name: </p>
                <input type="text" name="park_name"><br><br>
                <input type="submit" value="Start Quiz">
            </form>
            """
@app.route("/start_quiz", methods=["POST"])
def start_quiz():
    if request.method == "POST":
        park_name = request.form.get("park_name")
        park = next((p for p in park_list.parks if p.fullName == park_name), None)
        if park:
            quiz_html = f"""
            <h2>Park Quiz: {park.fullName}</h2>
            <hr>
            <form method="post" action="/quiz_result">
                <input type="hidden" name="park_name" value="{park.fullName}">
                <p>How many amenities does {park.fullName} have?</p>
                <input type="text" name="amenities_question"><br><br>
                <p>How many topics does {park.fullName} cover?</p>
                <input type="text" name="topics_question"><br><br>
                <p>What are the latitude and longitude of {park.fullName}? (Format: lat:___, long:___)</p>
                <input type="text" name="lat_long_question"><br><br>
                <p>What is the park code of {park.fullName}?</p>
                <input type="text" name="park_code_question"><br><br>
                <p>Where is {park.fullName} located? (State abbreviated location, Connecticut = CT)</p>
                <input type="text" name="location_question"><br><br>
                <input type="submit" value="Submit Answers">
            </form>
            """
            return quiz_html
        else:
            return ("<h2>Park not found.</h2>"
                    "<p><br><a href='/'>Return to Homepage</a></p>")


@app.route("/quiz_result", methods=["POST"])
def quiz_result():
    park_name = request.form.get("park_name")
    amenities_answer = request.form.get("amenities_question")
    topics_answer = request.form.get("topics_question")
    lat_long_answer = request.form.get("lat_long_question")
    park_code_answer = request.form.get("park_code_question")
    location_answer = request.form.get("location_question")
    park = next((p for p in park_list.parks if p.fullName == park_name), None)
    if park:
        correct_answers = 0
        if amenities_answer == str(park.total_activities()):
            correct_answers += 1
        if topics_answer == str(park.total_topics()):
            correct_answers += 1
        if lat_long_answer == park.latitude_longitude():
            correct_answers += 1
        if park_code_answer == park.code:
            correct_answers += 1
        if location_answer.lower() == park.location.lower():
            correct_answers += 1
        total_questions = 5
        score_percent = (correct_answers / total_questions) * 100
        result_html = f"""
        <h2>Quiz Result</h2>
        <p>Park: {park.fullName}</p>
        <p>Correct Answers: {correct_answers} out of {total_questions}</p>
        <p>Score: {score_percent}%</p>
        <p><br><a href='/'>Return to Homepage</a></p>
        """
        return result_html
    else:
        return ("<h2>Park not found.</h2>"
                "<p><br><a href='/'>Return to Homepage</a></p>")
#Especially in this code, I could have used elif or else instead of continuosly using if as this could cause me issues.
@app.route("/Info", methods=["GET", "POST"])
def park_info():
    if request.method == "GET":
        park_names = [park.fullName for park in park_list.parks]
        dropdown_options = "".join([f"<option value='{name}'>{name}</option>" for name in park_names])
        return f"""
        <h2>Select a Park</h2>
        <form method="post">
            <select name="park_name">
                {dropdown_options}
            </select>
            <input type="submit" value="Get Information">
        </form>
        """
    elif request.method == "POST":
        park_name = request.form.get("park_name")
        park = park_list.search_park_by_name(park_name)
        if park:
            park_info_html = f"""
            <h2>{park.fullName}</h2>
            <hr>
            <p>Location: {park.location}</p>
            <p>Total Activities: {park.total_activities()}</p>
            <p>Total Topics: {park.total_topics()}</p>
            <p>Latitude-Longitude: {park.latitude_longitude()}</p>
            <p>Park Code: {park.code}</p>
            <p><br><a href="/">Return to Homepage</a></p>
            """
            return park_info_html
        else:
            return "<h2>Park not found.</h2>"

if __name__ == "__main__":
    app.run(debug=True)

#For my code in particular HTML, I could have created a static file holding my css which would enable me to style my code and make it look nice and formal.