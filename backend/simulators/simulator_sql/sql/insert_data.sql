INSERT INTO Clients (name, phone, address, email, account_type, created_at, has_mortgage, has_insurance)
VALUES
('John Smith', '123-456-7890', '123 Main St', 'johnsmith@email.com', 'savings', '2020-01-01', TRUE, FALSE),
('Jane Doe', '123-456-7891', '456 Main St', 'janedoe@email.com', 'checking', '2020-02-01', TRUE, TRUE),
('Bob Johnson', '123-456-7892', '789 Main St', 'bobjohnson@email.com', 'savings', '2020-03-01', FALSE, TRUE),
('Sally Smith', '123-456-7893', '321 Main St', 'sallysmith@email.com', 'checking', '2020-04-01', FALSE, FALSE),
('Mike Jones', '123-456-7894', '654 Main St', 'mikejones@email.com', 'savings', '2020-05-01', TRUE, TRUE),
('Lisa Williams', '123-456-7895', '987 Main St', 'lisawilliams@email.com', 'checking', '2020-06-01', FALSE, TRUE),
('Chris Brown', '123-456-7896', '246 Main St', 'chrisbrown@email.com', 'savings', '2020-07-01', TRUE, TRUE),
('Sarah Johnson', '123-456-7897', '369 Main St', 'sarahjohnson@email.com', 'checking', '2020-08-01', FALSE, FALSE),
('Tom Smith', '123-456-7898', '159 Main St', 'tomsmith@email.com', 'savings', '2020-09-01', TRUE, TRUE),
('Kate Williams', '123-456-7899', '753 Main St', 'katewilliams@email.com', 'checking', '2020-10-01', TRUE, TRUE),
('Mark Jones', '123-456-7900', '147 Main St', 'markjones@email.com', 'savings', '2020-11-01', FALSE, TRUE);

INSERT INTO Employees (name, phone, address, email, account_type, created_at, role)
VALUES
('John Smith', '123-456-7890', '123 Main St', 'johnsmith@email.com', 'manager', '2020-01-01', 'manager'),
('Jane Doe', '123-456-7891', '456 Main St', 'janedoe@email.com', 'assistant manager', '2020-02-01', 'assistant manager'),
('Bob Johnson', '123-456-7892', '789 Main St', 'bobjohnson@email.com', 'teller', '2020-03-01', 'teller'),
('Sally Smith', '123-456-7893', '321 Main St', 'sallysmith@email.com', 'assistant teller', '2020-04-01', 'assistant teller'),
('Mike Jones', '123-456-7894', '654 Main St', 'mikejones@email.com', 'loan officer', '2020-05-01', 'loan officer'),
('Lisa Williams', '123-456-7895', '987 Main St', 'lisawilliams@email.com', 'assistant loan officer', '2020-06-01', 'assistant loan officer'),
('Chris Brown', '123-456-7896', '246 Main St', 'chrisbrown@email.com', 'customer service representative', '2020-07-01', 'customer service representative'),
('Sarah Johnson', '123-456-7897', '369 Main St', 'sarahjohnson@email.com', 'IT specialist', '2020-08-01', 'IT specialist'),
('Tom Smith', '123-456-7898', '159 Main St', 'tomsmith@email.com', 'human resources manager', '2020-09-01', 'human resources manager'),
('Kate Williams', '123-456-7899', '753 Main St', 'katewilliams@email.com', 'marketing specialist', '2020-10-01', 'marketing specialist'),
('Mark Jones', '123-456-7900', '147 Main St', 'markjones@email.com', 'accountant', '2020-11-01', 'accountant'),
('Susan Brown', '123-456-7901', '753 Main St', 'susanbrown@email.com', 'financial advisor', '2020-12-01', 'financial advisor'),
('James Smith', '123-456-7902', '369 Main St', 'jamessmith@email.com', 'sales representative', '2021-01-01', 'sales representative'),
('Emily Williams', '123-456-7903', '246 Main St', 'emilywilliams@email.com', 'legal advisor', '2021-02-01', 'legal advisor'),
('David Jones', '123-456-7904', '987 Main St', 'davidjones@email.com', 'security officer', '2021-03-01', 'security officer'),
('Jessica Brown', '123-456-7905', '321 Main St', 'jessicabrown@email.com', 'receptionist', '2021-04-01', 'receptionist');

INSERT INTO Finances (client, amount, created_at, transaction_type)
VALUES
('John Smith', 1000, '2020-01-01', 'deposit'),
('Jane Doe', 2000, '2020-02-01', 'withdrawal'),
('Bob Johnson', 3000, '2020-03-01', 'deposit'),
('Sally Smith', 4000, '2020-04-01', 'withdrawal'),
('Mike Jones', 5000, '2020-05-01', 'deposit'),
('Lisa Williams', 6000, '2020-06-01', 'withdrawal'),
('Chris Brown', 7000, '2020-07-01', 'deposit'),
('Sarah Johnson', 8000, '2020-08-01', 'withdrawal'),
('Tom Smith', 9000, '2020-09-01', 'deposit'),
('Kate Williams', 10000, '2020-10-01', 'withdrawal');

INSERT INTO Mortgages (client, amount, created_at)
VALUES
('John Smith', 100000, '2020-01-01'),
('Jane Doe', 200000, '2020-02-01'),
('Bob Johnson', 300000, '2020-03-01'),
('Sally Smith', 400000, '2020-04-01'),
('Mike Jones', 500000, '2020-05-01'),
('Lisa Williams', 600000, '2020-06-01'),
('Chris Brown', 700000, '2020-07-01'),
('Sarah Johnson', 800000, '2020-08-01'),
('Tom Smith', 900000, '2020-09-01'),
('Kate Williams', 1000000, '2020-10-01');

INSERT INTO abc1156A12s12iFkl (flag)
VALUES
('CTF_BANK_FOUND');