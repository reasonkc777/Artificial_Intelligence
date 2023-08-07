% Addition
addition_result(Result) :-
    X = 10,
    Y = 5,
    Result is X + Y.

% Subtraction
subtraction_result(Result) :-
    X = 15,
    Y = 7,
    Result is X - Y.

% Multiplication
multiplication_result(Result) :-
    X = 6,
    Y = 4,
    Result is X * Y.

% Division
division_result(Result) :-
    X = 20,
    Y = 4,
    Result is X / Y.

% Power
power_result(Result) :-
    X = 2,
    Y = 3,
    Result is X ** Y.

% Integer Division
integer_division_result(Result) :-
    X = 17,
    Y = 3,
    Result is X // Y.

% Modulus
modulus_result(Result) :-
    X = 23,
    Y = 5,
    Result is X mod Y.

% Queries
?- addition_result(AddResult).
?- subtraction_result(SubResult).
?- multiplication_result(MulResult).
?- division_result(DivResult).
?- power_result(PowerResult).
?- integer_division_result(IntegerDivResult).
?- modulus_result(ModResult).
