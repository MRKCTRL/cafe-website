from datetime import datetime
from flask import abort
from flask import, make_response

def get_timestamp():
    return datetime.now().strftime(('%Y-%m-%d  %H:%M:%S'))

# GONNA ADD THE JSON FROM THE CAFE API
JSON_FROM_CAFE = {
    "Fairy": {
        "fname": "Tooth",
        "lname": "Fairy",
        "timestamp": get_timestamp(),
    },
    "Ruprecht": {
        "fname": "Knecht",
        "lname": "Ruprecht",
        "timestamp": get_timestamp(),
    },
    "Bunny": {
        "fname": "Easter",
        "lname": "Bunny",
        "timestamp": get_timestamp(),
    }
}

def create_user(person):
    email =person.get('email')
    password = person.get('password', '')

    if email and password not in PEOPLE:
        PEOPLE[password] = {
        'email': email,
        'password': password,
        'timestamp': get_timestamp(),
        }
        return PEOPLE[email], 201
    else:
        abort(
            406,
            f"Person with Last name {email} already exist",
        )


def read_me(password):
    if password in PEOPLE:
        return PEOPLE[password]
    else:
        abort(
            404, f'Incorrect Password, Re-try agaain'
        )

def update(email, password):
    if email in PEOPLE:
        PEOPLE[password]['email'] = person.get('email', PEOPLE[password]['email'])
        PEOPLE[password]['timestamp'] = get_timestamp()
        RETURN people[pasword]
    else:
        abort(
            404,
            f'password doesnt match e-mail'
        )

def delete(password):
    if password in PEOPLE:
        del PEOPLE[password]
        return make_reponse(
            f'{passord} successfuly deleted'
        )
    else:
        abort(
            404,
            f'Person with {password} not found'
        )



def read_all():
    return list(PEOPLE.values())
