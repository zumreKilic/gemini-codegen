from flask import Flask, request, render_template
from generate import get_code_and_title

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    title = None
    code = None
    prompt = ""

    if request.method == "POST":
        prompt = request.form["prompt"]
        title, code = get_code_and_title(prompt)

    return render_template("index.html", prompt=prompt, title=title, code=code)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
