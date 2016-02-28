from flask import Flask, render_template
import utils

app = Flask(__name__)

app.debug = True

@app.route("/")
def index():
    return render_template("index.html")    

@app.route("/list")
def list():
    cols = ['Name',
            'Description',
            'Category',
            'City',
            'State']
    sheet = utils.get_sheet('google_keys.json')
    records = sheet.get_all_records()

    return render_template("list.html",
                           cols=cols,
                           records=records)

if __name__ == "__main__":
    app.run()