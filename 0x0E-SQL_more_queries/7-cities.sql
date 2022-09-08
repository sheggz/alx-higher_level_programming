--a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities`(
    `id` INT NOT NULL,
    `state_id` INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    CONSTRAINT `id` PRIMARY KEY `id`,
    CONSTRAINT `state_id` FOREIGN KEY (`state`)
    REFERENCES `hbtn_0d_usa`.states(`id`)
);