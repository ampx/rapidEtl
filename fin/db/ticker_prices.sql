CREATE TABLE findb.index_price_daily(
   dt date NOT NULL,
   idx varchar(255) NOT NULL,
   open float NOT NULL,
   high float NOT NULL,
   low float NOT NULL,
   close float NOT NULL,
   adj_close float NOT NULL,
   volume float NOT NULL,
   UNIQUE KEY(dt, idx) 
)ENGINE=INNODB;
