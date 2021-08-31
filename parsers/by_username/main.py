import multiprocessing
import pymongo
import search_script


DB_NAME = 'oleg_work'
DB_COLLECTION_NAME = 'requests'


def read_requests():
    db_client = pymongo.MongoClient("mongodb://localhost:27017/")
    current_db = db_client[DB_NAME]
    collection = current_db[DB_COLLECTION_NAME]
    a = collection.find()
    to_update = []
    for i in a:
        if i['is_processed'] is False and i['task_type'] == 'by_username':
            to_update.append([i['id'], i['data']])
    return to_update


def process_requests(data):
    with multiprocessing.Pool(len(data)) as p:
        result = p.map(search_script.check, data)
    return result


def write_requests(data):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient[DB_NAME]
    mycol = mydb[DB_COLLECTION_NAME]
    for i in data:
        idx, res = i[0], i[1]
        myquery = {"id": idx}
        newvalues = {"$set": {"is_processed": True}}
        mycol.update_many(myquery, newvalues)
        newvalues = {"$set": {'result': res}}
        mycol.update_many(myquery, newvalues)


def main():
    while True:
        data = read_requests()
        if len(data) > 0:
            print("Started parse,", data)
            info = process_requests(data)
            print('Data getted,', info)
            write_requests(info)
            print('Updated')


if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()
