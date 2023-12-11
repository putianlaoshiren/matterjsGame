from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/')
def index():
    return render_template('choose_game.html')

@app.route('/game1')
def game1():
    return render_template('game1_xuanguang.html')

@app.route('/shut1')
def shut1():
    return render_template('shut1.html')

@app.route('/shut2')
def shut2():
    return render_template('shut2.html')

@app.route('/shut3')
def shut3():
    return render_template('shut3.html')

@app.route('/game2')
def game2():
    return render_template('game2.html')
    
@app.route('/game3')
def game3():
    return render_template('game3.html')

@app.route('/game4')
def game4():
    return render_template('game4.html')
if __name__ == '__main__':
    app.run(debug=True)