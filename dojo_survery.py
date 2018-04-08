from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def take():
  return render_template("index.html")

@app.route('/results', methods=['POST'])
def result():
   
   name = request.form['name']
   location = request.form['location']
   language = request.form['language']
   comment = request.form['comment']
  
   return render_template('results.html',name = name, location = location, language = language, comment = comment)
app.run(debug=True) # run our server