import json
from flask import Flask, request
import dao
from db import db



app = Flask(__name__)
db_filename = "cms.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.create_all()

# generalized response formats
def success_response(data, code=200):
    return json.dumps({"success": True, "data": data}), code

def failure_response(message, code=404):
    return json.dumps({"success": False, "error": message}), code


# routes below

@app.route('/api/users/', methods = ['GET'])
def get_users():
    return success_response(dao.get_all_users())


@app.route('/api/users/', methods = ['POST'])
def create_user():
    body = json.loads(request.data)
    name = body.get('name')
    return success_response(dao.create_a_user(name), 201)


@app.route('/api/users/<int:user_id>/', methods = ['DELETE'])
def delete_user(user_id):
    check_user = dao.get_user_by_id(user_id)
    if check_user is None:
        return failure_response('User not found, user cannot be deleted.')
    return success_response(dao.delete_user_by_id(user_id), 201)


@app.route('/api/users/<int:user_id>/', methods = ['GET'])
def get_spec_user(user_id):
    get_user = dao.get_user_by_id(user_id)
    if get_user is None:
        return failure_response('User not found.')
    return success_response(get_user)


@app.route('/api/channels/', methods = ['GET'])
def get_all_channels():
    return success_response(dao.get_all_channels())


@app.route('/api/channels/', methods = ['POST'])
def create_channel():
    body = json.loads(request.data)
    name = body.get('name')
    return success_response(dao.create_a_channel(name), 201)


@app.route('/api/channels/<int:channel_id>/', methods = ['GET'])
def get_spec_channel(channel_id):
    select_channel = dao.get_channel_by_id(channel_id)
    if select_channel is None:
        return failure_response('Channel not found.')
    return success_response(select_channel)


@app.route('/api/channels/<int:channel_id>/', methods = ['DELETE'])
def delete_channel(channel_id):
    select_channel = dao.get_channel_by_id(channel_id)
    if select_channel is None:
        return failure_response('Channel not found, unable to delete channel.')
    return success_response(dao.delete_channel_by_id(channel_id), 201)


@app.route('/api/channels/<int:channel_id>/', methods = ['POST'])
def add_user_to_channel(channel_id):
    body = json.loads(request.data)
    user_id = body.get('user_id')
    check_channel = dao.get_channel_by_id(channel_id)
    if check_channel is None:
        return failure_response('Channel does not exist.')
    return success_response(dao.add_user_to_channel(user_id, channel_id), 201)


@app.route('/api/channels/<int:channel_id>/message/', methods = ['POST'])
def add_message_to_channel(channel_id):
    body = json.loads(request.data)
    user_id = body.get('user_id')
    content = body.get('content')
    find_channel = dao.get_channel_by_id(channel_id)
    if find_channel is None:
        return failure_response('Channel not found, cannot add message.')

    check_user = dao.check_user_in_channel(user_id, channel_id)
    if check_user is None:
        return failure_response('User is not found in the channel.')
    return success_response(dao.create_message_to_channel(user_id, channel_id, content), 201)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
