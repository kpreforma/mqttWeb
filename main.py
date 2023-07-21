from flask import Flask, render_template, request, url_for, redirect, session
import pymongo

# import bcrypt

app = Flask(__name__)
app.secret_key = os.environ["APP_ENCRYPTION"]
client = pymongo.MongoClient(os.environ["MONGODB_CONNSTRING"])
db = client.get_database("credentials")
records = db.gptflask
messages = []


@app.route("/", methods=["POST", "GET"])
# def index():
#     message = ""
#     if "email" in session:
#         return redirect(url_for("logged_in"))
#     if request.method == "POST":
#         user = request.form.get("fullname")
#         email = request.form.get("email")
#         password1 = request.form.get("password1")
#         password2 = request.form.get("password2")

#         user_found = records.find_one({"name": user})
#         email_found = records.find_one({"email": email})
#         if user_found:
#             message = 'There already is a user by that name'
#             return render_template('index.html', message=message)
#         if email_found:
#             message = 'This email already exists in database'
#             return render_template('index.html', message=message)
#         if password1 != password2:
#             message = 'Passwords should match!'
#             return render_template('index.html', message=message)
#         else:
#             hashed = bcrypt.hashpw(password2.encode('utf-8'), bcrypt.gensalt())
#             user_input = {'name': user, 'email': email, 'password': hashed}
#             records.insert_one(user_input)

#             user_data = records.find_one({"email": email})
#             new_email = user_data['email']

#             return render_template('logged_in.html', email=new_email)
#     return render_template('index.html')


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template("form.html")
    if request.method == "POST":
        form_data = request.form
        response = openai_response(
            form_data["message"] + ". Respond with less than 30 words.", messages
        )
        response_message_content = response["choices"][0]["message"]["content"]
        print(response_message_content)
        return render_template("form.html", output=response_message_content)


# @app.route('/', )
# def data():
#     if request.method == 'GET':
#         return f"The URL /data is accessed directly. Try going to index page (/) to submit form"
#     if request.method == 'POST':
#         form_data = request.form
#         response = openai_response(form_data["message"] + ". Respond with less than 30 words.", messages)
#         response_message_content = response["choices"][0]["message"]["content"]
#         return render_template('form.html', output=response_message_content)

if __name__ == "__main__":
    messages.append(
        {"role": "system", "content": "You are an assistant that speaks normally."}
    )
    print(messages)
    app.run(host="127.0.0.1", port=8000, debug=True)
