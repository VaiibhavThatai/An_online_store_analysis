DROP SCHEMA IF EXISTS ur_store;
GO
CREATE SCHEMA ur_store;
GO
DROP TABLE IF EXISTS ur_store.customers;

CREATE TABLE store.customers (
    cust_id INTEGER,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    state_code VARCHAR(2),
    datetime_created VARCHAR(100),
    datetime_updated VARCHAR(100),
    datetime_inserted TIMESTAMP not null default CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS store.customer_risk_score;
CREATE TABLE store.customer_risk_score(
    customer_id INTEGER,
    risk_score INTEGER,
    datetime_inserted TIMESTAMP not null default CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS store.orders;
CREATE TABLE store.orders(
    order_id VARCHAR(50), 
    customer_id INTEGER,
    item_id VARCHAR(50), 
    item_name VARCHAR(150), 
    delivered_on VARCHAR(50)
);

DROP TABLE IF EXISTS store.states ;
CREATE TABLE store.states  (
    state_identifier INTEGER,
    state_code VARCHAR(2),
    st_name VARCHAR(30)
);

INSERT INTO store.states(state_identifier, state_CODE, st_name)
VALUES

/*  "AN", "AP", "AR", "AS", "BR", "CH", "CT",
    "DN", "DD", "DL", "GA", "GJ", "HR", "HP",
    "JK", "JH", "KA", "KL", "LD", "MP", "MH",
    "MN", "ML", "MZ", "NL", "OR", "PY", "PB",
    "RJ", "SK", "TN", "TG", "TR", "UP", "UT",
    "WB"
*/
(1, 'AN', 'ANDAMAN AND NICOBAR'),
(2, 'AP', 'ANDHRA PRADESH'),
(3, 'AR', 'ARUNACHAL PRADESH'),
(4, 'AS', 'ASSAM'),
(5, 'BR', 'BIHAR'),
(6, 'CH', 'CHANDIGARH'),
(7, 'CT', 'CHHATISGARH'),
(8, 'DN',  'DADRA AND NAGAR HAVELI'),
(9, 'DD',  'DAMAN AND DIU'),
(10, 'DL', 'DELHI'),
(11, 'GA', 'GOA'),
(12, 'GJ', 'GUJARAT'),
(13, 'HR', 'HARYANA'),
(14, 'HP', 'HIMACHAL PRADESH'),
(15, 'JK', 'JAMMU AND KASHMIR'),
(16, 'JH', 'JHARKHAND'),
(17, 'KA', 'KARNATAKA'),
(18, 'KL', 'KERALA'),
(19, 'LD', 'LAKSHWADEEP'),
(20, 'MP', 'MADHYA PRADESH'),
(21, 'MH', 'MAHARASHTRA'),
(22, 'MZ', 'MIZORAM'),
(23, 'NL', 'NAGALAND'),
(24, 'OR', 'ODISHA'),
(25, 'PY', 'PUDUCHERRY'),
(26, 'PB', 'PUNJAB'),
(27, 'RJ', 'RAJASTHAN'),
(28, 'SK', 'SIKKIM'),
(29, 'TN', 'TAMIL NADU'),
(30, 'TG', 'TELANGANA'),
(31, 'TR', 'TRIPURA'),
(32, 'UP', 'UTTAR PRADESH'),
(33, 'UT', 'UTTARAKHAND'),
(34, 'WB', 'WEST BENGAL'),
(35, 'ML', 'MEGHALAYA'),
(36, 'MN', 'MANIPUR')




/*  "AN", "AP", "AR", "AS", "BR", "CH", "CT",
    "DN", "DD", "DL", "GA", "GJ", "HR", "HP",
    "JK", "JH", "KA", "KL", "LD", "MP", "MH",
    "MN", "ML", "MZ", "NL", "OR", "PY", "PB",
    "RJ", "SK", "TN", "TG", "TR", "UP", "UT",
    "WB"
*/