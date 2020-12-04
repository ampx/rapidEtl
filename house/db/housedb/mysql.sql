CREATE TABLE rooms (
	roomId tinyint not null,
	name VARCHAR(100) not null,
	PRIMARY KEY (roomId)
)ENGINE=InnoDB;

insert into rooms values(1, "Master Bedroom");
insert into rooms values(2, "Radiks Room");
insert into rooms values(3, "Office");
insert into rooms values(4, "Kids Room");
insert into rooms values(5, "Hallway");
insert into rooms values(6, "Kitchen");
insert into rooms values(7, "Living Room");
insert into rooms values(8, "Formal Living Room");
insert into rooms values(9, "Laundry Room");
insert into rooms values(10, "Garage");
insert into rooms values(11, "Front Outdoor");
insert into rooms values(12, "Side Gate");
insert into rooms values(13, "Side House");
insert into rooms values(14, "Backyard");




CREATE TABLE ac (
	roomId tinyint not null,
	ac_name VARCHAR(100) not null,
	srp_name VARCHAR(100) not null,
	PRIMARY KEY (roomId)
)ENGINE=InnoDB;

insert into ac values(1, "Goodman", "Hallway Thermostat");
insert into ac values(2, "Goodman", "Hallway Thermostat");
insert into ac values(3, "Goodman", "Hallway Thermostat");
insert into ac values(4, "Goodman", "Hallway Thermostat");
insert into ac values(5, "Goodman", "Hallway Thermostat");
insert into ac values(6, "Goettl", "Main Thermostat");
insert into ac values(7, "Goettl", "Main Thermostat");
insert into ac values(8, "Goettl", "Main Thermostat");
insert into ac values(9, "Goettl", "Main Thermostat");
insert into ac values(10, "Goettl", "Main Thermostat");
insert into ac values(15, "Goodman", "Hallway Thermostat");
insert into ac values(16, "Goodman", "Hallway Thermostat");
insert into ac values(17, "Goettl", "Main Thermostat");


CREATE TABLE srp_pwr (
	measured_time datetime not null,
	hallway_thermostat float,
	water_heater float,
	main_thermostat float,
	dryer float,
	total float,
	PRIMARY KEY (measured_time)
)ENGINE=InnoDB;


CREATE TABLE device_list (
	deviceId int not null,
	displayName VARCHAR(250) not null,
	PRIMARY KEY (deviceId)
)ENGINE=InnoDB;

CREATE TABLE device_room (
	deviceId int not null,
	roomId tinyint not null,
	PRIMARY KEY (deviceId)
)ENGINE=InnoDB;


DELIMITER $$

CREATE TRIGGER update_deviceName_trig
AFTER INSERT
ON events FOR EACH ROW
BEGIN
    IF (NEW.deviceId is not NULL and NEW.deviceId!="" and NEW.displayName is not null and NEW.displayName!="") THEN
        replace into device_list (deviceId, displayName) values (new.deviceId, new.displayName);
    END IF;
END$$

DELIMITER ;




select q1.measured_time as time,
greatest(0, q1.dryer-q2.dryer) as dryer,
greatest(0, q1.hallway_thermostat-q2.hallway_thermostat) as hallway_thermostat,
greatest(0, q1.main_thermostat-q2.main_thermostat) as main_thermostat,
greatest(0, q1.water_heater-q2.water_heater) as water_heater
from
(select * from srp_pwr where measured_time between $__timeFrom() and $__timeTo()) as q1
left join 
(select * from srp_pwr where measured_time between $__timeFrom() and $__timeTo()) as q2
on q1.measured_time=DATE_ADD(q2.measured_time, INTERVAL 1 MINUTE)

SELECT
  $__timeGroupAlias(measured_time,$__interval),
  (dryer + hallway_thermostat + main_thermostat + water_heater) as total_accum_pwr
FROM srp_pwr
WHERE
  $__timeFilter(measured_time)
GROUP BY 1
ORDER BY $__timeGroup(measured_time,$__interval)
