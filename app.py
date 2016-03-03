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
        if r['Approved'].lower() == "false":
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
        r['url'] = '/show/{}'.format(r['ID'])
        records.append(r)

    return render_template("list.html",
                           cols=cols,
                           records=records,
                           fieldnames=settings.fieldnames)

@app.route("/add", methods=['POST','GET'])
def add():

    if request.method == 'GET':
        return render_template("add.html",
                                fieldnames=settings.fieldnames,
                                categories=settings.categories)

    if request.method == 'POST':
        print(request)
        sheet = utils.get_sheet('google_keys.json')
        print("got sheet")
        row = [request.form.get('name',''),
                request.form.get('description',''),
                request.form.get('category',''),
                request.form.get('address1',''),
                request.form.get('address2',''),
                request.form.get('city',''),
                request.form.get('state',''),
                request.form.get('zip',''),
                request.form.get('phone',''),
                request.form.get('website',''),
                request.form.get('email',''),
                ]
        if settings.require_approval:
            row.append(False)
        else:
            row.append(True)


        try:
            sheet.insert_row(row, index=2)
        except:
            print("false")
            return render_template("item_added.html",
                           success=False,
                           require_approval=settings.require_approval)

        print("true")
        return render_template("item_added.html",
                success=True,
                require_approval=settings.require_approval)


@app.route("/show/<record_id>", methods=['GET'])
def show(record_id):
    sheet = utils.get_sheet('google_keys.json')
    sheet_records = sheet.get_all_records()
    record = [r for r in sheet_records if r['ID']==record_id]
    if len(record) != 1:
        render_template("show.html",
                        found=False)
    return render_template("show.html",
                            found=True,
                            record=record[0],
                            fieldnames=settings.fieldnames)


if __name__ == "__main__":
    app.run()