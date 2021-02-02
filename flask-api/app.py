from flask import Flask
application = Flask(__name__)

@application.route("/")
def home():
    return "Welcome to the API"

@application.route("/<original_number>/<number_to_increment>")
def increment(original_number, number_to_increment):
    new_number = float(original_number) + float(number_to_increment)
    return f"Original number was {original_number}, new number is {new_number}"

if __name__ == "__main__":
    application.run(host='0.0.0.0')
