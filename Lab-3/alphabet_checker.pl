% Base case: f is a member of a list if it's the first element
is_member(f, [f | _]).
% Recursive case: f is a member of a list if it's in the rest of the list
is_member(f, [_ | Rest]) :- is_member(f, Rest).

% Query
?- is_member(f, [a, b, c, d, e, f, g]).
