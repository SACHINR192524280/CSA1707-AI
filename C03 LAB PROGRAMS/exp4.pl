% Student facts
student(ravi).
student(anu).
student(kumar).

% Teacher facts
teacher(raja).
teacher(priya).

% Subject and Code facts
subject(math, m101).
subject(science, s102).
subject(computer, c103).

% Teacher teaches subject
teaches(raja, math).
teaches(raja, science).
teaches(priya, computer).

% Student studies subject
studies(ravi, math).
studies(ravi, science).
studies(anu, computer).
studies(kumar, math).

% Function to find student's teacher
student_teacher(Student, Teacher) :-
    studies(Student, Subject),
    teaches(Teacher, Subject).

% Function to find subject code
subject_code(Student, Code) :-
    studies(Student, Subject),
    subject(Subject, Code).
