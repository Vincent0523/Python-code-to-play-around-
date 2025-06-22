from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)

#use this to open the browser http://127.0.0.1:5000/

#what to use to active it in the terminal  
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process.\venv\Scripts\activate
