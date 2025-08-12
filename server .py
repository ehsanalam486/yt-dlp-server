from flask import Flask, request, send_file
import yt_dlp
import os

app = Flask(__name__)

@app.route("/download", methods=["GET"])
def download():
    url = request.args.get("url")
    if not url:
        return {"error": "No URL provided"}, 400
    
    ydl_opts = {
        "format": "best",
        "outtmpl": "%(title)s.%(ext)s"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)

    return send_file(filename, as_attachment=True)

@app.route("/")
def home():
    return "yt-dlp Server is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)