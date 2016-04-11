'''
Created on Apr 11, 2016
Copyright (c) 2015-2016 Teodoro Montanaro

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License
@author: tmontanaro
'''


from flask import Flask, url_for, render_template, request, redirect
import db_interaction


app = Flask(__name__)

@app.route('/')
def hello_world():
    # if no address is given, redirect to the index page
    return redirect(url_for('index'))

@app.route('/index.html')
def index():
    tasks_list = db_interaction.get_sorted_tasks_list()
    return render_template('index.html', tasks_list=tasks_list)


@app.route('/insert_task.html', methods=['POST'])
def insert_task():
    if ('description' in request.form and request.form['description']!=''):
        description = request.form['description']
        if ('urgent' in request.form and request.form['urgent'] == 'on'):
            urgent = 1
        else:
            urgent = 0
        db_interaction.db_insert_task(description, urgent)

    # back to the home page
    return redirect(url_for('index'))

@app.route('/delete_task.html', methods=['GET'])
def delete_task():
    if 'id_task' in request.args:
        id_task = request.args.get('id_task')
        db_interaction.db_remove_task_by_id(id_task)

    # back to the home page
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
