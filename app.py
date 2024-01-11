from flask import Flask,render_template,redirect,request, jsonify
from quiz import extract_questions
from database import  checking_cred,adding_new

app = Flask(__name__)

global signin 
signin=False 

global exam
exam=False


def checking(answers):
    global answer
    correct=answer 
    score=0
    attempt=0
    total=0
    for key in correct:
        if key in answers:
            if correct[key]==answers[key]:
                score+=1 
            attempt+=1
        total+=1
    unattempt=total-attempt
    wrong=attempt-score
    return score,attempt,wrong,unattempt

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/course')
def course():
    if signin==True:
       global name 
       original=name
       global exam 
       exam=False
       return render_template('courses.html',Username=original)
    else:
        subject=['LOGIN TO MOVE FURTHER','Explore our courses and enhance your learning journey by joining us.']
        return render_template('continue.html',Subject=subject)
    

@app.route('/login')
def login():
    if signin==True:
        return render_template('already.html')
    else:
        return render_template('login.html')

@app.route('/signin', methods=['POST'])
def sign_in():
    username = request.form['username']
    password = request.form['password']
    # print(username,password)
    x=checking_cred(username,password)
    if x:
        global signin 
        signin=True
        global name 
        name=username
        return render_template('courses.html',Username=name)
    else:
        subject=['WRONG CREDENTIALS','Please try again']
        return render_template('continue.html',Subject=subject)

    

@app.route('/signup', methods=['POST'])
def sign_up():
    username = request.form['username']
    password = request.form['password']
    email=request.form['email']
    # print(username,password,email)
    user={"username":username,"password":password,"email":email}
    x=adding_new(user)
    if x:
        global signin 
        signin=True
        subject=['WELCOME !!!','Explore our platform to fill your curiosity']
        global name 
        name=username
        return render_template('continue.html',Subject=subject)


@app.route('/button_c', methods=['POST'])
def button_c():
    print("Button Pressed for c!")
    question,ans=extract_questions('questions\c.txt')
    subject='C'
    global answer
    answer=ans
    return render_template('question.html', questions=question,Subject=subject)

@app.route('/button_java', methods=['POST'])
def button_java():
    print("Button Pressed for java!")
    question,ans=extract_questions('questions\java.txt')
    subject='Java'
    global answer
    answer=ans
    return render_template('question.html', questions=question,Subject=subject)

@app.route('/button_c_plus', methods=['POST'])
def button_c_plus():
    print("Button Pressed for c++!")
    question,ans=extract_questions('questions\c++.txt')
    subject='C++'
    global answer
    answer=ans
    return render_template('question.html', questions=question,Subject=subject)

@app.route('/button_ds', methods=['POST'])
def button_ds():
    print("Button Pressed for ds!")
    question,ans=extract_questions('questions\dsa.txt')
    subject='Datastructures'
    global answer
    answer=ans
    return render_template('question.html', questions=question,Subject=subject)

@app.route('/button_sql', methods=['POST'])
def button_sql():
    print("Button Pressed for sql!")
    question,ans=extract_questions('questions\sql.txt')
    subject='SQL'
    global answer
    answer=ans
    return render_template('question.html', questions=question,Subject=subject)

@app.route('/button_python', methods=['POST'])
def button_python():
    print("Button Pressed for python!")
    question,ans=extract_questions('questions\python.txt')
    subject='Python'
    global answer
    answer=ans
    return render_template('question.html', questions=question,Subject=subject)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    global show
    global exam
    if exam==False:
        answers = {}
        for key in request.form:
            if key.startswith('answer_'):
                question_index = key.split('_')[-1]
                answers[question_index] = request.form[key]
        print(answers)
        score,attempt,wrong,unattempt=checking(answers)
        show=[score,wrong,attempt,unattempt]
        exam=True
        response = redirect('/submit')  # Replace '/new_page' with the URL of your new page
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        return response
    else: 
        result=show
        return render_template('result.html',show=result)
    
@app.route('/give_data')
def give_data():
    global show 
    data=show 
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
