from flask import Flask,render_template,request
import pickle
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
import matplotlib.pylab as plt
import io
import base64
# from flask import Flask, render_template
import os

app = Flask(__name__)


#load the model
save_cv = pickle.load(open('count_vectorizer.pkl','rb'))
model = pickle.load(open('movies_review_classification.pkl','rb'))

# Define the path to the images folder
img = os.path.join('static', 'image')



@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    sentence = request.form['sentence']
    sen = save_cv.transform([sentence]).toarray()
    res = model.predict(sen)[0]
    result = 'POSITIVE' if res == 1 else 'NEGATIVE'
    happy_img = os.path.join(img, 'happy.png')
    sad_img = os.path.join(img, 'sad.png')
    image = happy_img if res == 1 else sad_img
    
    return render_template('index.html', result=result, image=image)


 


# @app.route('/')
# def home():

#     return render_template('index.html', image=file,file2=file2)

# @app.route('/submit_form', methods=['POST'])
# def submit_form():
#         sentence = request.form['sentence']
#         sen = save_cv.transform([sentence]).toarray()
#         res = model.predict(sen)[0]
#         result = 'POSITIVE' if res == 1 else 'NEGATIVE' 
#         image = 'happy.png' if res == 1 else 'sad.png'
#         return render_template('index.html', result=result,image=image)



if __name__ == '__main__':
    app.run(debug=True)