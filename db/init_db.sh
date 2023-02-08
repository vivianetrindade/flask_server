#!/bin/sh
sqlite3 dibz.db <<EOF
create table user (uid INTEGER PRIMARY KEY,f_name TEXT, l_name TEXT, age INTEGER);
create table queue (qid INTEGER PRIMARY KEY, q_name TEXT, is_pay_queue INTEGER);
create table city (cid INTEGER PRIMARY KEY, city_name TEXT);
create table user_is_in_queue (uid INTEGER, qid INTEGER, is_active INTEGER,
FOREIGN KEY(uid) REFERENCES user(uid), FOREIGN KEY(qid) REFERENCES queue(qid));
create table q_is_in_city (qid INTEGER, cid INTEGER, FOREIGN KEY(qid) REFERENCES queue(qid),
FOREIGN KEY(cid) REFERENCES city(cid));
BEGIN TRANSACTION;
INSERT INTO user (f_name,l_name,age) VALUES ('Alice','Andersson', 22);
INSERT INTO user (f_name,l_name,age) VALUES ('Bob','Balleryd', 17);
INSERT INTO user (f_name,l_name,age) VALUES ('Charlie','Cederlund', 65);
INSERT INTO queue (q_name, is_pay_queue) VALUES ('Q1', 0);
INSERT INTO queue (q_name, is_pay_queue) VALUES ('Q2', 0);
INSERT INTO queue (q_name, is_pay_queue) VALUES ('Q3', 1);
INSERT INTO city (city_name) VALUES ('Stockholm');
INSERT INTO city (city_name) VALUES ('Gothenburg');
INSERT INTO city (city_name) VALUES ('Malmoe');
INSERT INTO q_is_in_city (qid, cid) VALUES (1,1);
INSERT INTO q_is_in_city (qid, cid) VALUES (1,2);
INSERT INTO q_is_in_city (qid, cid) VALUES (2,1);
INSERT INTO q_is_in_city (qid, cid) VALUES (2,3);
INSERT INTO q_is_in_city (qid, cid) VALUES (3,1);
INSERT INTO user_is_in_queue (uid, qid, is_active) VALUES (1,1,1);
INSERT INTO user_is_in_queue (uid, qid, is_active) VALUES (1,2,1);
INSERT INTO user_is_in_queue (uid, qid, is_active) VALUES (1,3,0);
INSERT INTO user_is_in_queue (uid, qid, is_active) VALUES (2,1,1);
INSERT INTO user_is_in_queue (uid, qid, is_active) VALUES (2,2,1);
INSERT INTO user_is_in_queue (uid, qid, is_active) VALUES (2,3,1);
INSERT INTO user_is_in_queue (uid, qid, is_active) VALUES (3,1,0);
INSERT INTO user_is_in_queue (uid, qid, is_active) VALUES (3,3,0);
COMMIT;
EOF