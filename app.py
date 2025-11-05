from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

# In-memory storage (will reset on server restart)
categories = ['Workout', 'Entrepreneurial', 'Indie Projects']
tasks = {
    'Workout': [
        {'id': 1, 'name': 'Lower Body', 'date': '', 'day': 'Monday'},
        {'id': 2, 'name': 'Upper Body', 'date': '', 'day': 'Wednesday'},
    ],
    'Entrepreneurial': [
        {'id': 3, 'name': 'Call potential customer', 'date': '2025-10-25', 'day': ''},
        {'id': 4, 'name': 'Read "Mom Test"', 'date': '', 'day': ''},
    ],
    'Indie Projects': []
}
next_id = 5

@app.route('/')
def home():
    # print(categories) # debug to see what data is being sent to the HTML
    # print(tasks) # debug to see what data is being sent to the HTML
    return render_template('task_manager.html', categories=categories, tasks=tasks)

@app.route('/add-task', methods=['POST'])
def add_task():
    global next_id
    category = request.form.get('category')
    task_name = request.form.get('task_name')
    task_date = request.form.get('task_date', '')
    task_day = request.form.get('task_day', '')
    
    if category in tasks:
        tasks[category].append({
            'id': next_id,
            'name': task_name,
            'date': task_date,
            'day': task_day
        })
        next_id += 1
    
    return redirect('/')

@app.route('/add-category', methods=['POST'])
def add_category():
    category_name = request.form.get('category_name')
    if category_name and category_name not in categories:
        categories.append(category_name)
        tasks[category_name] = []
    return redirect('/')

@app.route('/delete-task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    for category in tasks:
        tasks[category] = [t for t in tasks[category] if t['id'] != task_id]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)