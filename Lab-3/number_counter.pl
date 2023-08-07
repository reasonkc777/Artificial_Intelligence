count_from_to(From, To) :-
    From =< To,
    writeln(From),
    Next is From + 1,
    count_from_to(Next, To).

count_from_to(_, _).

% Query to count from 10 to 15
?- count_from_to(10, 15).
