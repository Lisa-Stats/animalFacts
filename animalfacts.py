from flask import Flask, render_template, request
import req as reqs

app = Flask(__name__)

@app.route("/")
def main():
    if request.args.get("dog", False) == "Get Dog Fact":
        return render_template("index.html",
                               dog_data=reqs.dog_request())
    elif request.args.get("cat", False) == "Get Cat Fact":
        return render_template("index.html",
                               cat_data=reqs.cat_request())
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
