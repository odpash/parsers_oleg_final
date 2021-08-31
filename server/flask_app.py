from flask import Flask, jsonify
import logging
import pymongo

application = Flask(__name__)
application.config['SECRET_KEY'] = 'aaaaa'
APP_NAME = 'API'
logging.basicConfig(filename="LOGLOG", level=logging.INFO)
DB_NAME = 'oleg_work'
DB_COLLECTION_NAME = 'requests'


@application.route('/create_task/task_type=<string:task_type>/data=<string:data>', methods=['GET', 'POST'])
def create_task(task_type, data):
    db_client = pymongo.MongoClient("mongodb://localhost:27017/")
    current_db = db_client[DB_NAME]
    collection = current_db[DB_COLLECTION_NAME]
    if task_type == 'by_fio' or task_type == 'by_username' or task_type == 'by_phone' or task_type == 'by_docs' or \
            task_type == 'by_fio' and data:
        count = collection.find().count() + 1
        collection.insert_one(
            {'id': count, 'task_type': task_type, 'data': data, 'is_processed': False, 'result': None})
        d = jsonify(Status='OK', request_id=count)
    else:
        d = jsonify(Status='ERROR', request_id=0)
    return d


@application.route('/check_request_by_id/request_id=<int:request_id>', methods=['GET', 'POST'])
def get_result(request_id):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient[DB_NAME]
    mycol = mydb[DB_COLLECTION_NAME]
    myquery = {"id": request_id}
    mydoc = mycol.find(myquery)
    if mydoc.count() > 0:
        last = ''
        for x in mydoc:
            last = x
        if last['is_processed'] is False:
            return jsonify(Status='NOT_READY', Result={})
        else:
            return jsonify(Status='OK', Result=last['result'])
    else:
        return jsonify(Status='REQUESTS_NOT_FOUND', Result={})


if __name__ == '__main__':
    application.run(host='127.0.0.1', port=8000, debug=True)
