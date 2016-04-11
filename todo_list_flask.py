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
    if ('string_for_insertion' in request.form and request.form['string_for_insertion']!=''):
        string_for_insertion = request.form['string_for_insertion']
        if ('urgent_for_insertion' in request.form and request.form['urgent_for_insertion'] == 'on'):
            urgent_for_insertion = 1
        else:
            urgent_for_insertion = 0
        db_interaction.db_insert_task(string_for_insertion, urgent_for_insertion)

    # back to the home page
    return redirect(url_for('index'))

@app.route('/delete_task.html', methods=['GET'])
def delete_task():
    if 'string_for_delete' in request.args:
        string_for_delete = request.args.get('string_for_delete')
        db_interaction.db_remove_task(string_for_delete)

    # back to the home page
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
