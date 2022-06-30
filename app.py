from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from test_model import Person

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exercise_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'Response Data'


@app.route('/another')
def another():
    return 'Another Response'


@app.route('/test_request')
def test_request():
    return f'test_request:{request.args.get("dummy")}'


@app.route('/exercise_request/<exercise>')
def exercise_request(exercise):
    return f'exercise_request:{exercise}'


@app.route('/show_html')
def show_html():
    return render_template('./test_html.html')


@app.route('/try_rest', methods=['POST'])
def try_rest():
    # リクエストデータをJSONとして受け取る
    request_json = request.get_json()
    print(request_json)
    print(type(request_json))
    name = request_json['name']
    print(name)
    response_json = {"response_json": request_json}
    return jsonify(response_json)


@app.route('/person_search')
def person_search():
    return render_template('./person_search.html')


@app.route('/person_result')
def person_result():
    search_size = request.args.get("search_size")
    persons = db.session.query(Person).filter(Person.size > search_size)
    return render_template('./person_result.html', persons=persons, search_size=search_size)

# ここからWebアプリ２の演習の回答例
from exercise_model import Human
from sqlalchemy import or_

@app.route('/human_search')
def human_search():
    return render_template('./human_search.html')

@app.route('/human_result')
def human_result():
    search_height = request.args.get('search_height')
    search_weight = request.args.get('search_weight')
    humans = db.session.query(Human).filter(or_(Human.height>=search_height, Human.weight>=search_weight))
    return render_template('./human_result.html', humans=humans, search_height=search_height, search_weight=search_weight)

# ここからWebアプリ3の演習の回答例
@app.route('/human_search2')
def human_search2():
    return render_template('./human_search2.html')

@app.route('/human_result2')
def human_result2():
    search_height = request.args.get('search_height')
    search_weight = request.args.get('search_weight')
    humans = db.session.query(Human).filter(or_(Human.height>=search_height, Human.weight>=search_weight))
    return render_template('./human_result2.html', humans=humans, search_height=search_height, search_weight=search_weight)

