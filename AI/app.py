from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/check', methods=['POST'])
def check():
    try:
        number = int(request.form['number'])
        if number % 2 == 0:
            result = f"{number} is an Even number."
        else:
            result = f"{number} is an Odd number."
        feedback = intelligent_feedback(number)
    except ValueError:
        result = "Please enter a valid integer."
        feedback = "Try again with a whole number."
    
    return render_template('result.html', result=result, feedback=feedback)

def intelligent_feedback(number):
    if number % 2 == 0:
        return "Great! Remember: Numbers divisible by 2 are even."
    else:
        return "Good job! Recall: Numbers not divisible by 2 are odd."

if __name__ == '__main__':
    app.run(debug=True)
