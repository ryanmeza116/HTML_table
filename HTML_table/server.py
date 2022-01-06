from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    names = [
        {'first_name' : 'Ryan', 'last_name' : 'Meza'},
        {'first_name' : 'Abby', 'last_name' : 'Meza'},
        {'first_name' : 'Nellie', 'last_name' : 'Meza'},
        {'first_name' : 'Lincoln', 'last_name' : 'Meza'},
        {'first_name' : 'Amelia', 'last_name' : 'Meza'}
    ]
    return render_template('index.html', names = names)



if __name__ == "__main__":
    app.run(debug=True)