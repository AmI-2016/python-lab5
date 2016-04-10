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
    return render_template('index.html')


@app.route('/insert_task.html', methods=['GET', 'POST'])
def insert_task():
    if request.method == 'POST':
        if ('string_for_insertion' in request.form and request.form['string_for_insertion']!=''):
            string_for_insertion = request.form['string_for_insertion']
            if ('urgent_for_insertion' in request.form and request.form['urgent_for_insertion'] == 'on'):
                urgent_for_insertion = 1
            else:
                urgent_for_insertion = 0
            db_interaction.db_insert_task(string_for_insertion, urgent_for_insertion)
        else:
            string_for_insertion = ""
    else:
        string_for_insertion = ""
    return render_template('insert_task.html', string_for_insertion = string_for_insertion)

@app.route('/show_tasks.html')
def show_tasks():
    tasks_list = db_interaction.get_sorted_tasks_list()
    return render_template('show_tasks.html', tasks_list=tasks_list)

@app.route('/delete_task.html', methods=['GET', 'POST'])
def delete_task():
    if request.method == 'POST':
        if 'substring_for_delete' in request.form:
            substring_for_delete = request.form['substring_for_delete']
            db_interaction.db_remove_task(substring_for_delete)
        else:
            substring_for_delete = ""
    else:
        substring_for_delete = ""
    tasks_list = db_interaction.get_sorted_tasks_list()
    return render_template('delete_task.html', substring_for_delete = substring_for_delete, tasks_list=tasks_list)


if __name__ == '__main__':
    app.run(debug=True)
