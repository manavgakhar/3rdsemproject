from flask import Flask,render_template,url_for,request,redirect,session,flash
from werkzeug.utils import secure_filename
import speech_recognition as sr
import os



isl_gif=['address',
 'ahemdabad',
 'all',
 'any questions',
 'are you angry',
 'are you hungry',
 'assam',
 'august',
 'banana',
 'banaras',
 'banglore',
 'be careful',
 'bridge',
 'cat',
 'christmas',
 'church',
 'cilinic',
 'dasara',
 'december',
 'did you finish homework',
 'do you have money',
 'do you want something to drink',
 'do you watch TV',
 'dont worry',
 'flower is beautiful',
 'good afternoon',
 'good morning',
 'good question',
 'grapes',
 'hello',
 'hindu',
 'hyderabad',
 'i am a clerk',
 'i am fine',
 'i am sorry',
 'i am thinking',
 'i am tired',
 'i go to a theatre',
 'i had to say something but I forgot',
 'i like pink colour',
 'i love to shop',
 'job',
 'july',
 'june',
 'karnataka',
 'kerala',
 'krishna',
 'lets go for lunch',
 'mango',
 'may',
 'mile',
 'mumbai',
 'nagpur',
 'nice to meet you',
 'open the door',
 'pakistan',
 'please call me later',
 'police station',
 'post office',
 'pune',
 'punjab',
 'saturday',
 'shall I help you',
 'shall we go together tommorow',
 'shop',
 'sign language interpreter',
 'sit down',
 'stand up',
 'take care',
 'temple',
 'there was traffic jam',
 'thursday',
 'toilet',
 'tomato',
 'tuesday',
 'usa',
 'village',
 'wednesday',
 'what is the problem',
 "what is today's date",
 'what is your father do',
 'what is your name',
 'whats up',
 'where is the bathroom',
 'where is the police station',
 'you are wrong']



app=Flask(__name__)

app.secret_key = 'the random string'

@app.route("/")
def home():
    return render_template("signlanguage.html")

@app.route("/gifs")
def gifs():
    return render_template("gifs.html", list=isl_gif)

@app.route("/future")
def future():
    return render_template("future.html")




UPLOAD_FOLDER = "./"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# You have 50 free calls per day, after that you have to register somewhere
# around here probably https://cloud.google.com/speech-to-text/
GOOGLE_SPEECH_API_KEY = None




@app.route("/", methods=["GET", "POST"])
def index():
    extra_line = ''
    if request.method == "POST":

        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["file"]


        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file:

            recognizer = sr.Recognizer()
            audio_file = sr.AudioFile(file)
            with audio_file as source:
                audio_data = recognizer.record(source)
            text = recognizer.recognize_google(
                audio_data, key=GOOGLE_SPEECH_API_KEY, language="en-EN"
            )


            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)
            extra_line += f"<br>File saved to {filepath}"

    return render_template("signlanguage.html", extra_line =text)



if __name__ == "__main__":
    app.run(debug=True)









