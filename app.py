import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set the SQLite database file to the /tmp directory (Vercel's writable directory)
db_path = os.path.join('/tmp', 'responses.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the database model for storing responses
class QuestionnaireResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Q1 = db.Column(db.Integer)
    Q2 = db.Column(db.Integer)
    Q3 = db.Column(db.Integer)
    Q4 = db.Column(db.Integer)
    Q5 = db.Column(db.Integer)
    Q6 = db.Column(db.Integer)
    Q7 = db.Column(db.Integer)
    Q8 = db.Column(db.Integer)
    Q9 = db.Column(db.Integer)
    Q10 = db.Column(db.Integer)
    Q11 = db.Column(db.Integer)
    Q12 = db.Column(db.Integer)
    Q13 = db.Column(db.Integer)
    Q14 = db.Column(db.Integer)
    Q15 = db.Column(db.Integer)
    Q16 = db.Column(db.Integer)
    Q17 = db.Column(db.Integer)
    Q18 = db.Column(db.Integer)
    Q19 = db.Column(db.Integer)
    Q20 = db.Column(db.Integer)
    Q21 = db.Column(db.Integer)
    Q22 = db.Column(db.Integer)
    Q23 = db.Column(db.Integer)
    Q24 = db.Column(db.Integer)
    Q25 = db.Column(db.Integer)
    Q26 = db.Column(db.Integer)
    Q27 = db.Column(db.Integer)
    Q28 = db.Column(db.Integer)
    Q29 = db.Column(db.Integer)
    Q30 = db.Column(db.Integer)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Extract data from the form and save to the database
        response = QuestionnaireResponse(
            Q1=request.form.get('Q1'),
            Q2=request.form.get('Q2'),
            Q3=request.form.get('Q3'),
            Q4=request.form.get('Q4'),
            Q5=request.form.get('Q5'),
            Q6=request.form.get('Q6'),
            Q7=request.form.get('Q7'),
            Q8=request.form.get('Q8'),
            Q9=request.form.get('Q9'),
            Q10=request.form.get('Q10'),
            Q11=request.form.get('Q11'),
            Q12=request.form.get('Q12'),
            Q13=request.form.get('Q13'),
            Q14=request.form.get('Q14'),
            Q15=request.form.get('Q15'),
            Q16=request.form.get('Q16'),
            Q17=request.form.get('Q17'),
            Q18=request.form.get('Q18'),
            Q19=request.form.get('Q19'),
            Q20=request.form.get('Q20'),
            Q21=request.form.get('Q21'),
            Q22=request.form.get('Q22'),
            Q23=request.form.get('Q23'),
            Q24=request.form.get('Q24'),
            Q25=request.form.get('Q25'),
            Q26=request.form.get('Q26'),
            Q27=request.form.get('Q27'),
            Q28=request.form.get('Q28'),
            Q29=request.form.get('Q29'),
            Q30=request.form.get('Q30')
        )
        db.session.add(response)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
