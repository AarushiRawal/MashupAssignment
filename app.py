from flask import Flask, render_template, request
import zipfile
import yagmail
from mashup_utils import download_videos, convert_to_audio, trim_audio, merge_audio

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods=["POST"])
def create():
    singer = request.form["singer"]
    num_videos = int(request.form["videos"])
    duration = int(request.form["duration"])
    email = request.form["email"]

    output_file = "mashup.mp3"

    try:
        download_videos(singer, num_videos)
        convert_to_audio()
        trim_audio(duration)
        merge_audio(output_file)

        zip_name = "mashup.zip"
        with zipfile.ZipFile(zip_name, 'w') as zipf:
            zipf.write(output_file)

        yag = yagmail.SMTP("aarushirawal@gmail.com", "tpbm lzdi inlx tefy")
        yag.send(
            to=email,
            subject="Your Mashup File",
            contents="Here is your mashup.",
            attachments=zip_name
        )

        return "Mashup sent successfully!"

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
