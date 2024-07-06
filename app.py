from flask import Flask, render_template, request, redirect, url_for
import requests
app = Flask(__name__)

tasks = []

@app.route('/')
def home():
  data = {
        'title': 'Welcome to David\'s Website',
        'heading': 'Welcome to my Flask app!',
        'description': 'This is a simple Flask application using an HTML template and a dictionary.',
        'new_items':['Click here to read the story  of', 'item 2'],
        'new_items2':[' dave b new data of', 'item 2 dylan michal'],
  }
  return render_template('index.html', data=data)

@app.route('/about')
def about():
  about_data = {
        'title': 'About Page',
        'heading': 'About This Flask App',
        'content_one': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Optio, aspernatur. Neque ex deserunt omnis? Minus excepturi soluta amet provident mollitia dolor ipsam porro illum architecto? Adipisci culpa recusandae autem mollitia.',
        'content_two': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Optio, aspernatur. Neque ex deserunt omnis? Minus excepturi soluta amet provident mollitia dolor ipsam porro illum architecto? Adipisci culpa recusandae autem mollitia.'
  }
  return render_template('about.html', data=about_data)

@app.route('/tasks', methods=['GET', 'POST'])
def task_list():
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            tasks.append({'task': task, 'complete': False})
        return redirect(url_for('task_list'))
    return render_template('tasks.html', tasks=tasks, enumerate=enumerate)


@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['complete'] = not tasks[task_id]['complete']
    return redirect(url_for('task_list'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    if request.method == 'POST':
        new_task = request.form.get('task')
        if 0 <= task_id < len(tasks) and new_task:
            tasks[task_id]['task'] = new_task
        return redirect(url_for('task_list'))
    
    task = tasks[task_id] if 0 <= task_id < len(tasks) else None
    return render_template('edit_task.html', task_id=task_id, task=task)

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('task_list'))

@app.route('/iss-location')
def iss_location():
    url = 'http://api.open-notify.org/iss-now.json'
    try:
        response = requests.get(url)
        data = response.json()
        if data['message'] == 'success':
            iss_position = data['iss_position']
            return render_template('location.html', iss_position=iss_position)
        else:
            error_message = 'Could not retrieve ISS location.'
            return render_template('location.html', error_message=error_message)
    except requests.exceptions.RequestException as e:
        return render_template('location.html', error_message=str(e))

if __name__ == '__main__':
  app.run(debug=True)

  