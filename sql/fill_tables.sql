-- Set params
set session my.number_of_sales = '100';
set session my.number_of_users = '100';
set session my.number_of_products = '100';
set session my.number_of_stores = '100';
set session my.number_of_coutries = '100';
set session my.number_of_cities = '30';
set session my.status_names = '5';
set session my.start_date = '2019-01-01 00:00:00';
set session my.end_date = '2020-02-01 00:00:00';

-- load the pgcrypto extension to gen_random_uuid ()
CREATE EXTENSION pgcrypto;

-- Filling of products
INSERT INTO product
select id, concat('Product ', id) 
FROM GENERATE_SERIES(1, current_setting('my.number_of_products')::int) as id;

-- Filling of countries
INSERT INTO country
select id, concat('Country ', id) 
FROM GENERATE_SERIES(1, current_setting('my.number_of_coutries')::int) as id;

-- Filling of cities
INSERT INTO city
select id
	, concat('City ', id)
	, floor(random() * (current_setting('my.number_of_coutries')::int) + 1)::int
FROM GENERATE_SERIES(1, current_setting('my.number_of_cities')::int) as id;

-- Filling of stores
INSERT INTO store
select id
	, concat('Store ', id)
	, floor(random() * (current_setting('my.number_of_cities')::int) + 1)::int
FROM GENERATE_SERIES(1, current_setting('my.number_of_stores')::int) as id;

-- Filling of users
INSERT INTO users
select id
	, concat('User ', id)
FROM GENERATE_SERIES(1, current_setting('my.number_of_users')::int) as id;

-- Filling of users
INSERT INTO status_name
select status_name_id
	, concat('Status Name ', status_name_id)
FROM GENERATE_SERIES(1, current_setting('my.status_names')::int) as status_name_id;

-- Filling of sales  
INSERT INTO sale
select gen_random_uuid ()
	, round(CAST(float8 (random() * 10000) as numeric), 3)
	, TO_TIMESTAMP(start_date, 'YYYY-MM-DD HH24:MI:SS') +
		random()* (TO_TIMESTAMP(end_date, 'YYYY-MM-DD HH24:MI:SS') 
							- TO_TIMESTAMP(start_date, 'YYYY-MM-DD HH24:MI:SS'))
	, floor(random() * (current_setting('my.number_of_products')::int) + 1)::int
	, floor(random() * (current_setting('my.number_of_users')::int) + 1)::int
	, floor(random() * (current_setting('my.number_of_stores')::int) + 1)::int
FROM GENERATE_SERIES(1, current_setting('my.number_of_sales')::int) as id
	, current_setting('my.start_date') as start_date
	, current_setting('my.end_date') as end_date;

-- Filling of order_status  
INSERT INTO order_status
select gen_random_uuid ()
	, date_sale + random()* (date_sale + '5 days' - date_sale)
	, sale_id
	, floor(random() * (current_setting('my.status_names')::int) + 1)::int
from sale;


-- INSERT INTO employees (name,phone,email,address,postalZip,region,country,iban,pan,pin,cvv)
-- VALUES
--   ('Michael Nolan','(646) 954-7123','elementum.sem.vitae@yahoo.ca','P.O. Box 197, 4421 Ultricies Road','577796','Vorarlberg','Austria','SM2127215728847524391737683','3732 523234 82397',4634,'637'),
--   ('Robin Burke','(565) 623-0178','nec.luctus.felis@yahoo.ca','P.O. Box 830, 523 Imperdiet Rd.','57-77','Maharastra','Singapore','ES2955773256519853818045','402681 398525 8686',4142,'246'),
--   ('Grace Burnett','1-867-577-2755','donec@outlook.edu','P.O. Box 849, 5302 A, Avenue','556373','Rajasthan','South Korea','NL87ESOX8275472613','676112744656468756',8495,'839'),
--   ('Drew Buchanan','1-315-462-0441','donec.felis@yahoo.couk','Ap #419-7291 Laoreet Road','74430','North Chungcheong','Australia','GR5837815015945175422542284','3035 828876 44379',6197,'147'),
--   ('Austin Figueroa','1-835-916-3953','egestas.rhoncus@hotmail.edu','Ap #604-4868 Urna. Av.','737233','Eastern Cape','Ukraine','ME03546033022636962341','633 47363 87564 657',3517,'846'),
--   ('Sage Henson','1-836-318-8036','suspendisse.ac.metus@hotmail.couk','Ap #524-4160 Lorem Street','9675','Campania','Colombia','KW2944529887713608797727205222','4532165588544',9105,'566'),
--   ('Macon Vaughan','1-638-152-5148','malesuada.vel.convallis@hotmail.ca','Ap #631-7752 Odio Rd.','833254','Uttarakhand','Philippines','CZ4657184582900742507064','6468822367385442',9000,'251'),
--   ('Mari Paul','1-665-561-7377','erat@protonmail.com','4083 Aliquet. St.','4412-2287','Troms og Finnmark','Canada','PK3009619865592329669916','503857294882',1940,'769'),
--   ('Alma Stevens','1-214-423-1474','est.tempor.bibendum@outlook.org','Ap #227-290 Sociis Rd.','23333-43458','Maule','Vietnam','DE45453016935522561717','557627 323225 2749',5929,'715'),
--   ('Addison Whitaker','1-879-337-9721','felis.adipiscing@icloud.net','853-9546 Magna. St.','3264','Coahuila','France','TN2368311735067625575374','633 43893 16268 642',3649,'301'),
--   ('Quon Camacho','(476) 584-4724','rutrum.fusce@protonmail.edu','9234 Tempus Rd.','55511','East Region','Australia','KZ844301147661787464','6771643757929579',7698,'931'),
--   ('Joshua Hess','1-588-788-1581','interdum.sed@google.org','655-5502 Sollicitudin St.','10-282','Berkshire','India','CY04236815238376417855872149','527 41956 34923 699',6055,'919'),
--   ('Brenden Whitfield','(118) 869-6162','tempus.mauris.erat@outlook.edu','466-2336 Metus Rd.','72543','Cartago','South Africa','SK9261353301923310641511','373447795459564',6385,'556'),
--   ('Armand Wheeler','(553) 751-3492','quam.dignissim@google.net','9440 Aliquam Rd.','2396','Western Australia','Italy','LB62911239447372577627878754','3674 697952 33680',2767,'738'),
--   ('Lucius Smith','(986) 441-7363','euismod.ac.fermentum@aol.edu','878-4842 Enim. Street','24-335','Gyeonggi','Philippines','HU03317899139172812532857205','4911365535274745',7584,'822'),
--   ('Igor Sellers','1-657-555-9752','nulla.integer.vulputate@yahoo.couk','Ap #215-2487 Curabitur Avenue','49R 8W2','Zamboanga Peninsula','China','FR2681685388884888275656565','2149 627672 58432',5846,'912'),
--   ('Mariko Gaines','1-155-723-8255','quisque.ornare.tortor@hotmail.org','Ap #814-2334 Dolor Road','3381','Luik','India','RO81RGJY9954212766796281','655243 752947 1233',5814,'539'),
--   ('Fitzgerald Craig','1-267-326-8274','nulla.eget@yahoo.ca','P.O. Box 790, 1071 Sed Rd.','40538','Ceará','France','MD7469264242580270136139','6767429452857422',7628,'460'),
--   ('Charles Roach','1-142-541-5526','pede.ultrices.a@outlook.couk','4884 Eros Road','3580','Carinthia','Indonesia','DE47024453451982044416','6759 792722 8146',8492,'678'),
--   ('Cadman Neal','1-852-145-0678','congue.elit@protonmail.couk','4344 Magnis Av.','62479','Nova Scotia','Indonesia','RS84204841642976976894','2014 677816 45627',8773,'546');