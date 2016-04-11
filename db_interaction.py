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

import sqlite3
import operator


def db_insert_task(text, urgent):
    '''
    :param text: text that we want to insert as task in the db
    :param urgent: 0 if the task is not urgent, 1 otherwise

    This method insert a task in the database
    '''

    # prepare the query text
    sql = """INSERT INTO task(todo, urgent) VALUES (?, ?)"""

    #connect to the db
    conn = sqlite3.connect("task_list.db")
    cursor = conn.cursor()

    try:
        #execute the query passing the needed parameters
        cursor.execute(sql, (text, urgent) )
        #commit all pending queries
        conn.commit()
    except Exception,e:
        print str(e)
        # if something goes wrong: rollback
        conn.rollback()

    #close the connection
    conn.close()


def get_sorted_tasks_list():
    '''
    Get existing tasks from the database
    '''

    tasks_list = []
    sql = "SELECT id_task, todo FROM task order by todo ASC" #here we order data using "order by"
    conn = sqlite3.connect("task_list.db")

    # to remove u from sqlite3 cursor.fetchall() results
    conn.text_factory = sqlite3.OptimizedUnicode


    cursor = conn.cursor()
    cursor.execute(sql)

    results = cursor.fetchall()

    for task in results:
        tasks_list.append((task[0],task[1]))  #we create a list of tuples (key, value) where key is the task id and the value is the text of the task

    conn.close()

    return tasks_list

def db_remove_task_by_id(id_task):
    '''
    :param id_task: unique identificator for the task we want to remove from the db

    This method remove from the db a specific task
    '''

    # prepare the query text
    sql = "delete from task where id_task = ?"


    #connect to the db
    conn = sqlite3.connect("task_list.db")
    cursor = conn.cursor()

    try:
        #execute the query passing the needed parameters
        cursor.execute(sql, (id_task, ) )
        #commit all pending executed queries in the connection
        conn.commit()
    except Exception,e:
        print str(e)
        # if something goes wrong: rollback
        conn.rollback()

    #close the connection
    conn.close()