from flask import Flask, render_template, request
import utils
import settings

app = Flask(__name__)

app.debug = True

@app.route("/")
def index():
    return render_template("index.html")    

@app.route("/list", methods=['POST','GET'])
def list():
    cols = ['Name',
            'Description',
            'Category',
            'City',
            'State']

    sheet = utils.get_sheet('google_keys.json')
    sheet_records = sheet.get_all_records()
    records = []
    if request.method == 'POST':
        search_term = request.form['search_term']
    else:
        search_term = None
    for r in sheet_records:
        print(r['Name'])
        if r['Approved'] == False:
            #this record hasn't been approved by the moderator
            continue
        if r['Name'].strip() == '':
            #skip anyting without a name
            continue
        if search_term:
            all_fields = " ".join([r[k] for k in cols])
            if search_term.lower() not in all_fields.lower():
                #skip anything where the search term doesn't appear
                continue
        records.append(r)

    return render_template("list.html",
                           cols=cols,
                           records=records,
                           fieldnames=settings.fieldnames)

@app.route("/add", methods=['POST','GET'])
def add():

    if request.method == 'GET':
        return render_template("add.html",
                                fieldnames=settings.fieldnames)

    if request.method == 'POST':
        sheet = utils.get_sheet('google_keys.json')
        row = [request.form['name'],
                request.form['description'],
                request.form['category'],
                request.form['address1'],
                request.form['address2'],
                request.form['city'],
                request.form['state'],
                request.form['zip'],
                request.form['phone'],
                request.form['website'],
                request.form['email'],
                ]

        if settings.require_approval:
            row.append(False)
        else:
            row.append(True)


        try:
            sheet.insert_row(row, index=2)
        except:
            return render_template("item_added.html",
                           success=False,
                           require_approval=settings.require_approval)


        return render_template("item_added.html",
                success=True,
                require_approval=settings.require_approval)


if __name__ == "__main__":
    app.run()