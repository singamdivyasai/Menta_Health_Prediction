from distutils.log import debug
import pickle
import numpy as np
import numpy as np
import pandas as pd 

from flask import Flask, render_template, request
model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
@app.route('/first')
def first():
    return render_template('first.html')
@app.route('/login')
def login():
    return render_template('login.html')
def home():
	return render_template('home.html')
@app.route('/upload')
def upload():
    return render_template('upload.html')  
@app.route('/preview',methods=["POST"])
def preview():
    if request.method == 'POST':
        dataset = request.files['datasetfile']
        df = pd.read_csv(dataset,encoding = 'unicode_escape')
        df.set_index('Id', inplace=True)
        return render_template("preview.html",df_view = df) 

@app.route('/chart')
def chart():
    return render_template('chart.html')




@app.route("/prediction1", methods=['GET'])
def prediction1():
    return render_template('index.html')


@app.route("/accuracy", methods=['GET'])
def accuracy():
    return render_template('accuracy.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Gender = request.form['Gender']
        self_employed = request.form['self_employed']
        family_history = request.form['family_history']
        work_interfere = request.form['work_interfere']
        no_employees = request.form['no_employees']
        remote_work = request.form['remote_work']
        tech_company = request.form['tech_company']
        anonymity = request.form['anonymity']
        leave = request.form['leave']
        mental_health_consequence = request.form['mental_health_consequence']
        phys_health_consequence = request.form['phys_health_consequence']
        coworkers = request.form['coworkers']
        supervisor = request.form['supervisor']
        mental_health_interview = request.form['mental_health_interview']
        phys_health_interview = request.form['phys_health_interview']
        mental_vs_physical = request.form['mental_vs_physical']
        obs_consequence = request.form['obs_consequence']
        benefits = request.form['benefits']
        care_options = request.form['care_options']
        wellness_program = request.form['wellness_program']
        seek_help = request.form['seek_help']

        arr = np.array([[Gender, self_employed, family_history, work_interfere, no_employees, remote_work,
                         tech_company, anonymity, leave, mental_health_consequence, phys_health_consequence, coworkers,
                         supervisor, mental_health_interview, phys_health_interview, mental_vs_physical,  obs_consequence,
                         benefits, care_options,  wellness_program, seek_help]])
        pred = model.predict(arr)
        return render_template('predict.html',prediction=pred)


if __name__ == "__main__":
    app.run(debug=True)
