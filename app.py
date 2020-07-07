from flask import Flask
from flask import render_template

app = Flask(__name__)

dummyData = [
    {
        "f_name": "Michael",
        "l_name": "McGarrigle",
        "title": "Mr",
        "content": "Anything"
    },
    {
        "f_name": "John",
        "l_name": "Smith",
        "title": "Mr",
        "content": "Anything Else"
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('homepage.html', title='Homepage', posts=dummyData)


@app.route('/about')

def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':

    app.run()