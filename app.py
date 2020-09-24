from flask import Flask, render_template, redirect, url_for
from forms import VMRequestForm
from wtforms import StringField, TextField
from flask_wtf.csrf import CSRFProtect
import csv


app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)
app.config['SECRET_KEY'] = ':JbnxUs^iTA},;Jtlv3-'


@app.route('/', methods=['GET', 'POST'])
def index():
    req_form = VMRequestForm()
    if req_form.validate_on_submit():
        # data = {field.name: field.data for field in req_form._fields.values() if type(field) in (TextField)}
        write_to_csv(req_form)
        return redirect(url_for('success'))
    return render_template('vm/request.html', form=req_form)


@app.route('/success', methods=['GET'])
def success():
    return render_template('vm/success.html')


def write_to_csv(form_data):
    with open(f'data/{form_data.username.data}.csv', 'w', newline='') as csvfile:
        wr = csv.DictWriter(csvfile, fieldnames=['username'])
        wr.writeheader()
        wr.writerow({form_data.username.name: form_data.username.data.strip()})
        # for k, v in form_data:
        #     print(f'Writing: {k} {v}')
        #     wr.writerow({k: v})


if __name__ == '__main__':
    app.run(debug=True)