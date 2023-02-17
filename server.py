from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

# navie route:
# @app.route("/works.html")
# def works():
#     return render_template('works.html')

# @app.route("/about.html")
# def about():
#     return render_template('about.html')

# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')

# dynamicall accept different URL param


@app.route('/<string:page_name>')
def html_name(page_name):
    return render_template(page_name)

# collect & store data in txt
def write_to_file(data):
  with open('database.txt', mode="a") as db:
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    file = db.write(f'\n{email},{subject},{message}')


# collect & store data in csv | start in newline in csv
def write_to_csv(data):
  with open('database.csv',newline='', mode="a" ) as db2:
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    csv_writer = csv.writer(db2, delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([email,subject,message])


# submitting the form

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
      try:
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
      except: 
        return 'did not save to database'
    else:
        return 'something went wrong'


