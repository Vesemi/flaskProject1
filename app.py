from flask import Flask, render_template
import database


app = Flask(__name__)
connection = database.connect()
database.create_tables(connection)

@app.route('/')
def index():
   # text = open('dane/xd.txt').read()
    return render_template("content.html")


@app.route('/xd')
def xd():
    return render_template("xd.html")


if __name__ == "__main__":

    app.run(debug=True)
