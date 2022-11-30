parent(dipok, deb).
parent(dipok, sruti).
parent(dipok, jeet).
parent(dipok, swarup).

male(deb).
male(jeet).
male(swarup).
female(sruti).
parent(shekhor, debo).
brother(shekhor,samir).
sister(shekhor,uma).
uncle(X,Y) :- parent(Z,X), brother(Z,Y).
aunt(X,Y) :- parent(Z,X), sister(Z,Y).

brother(X,Y) :- parent(Z,X), parent(Z,Y), male(Y),X\== Y.
sister(X,Y) :- parent(Z,X), parent(Z,Y),female(Y), X\== Y.


findbrother :- write(' Name: '), read(X), write('BrotherName: '),brother(X, Gc), write(Gc), tab(5), fail.
findbrother.

findsister :- write(' Name: '), read(X), write('SisterName: '),sister(X, Gc), write(Gc), tab(5), fail.
findsister.


finduncle :- write(' Name :'), read(X), write('Uncle Name : '), uncle(X, Uc), write(Uc), tab(5), fail.
finduncle.

findaunt :- write(' Name :'), read(X), write('Aunt Name : '), aunt(X, Au), write(Au), tab(5), fail.
findaunt.
