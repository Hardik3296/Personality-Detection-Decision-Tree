from flask import Flask, request, render_template
from cloud import dct
import os

app = Flask(__name__)

PORT = int(os.getenv('VCAP_APP_PORT', '8000'))

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/take-test/')
def test_form():
	return render_template('Test_page.html')
 
@app.route('/know-more/')
def detail_form():
	return render_template('details.html')

@app.route('/already-score/')
def scores_form():
	return render_template('my-form.html')

def result(string):
	if (string == 'ARCHITECT'): return render_template('Architect.html')
	elif(string == 'ADVOCATE'):return render_template('Advocate.html')
	elif(string == 'CAMPAIGNER'):return render_template('Campaigner.html')
	elif(string == 'COMMANDER'):return render_template('Commander.html')
	elif(string == 'CONSUL'):return render_template('Consul.html')
	elif(string == 'DEBATER'):return render_template('Debater.html')
	elif(string == 'DEFENDER'):return render_template('Defender.html')
	elif(string == 'EXECUTIVE'):return render_template('Executive.html')
	elif(string == 'LOGICIAN'):return render_template('Logician.html')
	elif(string == 'LOGISTICIAN'):return render_template('Logistician.html')
	elif(string == 'MEDIATOR'):return render_template('Mediator.html')
	elif(string == 'PROTAGONIST'):return render_template('Protagonist.html')
	elif(string == 'ADVENTURER'):return render_template('Adventurer.html')
	elif(string == 'ENTERTAINER'):return render_template('Entertainer.html')
	elif(string == 'ENTREPRENEUR'):return render_template('Entrepreneur.html')
	elif(string == 'VIRTUOSO'):return render_template('Virtuoso.html')

@app.route('/already-score/', methods=['GET','POST'])
def my_form_post():
	text1 = request.form['text']
	processed_text1 = text1.upper()
	print(text1)
	text2 = request.form['text']
	processed_text2 = text2.upper()
	text3 = request.form['text']
	processed_text3 = text3.upper()
	text4 = request.form['text']
	processed_text4 = text4.upper()
	text5 = request.form['text']
	processed_text5 = text5.upper()
	string = dct(processed_text1,processed_text2,processed_text3,processed_text4,processed_text5)
	x = result(string)
	return x

def checker(var):
	val = int(var);
	if (val != 1 and val != 2 and val != 3 and val != 4 and val != 5): val = 3;
	return val
def negation(val):
	if(val == 1): return 5
	elif(val == 2): return 4
	elif(val == 4): return 2
	elif(val == 5):return 1
	else: return 3

@app.route('/take-test/',methods = ['GET','POST'])
def evaluate():
	c1 = 0
	c2 = 0
	c3 = 0
	c4 = 0
	c5 = 0
	#Collecting value for 1 corresponding to extraversion
	tp11 = request.form['text']
	processed_tp11 = tp11.upper()
	print(tp11)
	tn11 = request.form['text']
	processed_tn11 = tn11.upper()
	print(tn11)
	c1 = c1 + 2*checker(tp11);
	c1 = c1 + 2*negation(checker(tn11));
	tp12 = request.form['text']
	processed_tp12 = tp12.upper()
	tn12 = request.form['text']
	processed_tn12 = tn12.upper()
	c1 = c1 + 2*checker(tp12);
	c1 = c1 + 2*negation(checker(tn12));
	tp13 = request.form['text']
	processed_tp13 = tp13.upper()
	tn13 = request.form['text']
	processed_tn13 = tn13.upper()
	c1 = c1 + 2*checker(tp13);
	c1 = c1 + negation(checker(tn13));
	tp14 = request.form['text']
	processed_tp14 = tp14.upper()
	tn14 = request.form['text']
	processed_tn14 = tn14.upper()
	c1 = c1 + 2*checker(tp14);
	c1 = c1 + 2*negation(checker(tn14));
	tp15 = request.form['text']
	processed_tp15 = tp15.upper()
	tn15 = request.form['text']
	processed_tn15 = tn15.upper()
	c1 = c1 + 2*checker(tp15);
	c1 = c1 + 2*negation(checker(tn15));
	#Collecting value for 2 corresponding to agreeableness
	#This is the Thinking attribute observant
	tp21 = request.form['text']
	processed_tp21 = tp21.upper()
	tn21 = request.form['text']
	processed_tn21 = tn21.upper()
	c2 = c2 + 2*checker(tp21);
	c2 = c2 + 2*negation(checker(tn21));
	tp22 = request.form['text']
	processed_tp22 = tp22.upper()
	tn22 = request.form['text']
	processed_tn22 = tn22.upper()
	c2 = c2 + 2*checker(tp22);
	c2 = c2 + 2*negation(checker(tn22));
	tp23 = request.form['text']
	processed_tp23 = tp23.upper()
	tn23 = request.form['text']
	processed_tn23 = tn23.upper()
	c2 = c2 + 2*checker(tp23);
	c2 = c2 + 2*negation(checker(tn23));
	tp24 = request.form['text']
	processed_tp24 = tp24.upper()
	tn24 = request.form['text']
	processed_tn24 = tn24.upper()
	c2 = c2 + 2*checker(tp24);
	c2 = c2 + 2*negation(checker(tn24));
	tp25 = request.form['text']
	processed_tp25 = tp25.upper()
	tn25 = request.form['text']
	processed_tn25 = tn25.upper()
	c2 = c2 + 2*checker(tp25);
	c2 = c2 + 2*negation(checker(tn25));
	#Collecting value for 3 corresponding to conscientiousness
	#This is the Thinking attribute
	tp31 = request.form['text']
	processed_tp31 = tp31.upper()
	tn31 = request.form['text']
	processed_tn31 = tn31.upper()
	c3 = c3 + 2*checker(tp31);
	c3 = c3 + 2*negation(checker(tn31));
	tp32 = request.form['text']
	processed_tp32 = tp32.upper()
	tn32 = request.form['text']
	processed_tn32 = tn32.upper()
	c3 = c3 + 2*checker(tp32);
	c3 = c3 + 2*negation(checker(tn32));
	tp33 = request.form['text']
	processed_tp33 = tp33.upper()
	tn33 = request.form['text']
	processed_tn33 = tn33.upper()
	c3 = c3 + 2*checker(tp33);
	c3 = c3 + 2*negation(checker(tn33));
	tp34 = request.form['text']
	processed_tp34 = tp34.upper()
	tn34 = request.form['text']
	processed_tn34 = tn34.upper()
	c3 = c3 + 2*checker(tp34);
	c3 = c3 + 2*negation(checker(tn34));
	tp35 = request.form['text']
	processed_tp35 = tp35.upper()
	tn35 = request.form['text']
	processed_tn35 = tn35.upper()
	c3 = c3 + 2*checker(tp35);
	c3 = c3 + 2*negation(checker(tn35));
	#Collecting value for 4 corresponding to emotional stability
	#This is the assertive/turbulent attribute
	tp41 = request.form['text']
	processed_tp41 = tp41.upper()
	tn41 = request.form['text']
	processed_tn41 = tn41.upper()
	c4 = c4 + 2*checker(tp41);
	c4 = c4 + 2*negation(checker(tn41));
	tp42 = request.form['text']
	processed_tp42 = tp42.upper()
	tn42 = request.form['text']
	processed_tn42 = tn42.upper()
	c4 = c4 + 2*checker(tp42);
	c4 = c4 + 2*negation(checker(tn42));
	tp43 = request.form['text']
	processed_tp43 = tp43.upper()
	tn43 = request.form['text']
	processed_tn43 = tn43.upper()
	c4 = c4 + 2*checker(tp43);
	c4 = c4 + 2*negation(checker(tn43));
	tp44 = request.form['text']
	processed_tp44 = tp44.upper()
	tn44 = request.form['text']
	processed_tn44 = tn44.upper()
	c4 = c4 + 2*checker(tp44);
	c4 = c4 + 2*negation(checker(tn44));
	tp45 = request.form['text']
	processed_tp45 = tp45.upper()
	tn45 = request.form['text']
	processed_tn45 = tn45.upper()
	c4 = c4 + 2*checker(tp45);
	c4 = c4 + 2*negation(checker(tn45));
	#Collecting value for 5 corresponding to intellect/imagination
	#This is judging/thinking attribute
	tp51 = request.form['text']
	processed_tp51 = tp51.upper()
	tn51 = request.form['text']
	processed_tn51 = tn51.upper()
	c5 = c5 + 2*checker(tp51);
	c5 = c5 + 2*negation(checker(tn51));
	tp52 = request.form['text']
	processed_tp52 = tp52.upper()
	tn52 = request.form['text']
	processed_tn52 = tn52.upper()
	c5 = c5 + 2*checker(tp52);
	c5 = c5 + 2*negation(checker(tn52));
	tp53 = request.form['text']
	processed_tp53 = tp53.upper()
	tn53 = request.form['text']
	processed_tn53 = tn53.upper()
	c5 = c5 + 2*checker(tp53);
	c5 = c5 + 2*negation(checker(tn53));
	tp54 = request.form['text']
	processed_tp54 = tp54.upper()
	tn54 = request.form['text']
	processed_tn54 = tn54.upper()
	c5 = c5 + 2*checker(tp54);
	c5 = c5 + 2*negation(checker(tn54));
	tp55 = request.form['text']
	processed_tp55 = tp55.upper()
	tn55 = request.form['text']
	processed_tn55 = tn55.upper()
	c5 = c5 + 2*checker(tp55);
	c5 = c5 + 2*negation(checker(tn55));

	#Evaluating test result.
	#Result should be [1,5]
	#If variable has 'n' in it, it is the negative one
	#If variable has 'p' in it, it is the positive one
	#Sum of all attributes*2 gives the answer to each of out personality score
	string = dct(c1,c2,c3,c5,c4)
	x = result(string)
	return x

if __name__=='__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)
