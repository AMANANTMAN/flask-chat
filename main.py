from flask import Flask,render_template,request
import chess
 
app = Flask(__name__)

board = chess.Board()

def updateBoard():
  print_board = ''
  for i in range(0, 64, 8):
    print_board += ' '.join(board.split(' ')[i:i+8]) + '\n'
  return print_board

@app.route('/')
def home_page():
  embed = updateBoard()
  return render_template('index.html', embed=embed)
 
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
