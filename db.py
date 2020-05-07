from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# association_table is between User IDs and Channel IDs (m-m relationship)
association_table = db.Table('Association', db.Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('channel_id', db.Integer, db.ForeignKey('channels.id'))
    )


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    channels = db.relationship('Channel', secondary = association_table, back_populates = 'users' )
    user_messages = db.relationship('Message', cascade = 'delete')

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')

    def short_serialize(self):
        return {
            'user_id': self.id,
            'name': self.name
        }

    def serialize(self):
        return {
            'user_id': self.id,
            'name': self.name,
            'channels': [c.short_serialize() for c in self.channels],
            'messages': [m.user_call_serialize() for m in self.user_messages]
        }


class Channel(db.Model):
    __tablename__ = 'channels'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    users = db.relationship('User', secondary = association_table, back_populates = 'channels')
    channel_messages = db.relationship('Message', cascade = 'delete')

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')

    def short_serialize(self):
        return {
            'channel_id': self.id,
            'name':self.name
        }


    def serialize(self):
        return {
            'channel_id': self.id,
            'name': self.name,
            'users': [u.short_serialize() for u in self.users],
            'messages': [m.channel_call_serialize() for m in self.channel_messages]
        }


class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    channel_id = db.Column(db.Integer, db.ForeignKey('channels.id'), nullable = False)

    def __init__(self, **kwargs):
        self.content = kwargs.get('content')
        self.user_id = kwargs.get('user_id')
        self.channel_id = kwargs.get('channel_id')

    # Specifically for serializing when calling User so that channel_id appears in message instances
    def user_call_serialize(self):
        channel = Channel.query.filter_by(id = self.channel_id).first()
        return {
            'message_id': self.id,
            'channel_id': channel.short_serialize(),
            'content': self.content
        }

    # Specifically for serializing when calling Channel so that user_id appears in message instances
    def channel_call_serialize(self):
        user = User.query.filter_by(id = self.user_id).first()
        return {
            'message_id': self.id,
            'user_id': user.short_serialize(),
            'content': self.content
        }

    def short_serialize(self):
        return {
            'message_id': self.id,
            'content': self.content
        }

    def serialize(self):
        channel = Channel.query.filter_by(id = self.channel_id).first()
        user = User.query.filter_by(id = self.user_id).first()
        return {
            'message_id': self.id,
            'user': user.short_serialize(),
            'channel': channel.short_serialize(),
            'content':self.content
        }
