% Facts
cat(tom).
loves(kunal, pasta).
hair_color(hair, black).
loves(nawaz, games).
lazy(pratyusha).
dances(lili).
searching_for(tom, food).
loves(jack, cricket).
loves(bili, cricket).
free(ryan).
school_closed.

% Relations
happy(lili) :- dances(lili).
hungry(tom) :- searching_for(tom, food).
friends(jack, bili) :- loves(jack, cricket), loves(bili, cricket).
will_go_to_play(ryan) :- free(ryan), school_closed.

% Queries
?- cat(tom).
?- loves(kunal, pasta).
?- happy(lili).
?- will_go_to_play(ryan).
