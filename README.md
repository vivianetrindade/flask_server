# Dibz backend take home

The task is split into 2 parts, one Docker/run configuration part and one API part. The Docker part is optional but if completed it will simplify running and testing your API solution.

## Docker/Run configuration task (Optional)
A Docker file is provided to install all required dependencies to run the application. There is also a shell script provided to build and run the resulting Docker image. When the shell script is used, an interactive bash-shell is opened in the Docker image. 

However, the necessary setup of the SQLite database (handled by the /db/init_db.sh script) is not automatically handled, and instead you will have to manually execute this script, make sure that the `SQL_DB_PATH` environmental variable is correctly set and then start the Flask-app.

If you want to, you can instead change the Dockerfile to automatically initialize the database and directly start the Flask-app when running the resulting image.

## API task
As you can see, the `app/endpoints.py` script currently contains a dummy endpoint that simply says Hi to whoever requests the endpoint. However, we would like to add some endpoint that can return information stored in the SQLite database to the requester.

Your task is to create the endpoints described below. To your help, there is a helper function in `app/utils.py` you can use to open a connection to the database. You can also check the `init_db.sh` script to understand the schema (5 tables: user, queue, city, user_is_in_queue, q_is_in_city).

1. Create a GET-API that returns the first and last names of all users in the database. The endpoint for this API should be `/users`.
2. Create a GET-API that returns all the queues that exist and the cities they are in. The endpoint for this API should be `/queues`.
3. Create a GET-API that returns users that does not have any "active" positions in a queue. The endpoint for this API should be `/admin/inactive`.
4. Create a GET-API that given a users first name (either as a path-param or query-param) returns all the queues that the user is currently active in. The endpoint for this API should be `/user/<name>` or `user?name=<name>`.
5. Create a POST-API that given a new users first name, last name and age inserts this into the database. The endpoint for this API should be `/user`.

## Your solution
Please provide your solution either as a private GitHub repo and invite relevant parties, or as a zip-file. 

Please also provide a maximum 1 page document with a description of your solution, reasoning and potential improvement ideas that you may have.  