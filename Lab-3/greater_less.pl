compare_integers(X, Y) :-
    (   X < Y -> writeln(X is less than Y)
    ;   X > Y -> writeln(X is greater than Y)
    ;   X =:= Y -> writeln(X is equal to Y)
    ).

% Queries
?- compare_integers(5, 10).
?- compare_integers(20, 5).
?- compare_integers(8, 8).
