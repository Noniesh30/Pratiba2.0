import random 
import json

def extract_questions(file_path):
    with open(file_path, 'r',encoding='utf-8') as file:
        x = file.read()
        list_of_questions=x.split('$')
        list_of_dicts=[]
        for i in list_of_questions:
            python_dict = json.loads(i)
            list_of_dicts.append(python_dict)
            # print(i)
        random_questions = random.sample(list_of_dicts, 15)
        Answers={}
        count=0
        for i in range(len(random_questions)):
            question=random_questions[i]
            if file_path=='questions\java.txt':
                if  "code" in question:
                    main_q=question["question"]
                    code_q=question["code"]
                    question["question"]=main_q+"\n"+code_q
            ans=question["correct_answer"]
            count+=1
            Answers[str(count)]=ans
        return random_questions,Answers 
    



