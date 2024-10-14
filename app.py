from flask import Flask, render_template, request, jsonify
from insights_linkedin import insights_linkedin

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    summary, profile_pic_url = insights_linkedin(name=name)
    
    return jsonify(
        {
            "summary_and_facts": summary.to_dict(),
            "picture_url": profile_pic_url
        }
    )

if __name__ == "__main__":
    app.run()