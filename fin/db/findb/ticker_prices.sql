CREATE TABLE `index_price_daily` (
  `Date` date DEFAULT NULL,
  `ticker` varchar(20) DEFAULT NULL,
  `open` float DEFAULT NULL,
  `high` float DEFAULT NULL,
  `low` float DEFAULT NULL,
  `close` float DEFAULT NULL,
  `adj_close` float DEFAULT NULL,
  `volume` float DEFAULT NULL,
  UNIQUE KEY(Date, ticker) 
) ENGINE=InnoDB
