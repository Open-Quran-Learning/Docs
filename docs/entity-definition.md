# **ENTITY DEFINITION**

| ENTITY | DEFINITION |
| --- | --- |
| USER | A USER is a person who can **only** be a (STUDENT OR STAFF) but can not be both at the same time.A USER is created on creation of an instance in the STUDENT or STAFF entities.A USER is created through signup form and after user verification has been completed.A USER is deleted/updated on USER demand.A USER can be suspended for several reasons.SUPERCLASS/SUBCLASS WITH STUDENT AND STAFF. |
| STUDENT | A STUDENT is a person who can enrolls in PROGRAMs/RECITATIONsA STUDENT is created through signup form and after user verification has been completed. |
| STAFF | A STAFF is a person who is working for the center and has a set of permissions that are granted to him by other STAFF members with MANAGER permissions.A STAFF is created from a form **only** accessible to STAFF members with certain privileges.A STAFF member is given permissions based on his job description which is subject to change.A STAFF account is deleted when the staff quits -- stops working for -- the center. |
| GUARDIAN | A GUARDIAN is a person who is responsible for a STUDENT who is aged under 18 years old.A GUARDIAN is created on registeration of the underaged STUDENT and can also be added/updated/removed through a form accessible by STUDENT. |
| PERMISSION | A PERMISSION is a privilege granted **only** to a STAFF member by another STAFF member with higher PERMISSION.A PERMISSION is created/updated/deleted only by the ADMINISTRATOR. |
| EVENT\_ADDRESS | An EVENT\_ADDRESS is the location where a PROGRAM/RECITATION will take place regardless of the fact of it being online or offline.An EVENT\_ADDRESS is created on creation of a WEB OR PHYSICAL ADDRESS , It can only be one of themAn EVENT\_ADDRESS is created by the privileged STAFF member.SUPERCLASS/SUBCLASS WITH PHYSICAL\_ADDRESS AND WEB\_ADDRESS. |
| PHYSICAL\_ADDRESS | A PHYSICAL\_ADDRESS is the address of the center where the LECTURE or RECITATION will take place. |
| WEB\_ADDRESS | A WEB\_ADDRESS is the url which the STUDENT will get to be able to attend the LECTURE or the RECITATION. |
| APPOINTMENT | An appointment is a time of the day. An appointment also holds the location where the program/recitation will be held. |
| SCHEDULE | A SCHEDULE is one or more appointments for PROGRAMs/RECITATIONs. A SCHEDULE is created/deleted by the privileged STAFF member. Can be online/offline. Can be recurrent.SUPERCLASS/SUBCLASS WITH LECTURE\_SCHEDULE. |
| LECTURE\_SCHEDULE | A LECTURE\_SCHEDULE is one or more appointments for LECTURE.A SCHEDULE is created/deleted by the privileged STAFF member. Can be online/offline. Can be recurrent. |
| PROGRAMS | A PROGRAM is a set of COURSEs and LECTUREs, A PROGRAM is created/updated/deleted through a form **only** accessible by the privileged STAFF members.A PROGRAM can be viewed by the STUDENTs.A PROGRAM can be (online - offline) |
| PROGRAM\_ENROLLMENT | A PROGRAM\_ENROLLMENT is the association between a STUDENT, a PROGRAM, and the state of him being accepted or not.A PROGRAM\_ENROLLMENT is created on STUDENT enrolling in the PROGRAM and the acceptance state is checked when the user passes the EXAM or by the privileged STAFF member. |
| PROGRAM\_SUPERVISION | A PROGRAM\_SUPERVISION is the association between a STAFF and a PROGRAM. |
| LECTURES | A LECTURE is a meeting between a STAFF member ( INSTRUCTOR ) and STUDENTs in a particular SCHEDULE. A LECTURE is created/updated/deleted by a STAFF member (INSTRUCTOR) .A LECTURE could be (online - offline). |
| COURSES | A COURSE is a set of LESSONs. A COURSE is created/updated/deleted through a form by the privileged STAFF members **only**.A COURSE can be viewed **only** by the STUDENTs who enrolled in the PROGRAM. |
| LESSON | A lesson is the study material provided by the privileged STAFF member. A lesson is created/updated/deleted through a form by the privileged STAFF member **only**.A LESSON can be viewed **only** by the STUDENTs who enrolled in the PROGRAM. |
| REQUIREMENT | A requirement is a characteristic that is required from the STUDENT to have to be able to enroll in the PROGRAM like being of a certain age range, gender,etc. It is created on creation of the PROGRAM |
| SKILL | A SKILL is a requirement from the STUDENT to be able to function properly in the PROGRAM and it is created by the privileged STAFF member and assigned to a PROGRAM on PROGRAM creation. |
| PREREQUISITE | A PREREQUISITE is a program that is recommended for the STUDENT to have passed in order to enroll in the PROGRAM he desires.A PREREQUISITE is assigned to a PROGRAM on creation of the PROGRAM and can be updated later by the privileged STAFF member (PROGRAM\_SUPERVISOR). |
| CATEGORY | A CATEGORY is a classification of the PROGRAM . A CATEGORY is created/updated/deleted by the privileged STAFF member (PROGRAM\_SUPERVISOR). |
| FAQs | A FAQ is a frequently asked question about a PROGRAM, a FAQ is created/updated/deleted by the privileged STAFF member through a form along with its answer. |
| EXAM | An EXAM is an evaluation test given by an STAFF member (INSTRUCTOR) to a STUDENT. |
| PROGRAM\_EXAM | A PROGRAM\_EXAM is the evaluation test given by the STAFF member on enrolling in a PROGRAM to validate if the STUDENT is qualified enough to enroll in the PROGRAM. |
| COURSE\_EXAM | A COURSE\_EXAM is the evaluation test given by the STAFF member at the end of each COURSE to make sure the STUDENT is qualified enough to move to the next COURSE. |
| LESSON\_EXAM | A COURSE\_EXAM is the evaluation test given by the STAFF member at the end of each LESSON as a practice for the student . |
| EXAM\_RESULT | AN EXAM\_RESULT is a report that can be viewed by the STUDENT associated with the PROGRAM and the STAFF member associated with the PROGRAM that this EXAM belongs to. |
| RECITATION | A RECITATION is a meeting between a STAFF member ( INSTRUCTOR ) and a STUDENT in a particular SCHEDULE. A RECITATION is created/updated/deleted by an STAFF member (INSTRUCTOR). A RECITATION could be (online - offline). |
| RECITATION\_ENROLLMENT | A RECITATION\_ENROLLMENT is the association between a STUDENT, RECITATION, ASSIGNMENT and the state of the STUDENT being accepted or not.A RECIATION\_ENROLLMENT is created when a STUDENT enrolls in the RECITATION.A RECIATION\_ENROLLMENT is updated when a STUDENT is suspended from the RECITATION.A RECIATION\_ENROLLMENT is deleted when a STUDENT quits the RECITATION. |
| ASSIGNMENT | An ASSIGNMENT is the homework given by the STAFF member to the STUDENT in the RECITATION.An ASSIGNMENT is created when the STAFF member ( INSTRUCTOR ) assigns it to a STUDENT or a group of STUDENTs. |
| RECITATION\_REPORT | AN RECITATION\_REPORT is a report that can be viewed by the STUDENT associated with the RECITATION and the STAFF member associated with the RECITATION that this ASSIGNMENT belongs to. |
