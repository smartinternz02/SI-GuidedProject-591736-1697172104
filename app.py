from flask import *
import pickle
import os
import re
import pandas
import numpy as np
app = Flask(__name__)
model = pickle.load(open('RandomForestClassifier_model (1).pkl','rb'))
@app.route('/', methods = [ 'POST', 'GET'])
def homepage():
    return render_template('index.html')
@app.route('/prediction', methods = [ 'POST', 'GET'])
def prediction():
    return render_template('prediction.html')
@app.route('/submit', methods=["POST","GET"])# route to show the predictions in a web UI
def submit():
    # reading the inputs given by the user
    input_feature=[int(x) for x in request.form.values()]
    input_feature=[np.array(input_feature)]
    print(input_feature)
    print((input_feature))
    names = ['Gender', 'Education Level', 'Institution Type', 'IT Student','Financial Condition', 'Internet Type', 'Network Type','Device']
    data = pandas.DataFrame(input_feature, columns=names)
    print(data)
    # predictions using the loaded model file
    prediction=model.predict(data)
    print(prediction)
    if (prediction == 0):
        return render_template("result.html", result ="Adaptivity Level is High")
    elif (prediction == 1):
        return render_template("result.html",result ="Adaptivity Level is medium")
    else:
        return render_template("result.html", result = "Adaptivity Level is Low")
    #showing the prediction results in a UI
if __name__=="__main__":
  # app.run(host='0.0.0.0', port-8000, debug=True)
    port=int(os.environ.get('PORT',5000)) 
    app.run(debug=True)
    if __name__ == '__main__':
        app.run(debug=True)
