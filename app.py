from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from os import environ
from forms import PostsForm

app = Flask(__name__)


app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + \
                                        environ.get('MYSQL_USER') + \
                                        ':' + \
                                        environ.get('MYSQL_PASSWORD') + \
                                        '@' + \
                                        environ.get('MYSQL_HOST') + \
                                        ':' + \
                                        environ.get('MYSQL_PORT') + \
                                        '/' + \
                                        environ.get('MYSQL_DB_NAME')

db = SQLAlchemy(app)


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(30), nullable=False)
    l_name = db.Column(db.String(30), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(300), nullable=False, unique=True)

    def __repr__(self):
        return ''.join(
            [
                'Title: ' + self.title + '\n'
                'Name: ' + self.f_name + ' ' + self.l_name + '\n'
                'Content: ' + self.content
            ]
        )


@app.route('/')
@app.route('/home')
def home():
    post_data = Posts.query.all()
    return render_template('homepage.html', title='Homepage', posts=post_data)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/add')
def add():
    form = PostsForm()
    return render_template('post.html', title='Add a post', form=form)


@app.route('/create')
def create():
    db.create_all()
    post = Posts(f_name='Michael', l_name='McGarrigle', title='Mr', content="Anything")
    post2 = Posts(f_name='John', l_name='Smith', title='Lord', content="Anything else")
    db.session.add(post)
    db.session.add(post2)
    db.session.commit()
    return "Added the table and populated it with some records"


@app.route('/delete')
def delete():
    db.drop_all()  # drops all the schemas
    #db.session.query(Posts).delete()  # deletes the contents of the table
    db.session.commit()
    return "everything is gone"


if __name__ == '__main__':
    app.run()