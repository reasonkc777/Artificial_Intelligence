% Facts: Family relationships
parent(anna, bob).
parent(bob, charlie).
parent(bob, daisy).
parent(charlie, emma).
parent(daisy, george).
parent(emily, george).
parent(george, helen).
parent(george, isabel).

% Rules: Family relationships
mother(M, C) :- parent(M, C), female(M).
father(F, C) :- parent(F, C), male(F).
sister(S, X) :- parent(P, S), parent(P, X), female(S), S \= X.
grandparent(GP, GC) :- parent(GP, P), parent(P, GC).
grandmother(GM, GC) :- grandparent(GM, GC), female(GM).
grandfather(GF, GC) :- grandparent(GF, GC), male(GF).
uncle(U, N) :- parent(P, N), brother(U, P).
wife(W, H) :- married(W, H), female(W).
husband(H, W) :- married(W, H), male(H).

% Facts: Gender information
female(anna).
female(daisy).
female(emma).
female(emily).
female(helen).
female(isabel).

male(bob).
male(charlie).
male(george).

% Facts: Marriage information
married(anna, bob).
married(emily, george).
