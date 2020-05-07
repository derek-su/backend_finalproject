from db import db, User, Channel, Message

# Methods below:

def get_all_users():
    return [user.serialize() for user in User.query.all()]


def create_a_user(name):
    new_user = User(name = name)
    db.session.add(new_user)
    db.session.commit()
    return new_user.serialize()


def get_user_by_id(user_id):
    select_user = User.query.filter_by(id = user_id).first()
    if select_user is None:
        return None
    return select_user.serialize()


def delete_user_by_id(user_id):
    select_user = User.query.filter_by(id = user_id).first()
    if select_user is None:
        return None

    db.session.delete(select_user)
    db.session.commit()
    return select_user.serialize()


def get_all_channels():
    return [channel.serialize() for channel in Channel.query.all()]


def create_a_channel(channel_name):
    new_channel = Channel(name = channel_name)
    db.session.add(new_channel)
    db.session.commit()
    return new_channel.serialize()


def get_channel_by_id(channel_id):
    select_channel = Channel.query.filter_by(id = channel_id).first()
    if select_channel is None:
        return None
    return select_channel.serialize()


def delete_channel_by_id(channel_id):
    select_channel = Channel.query.filter_by(id = channel_id).first()
    if select_channel is None:
        return None
    db.session.delete(select_channel)
    db.session.commit()
    return select_channel.serialize()


def add_user_to_channel(user_id, channel_id):
    adding_user = User.query.filter_by(id = user_id).first()
    channel = Channel.query.filter_by(id = channel_id).first()
    channel.users.append(adding_user)
    db.session.commit()
    return channel.serialize()



def check_user_in_channel(user_id, channel_id):
    select_channel = Channel.query.filter_by(id = channel_id).first()
    for user in select_channel.users:
        if user.id == user_id:
            return True
    return None


def create_message_to_channel(user_id, channel_id, content):
    new_message = Message(user_id = user_id, channel_id = channel_id, content = content)
    db.session.add(new_message)
    db.session.commit()
    return new_message.serialize()
