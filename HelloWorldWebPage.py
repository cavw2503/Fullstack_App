from flask import Flask, render_template
app = Flask(__name__) #create a Flask application object. __name__ tells Flask where to look for templates and static files.

@app.route('/')
def helloWorld():
    # HTML template with a simple message
    return render_template('template.html')

if __name__ == '__main__':
    app.run(debug=True)