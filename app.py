from flask import Flask

app = Flask(__name__)

@app.route("/")
def get_student_number():
    student_number = "200506382"  # replace with your student number
    return {"student_number": student_number}

@app.route("/webhook")
def get_dialogflow_response():
    response_text = "Welcome to the car rental bot! How can I assist you today?"
    return {"fulfillmentText": response_text}
    
if __name__ == "__main__":
    app.run()
