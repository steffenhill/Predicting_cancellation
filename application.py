import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import statsmodels.api as sm
from sklearn import linear_model

app = Flask(__name__)
model = pickle.load(open('trained_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = list(request.form.values())[0].split(',')
    final_features = [np.array(int_features)]
    prediction = model.predict_proba(final_features)
    output = prediction[0][0] * 100
    return render_template('index.html', prediction_text='The reservation has a {:.2f}% chance of not cancellation.'.format(output))
    

# @app.route('/results',methods=['POST'])
# def results():

#     data = request.get_json(force=True)
#     prediction = model.predict([np.array(list(data.values()))])

#     output = prediction[0]
#     return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)



