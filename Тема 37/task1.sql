CREATE DATABASE Students;
CREATE TABLE Students_of_VNMU (
    PersonID int,
    FullName varchar(255),
    Course enum(1, 2, 3, 4, 5, 6),
    Faculty varchar(255),
    Stipend bool,
    Year_of_introduction year
    );
INSERT INTO Students_of_VNMU (FullName, Course, Faculty, Stipend, Year_of_introduction)
VALUES ('Kuzniak Vladislav', 5, 1, 2016);
INSERT INTO Students_of_VNMU (FullName, Course, Faculty, Stipend, Year_of_introduction)
VALUES ('Tereshchenko Victoria', 3, 1, 2018);
INSERT INTO Students_of_VNMU (FullName, Course, Faculty, Stipend, Year_of_introduction)
VALUES ('Kuleba Valentin', 5, 0, 2016);
INSERT INTO Students_of_VNMU (FullName, Course, Faculty, Stipend, Year_of_introduction)
VALUES ('Hula Pavlo', 2, 0, 2019);
UPDATE Students_of_VNMU
SET Course=3, Year_of_introduction=2018
WHERE FullName='Hula Pavlo';
UPDATE Students_of_VNMU
SET Stipend=0
WHERE FullName='Tereshchenko Victoria';
DELETE FROM Students_of_VNMU WHERE Course=3;



