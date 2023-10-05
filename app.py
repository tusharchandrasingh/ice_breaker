from flask import Flask, render_template, request, jsonify

from ice_breaker import ice_break

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    person_info, profile_pic_url = ice_break(name=name)

    # print(f"log: details received from ice_break are {person_info} \n {profile_pic_url}")

    json_response = jsonify(
        {
            "summary": person_info.summary,
            "interests": person_info.topics_of_interest,
            "facts": person_info.facts,
            "ice_breakers": person_info.ice_breakers,
            "picture_url": profile_pic_url,
        }
    )

    print(f"log: processed json response is {json_response.json}")

    return json_response


if __name__ == "__main__":
    # app.run(host="0.0.0.0", debug=True)
    app.run(host="0.0.0.0")

