from flask import Flask,render_template,url_for,request
from flask import jsonify
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib

# load the model from disk
filename = 'wine_predict_nlp_model.pkl'
clf = pickle.load(open(filename, 'rb'))
cv=pickle.load(open('tranform.pkl','rb'))
my_prediction = ""


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def predict():
  global my_prediction

  if request.method == 'POST':
    message = request.form['message']
    print(message)
    data = [message]
    vect = cv.transform(data).toarray()
    my_prediction = clf.predict(vect)
    # return my_prediction
    # print(my_prediction)
  return render_template('description.html', prediction = my_prediction)





if __name__ == '__main__':
	app.run(debug=True)

