-- Departments
INSERT INTO HR_department VALUES (null, 'Department of Casualty Records', '8,000,000,000,000');
INSERT INTO HR_department VALUES (null, 'Department of "Moon" contruction', '500,000,000,000,000');
INSERT INTO HR_department VALUES (null, 'Department of Officer resuscitation', '14');


-- Training
INSERT INTO HR_training (name, start_date, end_date, maxAttendees)
VALUES ("marksmanship", "2/10/2019", "2/14/2019", 11000);
INSERT INTO HR_training (name, start_date, end_date, maxAttendees)
VALUES ("orientation", "2/22/2019", "2/23/2019", 5000);
INSERT INTO HR_training (name, start_date, end_date, maxAttendees)
VALUES ("tarkin talk", "3/1/2019", "3/1/2019", 15000);


-- Employee
insert into HR_employee values (null, "Boba", "Fett", "1977-05-25", 0);
insert into HR_employee values (null, "Darth", "Vader", "1999-05-19", 1);
insert into HR_employee values (null, "The", "Emperor", "1983-05-25", 1);


-- Computer
INSERT INTO HR_computer (purchaseDate, decommissionDate)
VALUES ("1/2/1992", "1/4/1999");
INSERT INTO HR_computer (purchaseDate, decommissionDate)
VALUES ("4/2/2002", "3/24/2019");
INSERT INTO HR_computer (purchaseDate, decommissionDate)
VALUES ("8/11/2012", "5/30/2014");


-- Computer and Employees
INSERT INTO HR_computeremployee VALUES (null, 1, 1);
INSERT INTO HR_computeremployee VALUES (null, 2, 2);
INSERT INTO HR_computeremployee VALUES (null, 3, 3);


-- Employee Training
INSERT INTO HR_employeetraining VALUES (null, 1, 1);
INSERT INTO HR_employeetraining VALUES (null, 2, 1);
INSERT INTO HR_employeetraining VALUES (null, 3, 3);