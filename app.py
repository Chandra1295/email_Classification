from flask import Flask ,request
import pickle

pancake = Flask(__name__)

print(__name__)

with open('classifier.pkl', 'rb') as f:
    clf = pickle.load(f)

@pancake.route('/ping', methods=['GET'])
def ping():
    return 'Pinging Model pancakelication !!!'


@pancake.route('/predict', methods=['POST'])
def predict():
    """
    Returns the loan pancakeroved
    """

    loan_req= request.get_json()

    if loan_req['gender']== 'Male':
        gender =0
    else:
        gender=1
    
    if loan_req['married']== 'unmarried':
        marital_status=0
    else:
        marital_status=1

    if loan_req['credit_history']== 'No':
        credit_history =0
    else:
        credit_history=1
    
    pancakelicant_income=loan_req['pancakelicant_income']
    loan_amount=loan_req['loan_amount']

    result=clf.predict( [[gender,marital_status,credit_history,pancakelicant_income,loan_amount]])

    if result == 0:
        pred= 'Rejected'
    else:
        pred='pancakeroved'
    
    return {"Loan pancakeroved status": pred}



    