from flask import Flask,render_template,request
import chess
 
app = Flask(__name__)

board = chess.Board()

def updateBoard():
  def make_matrix(board): #type(board) == chess.Board()
    pgn = board.epd()
    foo = []  #Final board
    pieces = pgn.split(" ", 1)[0]
    rows = pieces.split("/")
    for row in rows:
      foo2 = []  #This is the row I make
      for thing in row:
        if thing.isdigit():
          for i in range(0, int(thing)):
            foo2.append('.')
        else:
          foo2.append(thing)
      foo.append(foo2)
    return foo

  

@app.route('/')
def home_page():
  embed = updateBoard()
  return render_template('index.html', embed1=embed[0], embed2=embed[1], embed3=embed[2], embed4=embed[3], embed5=embed[4],embed6=embed[5],embed7=embed[6],embed8=embed[7])
 
@app.route('/form')
def form():
  return render_template('form.html')
 
@app.route('/data/', methods = ['POST', 'GET'])
def data():
  if request.method == 'GET':
    return f"The URL /data is accessed directly. Try going to '/form' to submit form"
  if request.method == 'POST':
    form_data = request.form
    return render_template('data.html',form_data = form_data)


if __name__ == '__main__':
  app.run()
