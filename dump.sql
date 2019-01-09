PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE action_tbl (
	idx BIGINT NOT NULL, 
	aciton_name VARCHAR(40), 
	txn_id VARCHAR(64), 
	authorization VARCHAR(40), 
	contract VARCHAR(12), 
	PRIMARY KEY (idx), 
	UNIQUE (txn_id)
);
CREATE TABLE producer_tbl (
	idx INTEGER NOT NULL, 
	name VARCHAR(30) NOT NULL, 
	email VARCHAR(120) NOT NULL, 
	article TEXT NOT NULL, 
	accnt_name VARCHAR(13) NOT NULL, 
	slogan VARCHAR(60), 
	location VARCHAR(60), 
	homepage VARCHAR(60), 
	maps_lat VARCHAR(20), 
	maps_lng VARCHAR(20), 
	PRIMARY KEY (idx), 
	UNIQUE (name)
);
CREATE TABLE account_tbl (
	idx BIGINT NOT NULL, 
	account_name VARCHAR(40), 
	created VARCHAR(40), 
	block_num BIGINT, 
	PRIMARY KEY (idx)
);
COMMIT;
