from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for complaints (use a database in production)
complaints = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    issue = request.form['issue']
    complaints.append({'name': name, 'issue': issue})
    return redirect(url_for('show_complaints'))

@app.route('/complaints')
def show_complaints():
    return render_template('complaints.html', complaints=complaints)

if __name__ == '__main__':
    app.run(debug=True)
