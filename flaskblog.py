from flask import Flask, render_template  # From flask package import Flask class
app = Flask(__name__)  ## initialize an instance of the Flask class,
## __name__ == name of the module,
## __name__ == __main__ if run the script directly


@app.route("/")  # .route() decorators to add additional complicated backend functionalities to the hello function
@app.route("/home")  # add another decorator so that you go to same page when accessing both route
def home():     # return the thing you want to show in the website's '/' route (root page)
    return render_template('home.html') # template is in the ./templates folder, folder name cannot be changed


@app.route("/about")
def about():
    return render_template('about.html')





## Method 1 to run the flask app - run with terminal flask command
# export FLASK_APP=flaskblog.py     -- to let terminal know which file is the main file of the app
# export FLASK_DEBUG=1              -- to turn on debug mode so that don't have to restart the server everytime changing the code
# flask run                         -- terminal command to start the flask app server


## Method 2 to run the flask app - run directly with python
if __name__ == '__main__':  # if run this script directly
    app.run(debug=True)     # then run the app with debug mode
