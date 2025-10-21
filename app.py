from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('plan_week.html')

@app.route('/save-plan', methods=['POST'])
def save_plan():
    # We'll add database here next
    print(request.form)  # For now, just print
    return "Plan saved! (temporarily)"

if __name__ == '__main__':
    app.run(debug=True)