from flask import Flask, render_template, session, request

app = Flask(__name__)
app.secret_key = "blahhhhhhhh"

@app.route('/')
def show_homepage():
    return render_template('homepage.html')

###############################
#                             #
# 1) Finish the routes below. #
#                             #
###############################


@app.route('/form')
def show_form():
    
    return render_template("form.html")

@app.route('/results')
def show_results():
    """Get form result and create display method."""
    cheery = request.args.get("cheery")
    honest = request.args.get("honest")
    dreary = request.args.get("dreary")

    if cheery and honest and dreary: 
        msg = "You've got the whole world in your hand."
    elif cheery and honest and not dreary:
        msg = "Up and to the right."
    elif honest and not cheery and not dreary: 
        msg = "Take a good look in the mirror. That is you!"
    elif honest and dreary and not cheery:
        msg = "Times are tough now. Just getting tougher."
    elif cheery and not honest and dreary: 
        msg = "Keep on smiling."    
    elif not honest and not cheery:
        msg = "I don't want no scrubs."
    else: 
        msg = "You will get through Hackbright"

    return render_template("results.html", msg=msg)

@app.route('/save-name', methods=["POST"])
def save_name():
    name = request.form.get('name')
    session['name'] = name
    

    return render_template("form.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
