from flask import Flask,render_template,redirect,request, jsonify
import databases.json_database as database
from databases import quiz

app = Flask(__name__)

global signin 
signin=False 

global exam
exam=False

global name
global subject
global show

def leveling(data):
    level=''
    data=int(data)
    if 0<data<3 or data==3:
        level='Poor'
    elif 3<data<5 or data==5:
        level='Average'
    elif 5<data<7 or data==7:
        level='Good'
    elif data==0:
        level='Beginner'
    elif data>7:
        level='Excellent'
        
    return level 


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
        global exam 
        exam=False
        global name 
        print(name)
        return render_template('profile_courses.html',name=name) 
    else:
        subject=['LOGIN TO MOVE FURTHER','Explore our courses and enhance your learning journey by joining us.']
        return render_template('courses.html')
    

@app.route('/login', methods=['POST'])
def login():
    global signin
    if signin==True:
        global name 
        print(name)
        return render_template('profile_courses.html',name=name) 
    else:
        return render_template('login.html')

@app.route('/signin', methods=['POST'])
def sign_in():
    username = request.form['username']
    password = request.form['password']
    # print(username,password)
    
    x=database.checking_cred(username,password)
    if x:
        global signin 
        signin=True
        global name 
        name=username
        print(name)
        return render_template('profile_courses.html',name=name)
    else:
        subject=['WRONG CREDENTIALS','Please try again']
        return render_template('continue.html',Subject=subject)

@app.route('/profile')
def profile():
    global signin
    if signin:
        global name 
        print(name)
        data,num=database.retrieve_avg_data(name)
        level=leveling(data[0])
        return render_template('profile.html',score=data[0],wrong=data[1],attempted=data[2],unattempted=data[3],number=num,name=name,level=level)

@app.route('/my_course')
def courses():
    global signin
    if signin:
        global name 
        print(name)
        return render_template('profile_courses.html',name=name) 


@app.route('/signup', methods=['POST'])
def sign_up():
    username = request.form['username']
    password = request.form['password']
    email=request.form['email']
    # print(username,password,email)
    user={"username":username,"password":password,"email":email,"test":[]}
    x=database.adding_new(user,username)
    if x:
        global signin 
        signin=True
        global name
        name=username
        print(name)
        return render_template('profile_courses.html',name=name)
        


@app.route('/button_c', methods=['POST'])
def button_c():
    print("Button Pressed for c!")
    question,ans=quiz.extract_questions('questions\c.txt')
    global subject
    subject='C'
    global answer
    answer=ans
    return render_template('question.html', questions=question,Subject=subject)

@app.route('/button_java', methods=['POST'])
def button_java():
    print("Button Pressed for java!")
    question,ans=quiz.extract_questions('questions\java.txt')
    global subject
    subject='Java'
    global answer
    answer=ans
    return render_template('question.html', questions=question,Subject=subject)

@app.route('/button_c_plus', methods=['POST'])
def button_c_plus():
    print("Button Pressed for c++!")
    question,ans=quiz.extract_questions('questions\c++.txt')
    global subject
    subject='C++'
    global answer
    answer=ans
    return render_template('question.html', questions=question,Subject=subject)

@app.route('/button_ds', methods=['POST'])
def button_ds():
    print("Button Pressed for ds!")
    question,ans=quiz.extract_questions('questions\dsa.txt')
    global subject
    subject='Datastructures'
    global answer
    answer=ans
    return render_template('question.html', questions=question,Subject=subject)

@app.route('/button_sql', methods=['POST'])
def button_sql():
    print("Button Pressed for sql!")
    question,ans=quiz.extract_questions('questions\sql.txt')
    global subject
    subject='SQL'
    global answer
    answer=ans
    return render_template('question.html', questions=question,Subject=subject)

@app.route('/button_python', methods=['POST'])
def button_python():
    print("Button Pressed for python!")
    question,ans=quiz.extract_questions('questions\python.txt')
    global subject
    subject='Python'
    global answer
    answer=ans
    return render_template('question.html', questions=question,Subject=subject)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    global exam
    answers = {}
    for key in request.form:
            if key.startswith('answer_'):
                question_index = key.split('_')[-1]
                answers[question_index] = request.form[key]
    print(answers)
    score,attempt,wrong,unattempt=checking(answers)
    global show
    show=[score,wrong,attempt,unattempt]
    exam=True
    global name
    global subject
    database.add_test_data(name,show,subject)
        # response = redirect('/submit')  # Replace '/new_page' with the URL of your new page
        # response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        # return response
    result=show
    return render_template('result.html',show=result)
    # else: 
    #     result=show
    #     return render_template('result.html',show=result)
    
@app.route('/give_data')
def give_data():
    global show 
    data=show 
    return jsonify(data)

@app.route('/api')
def get_data():
    global name 
    print(name)
    data=database.retrieve_test_data(name)
    return jsonify(data)

@app.route('/api_plot')
def get_plot():
    global name 
    print(name)
    data=database.retrieve_plot_data(name)
    return jsonify(data)

@app.route('/result')
def results():
    return render_template('exam.html')

@app.route('/logout')
def logout():
    global signin
    signin=False 
    return render_template('homepage.html')





if __name__ == '__main__':
    app.run(debug=True)
