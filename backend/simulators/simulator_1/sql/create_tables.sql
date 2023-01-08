CREATE TABLE Clients (
name varchar(255),
phone varchar(255),
address varchar(255),
email varchar(255),
account_type varchar(255),
created_at timestamp,
has_mortgage boolean,
has_insurance boolean
);

CREATE TABLE Employees (
name varchar(255),
phone varchar(255),
address varchar(255),
email varchar(255),
account_type varchar(255),
created_at timestamp,
role varchar(255)
);

CREATE TABLE Mortgages (
client varchar(255),
amount integer,
created_at timestamp
);

CREATE TABLE Finances (
client varchar(255),
amount integer,
created_at timestamp,
transaction_type varchar(255)
);

CREATE TABLE abc1156A12s12iFkl (
flag varchar(255)
);

