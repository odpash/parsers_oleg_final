from flask import Flask, jsonify
import logging
import pymongo

application = Flask(__name__)
application.config['SECRET_KEY'] = 'aaaaa'
APP_NAME = 'API'
logging.basicConfig(filename="LOGLOG", level=logging.INFO)


@application.route('/create_task/task_type=<string:task_type>/data=<string:data>', methods=['GET', 'POST'])
def create_task(task_type, data):
    db_client = pymongo.MongoClient("mongodb://localhost:27017/")
    current_db = db_client["oleg_work"]
    collection = current_db["requests"]
    if task_type == 'by_fio' or task_type == 'by_username' or task_type == 'by_phone' or task_type == 'by_docs' or\
            task_type == 'by_fio' and data:
        count = collection.find().count() + 1
        collection.insert_one({'id': count, 'task_type': task_type, 'data': data, 'is_processed': False})
        d = jsonify(Status='Ok', request_id=count)
    else:
        d = jsonify(Status='Error', request_id=-1)
    return d


if __name__ == '__main__':
    application.run(host='127.0.0.1', port=8000, debug=True)
