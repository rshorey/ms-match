from flask import Flask
import utils

app = Flask(__name__)

app.debug = True

@app.route("/")
def hello():
    cols = ['Name',
            'Description',
            'Category',
            'City',
            'State']
    sheet = utils.get_sheet('google_keys.json')
    records = sheet.get_all_records()
    out = """<html><head></head><body><table><th>"""
    for h in cols:
        out += "<td>{}</td>".format(h)
    out += "</th>"
    for row in records:
        out += "<tr>"
        for c in cols:
            out += "<td>{}</td>".format(row[c])
        out += "</tr>"
    out += "</table></body></html>"
    return out

if __name__ == "__main__":
    app.run()