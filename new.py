#IMPORTING
from flask import Flask , render_template , request

#INTERACTION
web = Flask(__name__)

#MAPPING
@web.route('/')
@web.route('/register')

#INPUTS
def homepage():
    return render_template('register.html')

#MAPPING
@web.route("/confirmation" , methods =['POST', 'GET'])

#INPUTS
def register():
    if request.method == "POST":
        n = request.form.get('name')
        c = request.form.get('city')
        p = request.form.get('phone number')
        e = request.form.get('email address')
        return render_template('confirm.html', name = n, city = c, phonenumber = p, emailaddress = e)

#MAIN
if __name__ == "__main__":
    web.run(debug=True)

