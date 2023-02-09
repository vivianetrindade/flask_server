import logging
import json

import flask
from flask import Response

from app.utils import get_db

app = flask.Flask("dibz_api")
logger = flask.logging.create_logger(app)
logger.setLevel(logging.INFO)


@app.route("/users", methods=["GET"])
def get_users():
    """
    Endpoint to get all users
    """
    users = get_db().execute("SELECT f_name, l_name FROM user").fetchall()
    users = [dict(zip(["first_name", "last_name"], user)) for user in users]
    
    return Response(json.dumps(users), status=200, content_type='application/json')
    
#Create a GET-API that returns all the queues that exist and the cities they are in. The endpoint for this API should be /queues.
@app.route("/queues", methods=["GET"])
def get_queues():
    """
    Endpoint to get all queues
    """
    queues = get_db().execute("""SELECT queue.q_name, city.city_name 
                            FROM q_is_in_city 
                            LEFT JOIN queue ON q_is_in_city.qid = queue.qid 
                            LEFT JOIN city ON q_is_in_city.cid = city.cid""").fetchall()
    queues = [dict(zip(["queue_id", "city"], queue)) for queue in queues]
    
    return Response(json.dumps(queues), status=200, content_type='application/json')

#Create a GET-API that returns users that does not have any "active" positions in a queue. The endpoint for this API should be /admin/inactive
@app.route("/admin/inactive", methods=["GET"])
def get_inactive_users():
    """
    Endpoint to get all inactive users
    """
    inactive_users = get_db().execute("""SELECT city.city_name, user.f_name|| ' ' || user.l_name AS name 
                                    FROM user 
                                    LEFT JOIN user_is_in_queue ON user.uid = user_is_in_queue.uid 
                                    LEFT JOIN q_is_in_city ON user_is_in_queue.qid = q_is_in_city.qid
                                    LEFT JOIN city ON q_is_in_city.cid = city.cid
                                     WHERE user_is_in_queue.is_active = 0""").fetchall()
    inactive_users = [dict(zip(["city_name", "name"], inactive_user)) for inactive_user in inactive_users]
    
    return Response(json.dumps(inactive_users), status=200, content_type='application/json')

#Create a GET-API that given a users first name (either as a path-param or query-param) returns all the queues that the user is currently active in. The endpoint for this API should be /user/<name> or user?name=<name>
@app.route("/user/<name>", methods=["GET"])
def get_user_queues(name):
    """
    Endpoint to get all queues for a specific user
    """
    user_queues = get_db().execute("""SELECT queue.q_name, city.city_name 
                                    FROM user 
                                    LEFT JOIN user_is_in_queue ON user.uid = user_is_in_queue.uid 
                                    LEFT JOIN queue ON user_is_in_queue.qid = queue.qid 
                                    LEFT JOIN q_is_in_city ON queue.qid = q_is_in_city.qid 
                                    LEFT JOIN city ON q_is_in_city.cid = city.cid 
                                    WHERE user.f_name = ? AND user_is_in_queue.is_active = 1""", (name,)).fetchall()
    user_queues = [dict(zip(["queue_name", "city"], user_queue)) for user_queue in user_queues]
    
    return Response(json.dumps(user_queues), status=200, content_type='application/json')

#Create a POST-API that given a new users first name, last name and age inserts this into the database. The endpoint for this API should be /user.
@app.route("/user", methods=["POST"])
def create_user():
    """
    Endpoint to create a new user
    """
    data = flask.request.json
    f_name = data.get("f_name")
    l_name = data.get("l_name")
    age = data.get("age")
    #check if user already exists
    user_exists = get_db().execute("SELECT * FROM user WHERE f_name = ? AND l_name = ? AND age = ?", (f_name, l_name, age)).fetchone()
    if user_exists:
        return Response(status=409)
    get_db().execute("INSERT INTO user (f_name, l_name, age) VALUES (?, ?, ?)", (f_name, l_name, age))
    get_db().commit()
    
    return Response(status=201)