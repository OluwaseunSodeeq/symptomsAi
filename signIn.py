from flask import Flask, request, render_template, redirect, url_for, flash
import re
import urllib.parse

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signIn", methods=["GET", "POST"])
def signinformvalidation():
    if request.method == "POST":
        isValid = True
        print("Form submitted!")

        full_name = request.form["full-name"]
        email = request.form["email"]
        password = request.form["password"]

        print(f"Full Name: {full_name}, Email: {email}, Password: {password}")

        # Full Name validation
        if len(full_name) < 3:
            flash('Full Name must be at least 3 characters long', "name-error")
            isValid = False
            print("Full Name error")

        # Email validation
        if not email.endswith('.com'):
            flash('Email must end with .com', 'email-error')
            isValid = False 
            print("Email error")

        # Password validation
        password_pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[\W_]).{1,}$')
        if not password_pattern.match(password):
            flash('Password must contain at least one lowercase letter, one uppercase letter, and one special character.', 'password-error')
            isValid = False
            print("Password error")
        
        if isValid:
            flash('Signup successful!', 'success')
            print("Validation passed. Redirecting to chatbox.")
            # Create a dictionary with user values
            user_values = {
                'full_name': full_name,
                'email': email
            }
            # Redirect to the chatbox with user values
            return redirect(url_for('chatbox', **user_values))
        else:
            print("Validation failed. Reloading sign-in page.")
    
    return render_template("signin.html")

@app.route("/chatbox")
def chatbox():
    # Retrieve query parameters
    full_name = request.args.get('full_name')
    email = request.args.get('email')
    print(f"Chatbox accessed with Full Name: {full_name}, Email: {email}")
    return render_template("chatbox.html", full_name=full_name, email=email)

if __name__ == '__main__':
    app.run(debug=True)

























# from flask import Flask,render_template,request
# from flask_wtf import FlaskForm
# from wtforms import StringField, validators

# app =Flask(__name__)
# app.config["SECRET_KEY"] = "secret"

# from flask import Flask, request, render_template, redirect, url_for, flash

# import re
# import urllib.parse

# app = Flask(__name__)
# app.secret_key = "your_secret_key"

# @app.route("/signIn", methods=["GET", "POST"])
# def signinformvalidation():
#     if request.method == "POST":
#         isValid = True

#         full_name = request.form["full-name"]
#         email = request.form["email"]
#         password = request.form["password"]

#         # Full Name validation
#         if len(full_name) < 3:
#             flash('Full Name must be at least 3 characters long', "name-error")
#             isValid = False

#         # Email validation
#         if not email.endswith('.com'):
#             flash('Email must end with .com', 'email-error')
#             isValid = False 

#         # Password validation
#         password_pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[\W_]).{1,}$')
#         if not password_pattern.match(password):
#             flash('Password must contain at least one lowercase letter, one uppercase letter, and one special character.', 'password-error')
#             isValid = False
        
#         if isValid:
#             flash('Signup successful!', 'success')
#             # Create a dictionary with user values
#             user_values = {
#                 'full_name': full_name,
#                 'email': email
#             }
#             # Convert the dictionary to query parameters
#             query_string = urllib.parse.urlencode(user_values)
#             # Redirect to the chatbox.html with query parameters
#             return redirect(f"/src/chatbox.html?{query_string}")
    
#     return render_template("signin.html")

# @app.route("/chatbox")
# def chatbox():
#     # Retrieve query parameters
#     full_name = request.args.get('full_name')
#     email = request.args.get('email')
#     return render_template("chatbox.html", full_name=full_name, email=email)

# if __name__ == '__main__':
#     app.run(debug=True)
