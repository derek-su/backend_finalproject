# API Specification for Slack-style Program

# Expected Functionality:

## Get all Users

### GET /api/users/

> Response:

```
{
    "success": true,
    "data": [
        {
            "user_id": 1,
            "name": "Derek S",
            "channels": [
                {
                    "channel_id": 1,
                    "name": "Announcements"
                },
                {
                    "channel_id": 2,
                    "name": "Backend"
                },
                {
                    "channel_id": 3,
                    "name": "Pollo"
                }
            ],
            "messages": [
                {
                    "message_id": 1,
                    "channel_id": {
                        "channel_id": 1,
                        "name": "Announcements"
                    },
                    "content": "Hello this will be the first message in the Announcements channel!"
                },
                {
                    "message_id": 3,
                    "channel_id": {
                        "channel_id": 2,
                        "name": "Backend"
                    },
                    "content": "Testing 123 in channel Backend!"
                },
                {
                    "message_id": 6,
                    "channel_id": {
                        "channel_id": 3,
                        "name": "Test case"
                    },
                    "content": "Hello I am suppose to appear"
                }
            ]
        },
        {
            "user_id": 2,
            "name": "Steve K",
            "channels": [
                {
                    "channel_id": 2,
                    "name": "Backend"
                }
            ],
            "messages": [
                {
                    "message_id": 4,
                    "channel_id": {
                        "channel_id": 2,
                        "name": "Backend"
                    },
                    "content": "Hi my name is Steve and I'm writing in the Backend channel."
                }
            ]
        }
    ]
}
```


## Create a User

### POST /api/users/

> Request:

```
{
	"name": <USER INPUT>
}
```

> Response:

```
{
    "success": true,
    "data": {
        "user_id": <ID>,
        "name": <USER INPUT>,
        "channels": [],
        "messages": []
    }
}
```

## Get Specific User

### GET /api/users/{int:user_id}/

> Response:

```
{
    "success": true,
    "data": {
        "user_id": 2,
        "name": "Steve K",
        "channels": [
            {
                "channel_id": 2,
                "name": "Backend"
            }
        ],
        "messages": [
            {
                "message_id": 4,
                "channel_id": {
                    "channel_id": 2,
                    "name": "Backend"
                },
                "content": "Hi my name is Steve and I'm writing in the Backend channel."
            },
            {
                "message_id": 5,
                "channel_id": {
                    "channel_id": 1,
                    "name": "Announcements"
                },
                "content": "Hi my name is Steve and I'm writing in ANNOUCEMENTS."
            }
        ]
    }
}
```
## Delete User

### DELETE /api/users/{int:user_id}/

> Response:

```
{
    "success": true,
    "data": {
        "user_id": <ID>,
        "name": <USER INPUT FOR NAME>,
        "channels": [],
        "messages": []
    }
}
```

## Get All Channels

### GET /api/channels/

> Response:

```
{
    "success": true,
    "data": [
        {
            "channel_id": 1,
            "name": "Announcements",
            "users": [
                {
                    "user_id": 1,
                    "name": "Derek S"
                }
            ],
            "messages": [
                {
                    "message_id": 1,
                    "user_id": {
                        "user_id": 1,
                        "name": "Derek S"
                    },
                    "content": "Hello this will be the first message in the Annoncements channel!"
                },
                {
                    "message_id": 2,
                    "user_id": {
                        "user_id": 1,
                        "name": "Derek S"
                    },
                    "content": "This is my second message."
                },
                {
                    "message_id": 5,
                    "user_id": {
                        "user_id": 2,
                        "name": "Steve K"
                    },
                    "content": "Hi my name is Steve and I'm writing in ANNOUCEMENTS."
                }
            ]
        },
        {
            "channel_id": 2,
            "name": "Backend",
            "users": [
                {
                    "user_id": 1,
                    "name": "Derek S"
                },
                {
                    "user_id": 2,
                    "name": "Steve K"
                }
            ],
            "messages": [
                {
                    "message_id": 3,
                    "user_id": {
                        "user_id": 1,
                        "name": "Derek S"
                    },
                    "content": "Comment in channel Backend!"
                },
                {
                    "message_id": 4,
                    "user_id": {
                        "user_id": 2,
                        "name": "Steve K"
                    },
                    "content": "Hi my name is Steve and I'm writing in the Backend channel."
                }
            ]
        }
    ]
}
```

## Create a channel

### POST /api/channels/

> Request:

```
{
	"name": <USER INPUT>
}
```

> Response:

```
{
    "success": true,
    "data": {
        "channel_id": <ID>,
        "name": <USER INPUT FOR NAME>,
        "users": [],
        "messages": []
    }
}
```

## Get Specific Channel

### GET /api/channels/{int:channel_id}/

> Response:

```
{
    "success": true,
    "data": {
        "channel_id": 2,
        "name": "Backend",
        "users": [
            {
                "user_id": 1,
                "name": "Derek S"
            },
            {
                "user_id": 2,
                "name": "Steve K"
            }
        ],
        "messages": [
            {
                "message_id": 3,
                "user_id": {
                    "user_id": 1,
                    "name": "Derek S"
                },
                "content": "Comment in channel Backend!"
            },
            {
                "message_id": 4,
                "user_id": {
                    "user_id": 2,
                    "name": "Steve K"
                },
                "content": "Hi my name is Steve and I'm writing in the Backend channel."
            }
        ]
    }
}
```

## Delete a Channel

### DELETE /api/channels/{int:channel_id}/

> Response:

```
{
    "success": true,
    "data": {
        "channel_id": <ID>,
        "name": <USER INPUT FOR NAME>,
        "users": [],
        "messages": []
    }
}
```



## Add User to a Channel

### POST /api/channels/{int:channel_id}/

> Request:

```
{
	"user_id": <USER INPUT>
}
```

> Response:

```
{
    "success": true,
    "data": {
        "channel_id": 3,
        "name": "New Server Channel",
        "users": [
            {
                "user_id": 4,
                "name": "Grant"
            }
        ],
        "messages": []
    }
}
```

## Add Message to a Channel

### POST /api/channels/{int:channel_id}/message/

> Request:

```
{
	"user_id": <USER INPUT FOR USER ID>,
	"content": <USER INPUT FOR CONTENT>
}
```

> Response:

```
{
    "success": true,
    "data": {
        "message_id": 6,
        "user": {
            "user_id": 3,
            "name": "Julie"
        },
        "channel": {
            "channel_id": 3,
            "name": "Pollo"
        },
        "content": "This is my comment for the Random channel"
    }
}
```
