from flask import Flask, render_template

app = Flask(__name__)

@app.route('/cheese_clicker.html')
def game():
    return render_template("/cheese_clicker.html")

if __name__ == "__main__":
    app.run(debug=True)

