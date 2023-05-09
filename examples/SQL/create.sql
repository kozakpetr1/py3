-- -----------------------------------------------------
-- Schema comics - databáze komiksových postav
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `comics` DEFAULT CHARACTER SET utf8 COLLATE utf8_czech_ci;

USE `comics`;

-- -----------------------------------------------------
-- Table `comics`.`studio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `comics`.`studio` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(50) NOT NULL,
    PRIMARY KEY (`id`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `comics`.`charact`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `comics`.`charact` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(40) NOT NULL,
    `weapon` VARCHAR(40) NULL,
    `studio_id` INT NOT NULL,
    INDEX `fk_charact_studio_idx` (`studio_id` ASC),
    PRIMARY KEY (`id`))
ENGINE = InnoDB;

INSERT INTO `comics`.`studio` (`id`, `name`) VALUES
    (NULL, 'DC Comics'),
    (NULL, 'Marvel Studios'),
    (NULL, 'The Walt Disney Studios');
