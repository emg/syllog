﻿var prolog = new PrologPlusCG.PPCGJS("#console");

var program = `
//
// Copyright (c) 2010-2021 Peter Oehrstroem and Ulrik Sandborg-Petersen
//
// License terms: MIT License.
// See LICENSE in the Syllog distribution.
//

// Configure the web server URL
// 
// Put your own URL here.
web_server_url(_url) :- concat("https:/", "/logic.aau.dk/syllog", _url).



term(1, males).
term(2, females).
term(3, adults).
term(4, mothers).
term(5, fathers).
term(6, parents).
term(7, students).
term(8, teachers).
term(9, doctors).

reset :- retract(reaction(_)), fail.
reset.

propkind(verbal).

update_propkind(_propkind) :- retract(propkind(_)), fail.
update_propkind(_propkind) :- assertz(propkind(_propkind), ()).

correct_answers(0).
answer_given(1).

reset_answer_given:- retract(answer_given(_)), fail.
reset_answer_given:- assertz(answer_given(0), ()).

update_answer_given1:- 
	retract(answer_given(0)), assertz(answer_given(1), ()).

update_answer_given:- 
	retract(answer_given(0)), assertz(answer_given(1), ()), correct_answers(X), 
	nl, write("THE NUMBER OF CORRECT ANSWERS IN A ROW: "), write(X),nl .

addto_correct_answers:- correct_answers(M),  val(M1,add(M,1)), 
		retract(correct_answers(M)), assertz(correct_answers(M1), ()).
reset_correct_answers:- correct_answers(M),
		retract(correct_answers(M)), assertz(correct_answers(0), ()).

clearscreen :- clearConsole, reset.

repeat.
repeat :- repeat.

validity_check(0,0).
validity_check(1,1).
validity_check(2,2).

find_syll(_V, _S, _M, _P, _F, _Q1, _Q2, _Q3, _U1, _U2, _U3) :- 
	repeat, choose_syl_numbers(_F, _N1, _N2, _N3), 
	quan(_N1, _Q1), quan(_N2, _Q2), quan(_N3, _Q3), 
	pos_syll(_S, _M, _P, _F, _Q1, _Q2, _Q3, _U1, _U2, _U3), 
	syl_validity(_V1, _U1, _U2, _U3), validity_check(_V1, _V), /.

write_syllogism :- write_syllogism_with_propkind(verbal) .

write_syllogism_with_propkind(_propkind) :- 
       	update_propkind(_propkind),
	answer_given(1), correct_answers(X), 
	generate_uid_if_not_there_already,
	clearConsole, reset, 
	rnd(1, 4, S), term(S, _S), rnd(4, 7, P), term(P, _P), 
	rnd(7, 10, M), term(M, _M), rnd(1, 3, _V), /, 		
	find_syll(_V, _S, _M, _P, _F, _Q1, _Q2, _Q3, _U1, _U2, _U3), 
	reset_answer_given, find_reaction(_U1, _U2, _U3, R), 
	writepropositionx(_propkind, _U1), nl, 
	writepropositionx(_propkind, _U2), nl, 
	write("Ergo: "), 
	writeproposition(_propkind, _U3), nl, 
	save_figure_and_syl(_F,_Q1,_Q2,_Q3), save_smp(S, M, P), 
	save_reaction(R), nl, save_time, reset_answer_given, 
	write("Decide with a click above whether this syllogism is valid or invalid -- as viewed by Aristoteles!"), nl, /.
write_syllogism_with_propkind(_).

write_syllogism_verbal :- write_syllogism_with_propkind(verbal).
write_syllogism_graph :- write_syllogism_with_propkind(graph).

reaction_valid :- answer_given(0), reaction(0), 
	nl, write("Wrong answer!"), nl, 
	reset_correct_answers,
	write("This is an invalid syllogism!"), nl, nl, 
	update_answer_given,/,
	log_answer(valid, false),
	nl.
reaction_valid :-  answer_given(0), 
	reaction(R), nl, write("Correct answer!"), nl, 
	addto_correct_answers,
	write("This is a valid syllogism!"), nl, 
	write("It is a "), write(R), nl, nl,
	update_answer_given,/,
	log_answer(valid, true),
	nl.
reaction_valid.


reaction_invalid :- answer_given(0), reaction(0), nl, write("Correct answer!"), nl, 
	addto_correct_answers,
	write("This is an invalid syllogism!"), nl, nl, 
	update_answer_given,/,
	log_answer(invalid, true),
	nl.
reaction_invalid :- answer_given(0), reaction(R), nl, write("Wrong answer!"), nl, 
	reset_correct_answers,
	write("This is a valid syllogism!"), nl, 
	write("It is a "), write(R), nl,nl,
	update_answer_given,
	/,
	log_answer(invalid, false),
	nl.
reaction_invalid.


help :- 	clearConsole, reset, 
	write("Here you must decide, whether a syllogism, randomly generated by the system,"), nl,
	write("is valid or invalid."), nl, 
	write("The syllogism will appear when you click the leftmost button named 'New syllogism'."), nl, 
	write("Then you must decide whether the syllogism is valid or invalid, and"), nl,
	write("indicate your decision by using the buttons named 'Valid' and 'Invalid'."), nl, 
	write("The particular type of validity which must be used, is the Aristotelian one"), nl,
	write("(and not the one that follows from use of Venn diagrams)."), nl, 
	write("This entails that all the concepts used in the syllogisms are assumed"), nl,
	write("to correspond to non-empty sets."), nl, nl,
	write("Click the button named 'Clear', if you wish to clear the screen."), nl, nl, /.

syll0(S, M, P, 1, pr(au, M, P), pr(au, S, M), pr(au, S, P), "barbara, 1st figure").
syll0(S, M, P, 1, pr(eu, M, P), pr(au, S, M), pr(eu, S, P), "celarent, 1st figure").
syll0(S, M, P, 1, pr(au, M, P), pr(iu, S, M), pr(iu, S, P), "darii, 1st figure").
syll0(S, M, P, 1, pr(eu, M, P), pr(iu, S, M), pr(ou, S, P), "ferio, 1st figure").
syll0(S, M, P, 1, pr(au, M, P), pr(au, S, M), pr(iu, S, P), "barbarix, 1st figure").
syll0(S, M, P, 1, pr(eu, M, P), pr(au, S, M), pr(ou, S, P), "feraxo, 1st figure").
syll0(S, M, P, 2, pr(eu, P, M), pr(au, S, M), pr(eu, S, P), "cesare, 2nd figure").
syll0(S, M, P, 2, pr(au, P, M), pr(eu, S, M), pr(eu, S, P), "camestres, 2nd figure").
syll0(S, M, P, 2, pr(eu, P, M), pr(iu, S, M), pr(ou, S, P), "festino, 2nd figure").
syll0(S, M, P, 2, pr(au, P, M), pr(ou, S, M), pr(ou, S, P), "baroco, 2nd figure").
syll0(S, M, P, 2, pr(au, P, M), pr(eu, S, M), pr(ou, S, P), "camestrop, 2nd figure").
syll0(S, M, P, 2, pr(eu, P, M), pr(au, S, M), pr(ou, S, P), "cesarox, 2nd figure").
syll0(S, M, P, 3, pr(iu, M, P), pr(au, M, S), pr(iu, S, P), "disamis, 3rd figure").
syll0(S, M, P, 3, pr(au, M, P), pr(iu, M, S), pr(iu, S, P), "datisi, 3rd figure").
syll0(S, M, P, 3, pr(au, M, P), pr(au, M, S), pr(iu, S, P), "darapti, 3rd figure").
syll0(S, M, P, 3, pr(eu, M, P), pr(au, M, S), pr(ou, S, P), "felapton, 3rd figure").
syll0(S, M, P, 3, pr(ou, M, P), pr(au, M, S), pr(ou, S, P), "bocardo, 3rd figure").
syll0(S, M, P, 3, pr(eu, M, P), pr(iu, M, S), pr(ou, S, P), "ferison, 3rd figure").
syll0(S, M, P, 4, pr(au, P, M), pr(au, M, S), pr(iu, S, P), "bramantip, 4th figure").
syll0(S, M, P, 4, pr(au, P, M), pr(eu, M, S), pr(eu, S, P), "camenes, 4th figure").
syll0(S, M, P, 4, pr(iu, P, M), pr(au, M, S), pr(iu, S, P), "dimaris, 4th figure").
syll0(S, M, P, 4, pr(eu, P, M), pr(au, M, S), pr(ou, S, P), "fesapo, 4th figure").
syll0(S, M, P, 4, pr(eu, P, M), pr(iu, M, S), pr(ou, S, P), "fresison, 4th figure").
syll0(S, M, P, 4, pr(au, P, M), pr(eu, M, S), pr(ou, S, P), "camenop, 4th figure").

syl_ext_validity(_X, _U1, _U2, _U3):- syl_validity(_Y,_U1, _U2, _U3), validity_check(_X,_Y).

syl_validity(1, _U1, _U2, _U3):- syll0(_, _, _, _, _U1, _U2, _U3, _), /.
syl_validity(2, _, _, _).

save_reaction(R) :- retract(reaction(_)), fail.
save_reaction(R) :- assertz(reaction(R), ()).

// Way of saving current S, M, P
cursmp(0,0,0).
save_smp(S,M,P) :- retract(cursmp(X,Y,Z)), assertz(cursmp(S, M, P), ()), /.
save_smp(S,M,P).


// Way of saving current figure and syllogism number
figure_syl(0,0,0,0).
save_figure_and_syl(_figure,_Q1,_Q2,_Q3) :-
	retract(figure_syl(_,_,_,_)),
	assertz(figure_syl(_figure,_Q1,_Q2,_Q3), ()),
	/.
save_figure_and_syl.

pos_syll(S, M, P, 1, _Q1, _Q2, _Q3, pr(_Q1, M, P), pr(_Q2, S, M), pr(_Q3, S, P)).
pos_syll(S, M, P, 2, _Q1, _Q2, _Q3, pr(_Q1, P, M), pr(_Q2, S, M), pr(_Q3, S, P)).
pos_syll(S, M, P, 3, _Q1, _Q2, _Q3, pr(_Q1, M, P), pr(_Q2, M, S), pr(_Q3, S, P)).
pos_syll(S, M, P, 4, _Q1, _Q2, _Q3, pr(_Q1, P, M), pr(_Q2, M, S), pr(_Q3, S, P)).


writepropositionx(graph, pr(au, S, P)) :- 
     writeproposition(graph, pr(au, S, P)), 
     write("   "), 
     writeproposition(graph, pr(iu, S, P)), /.
writepropositionx(_propkind, pr(X, S, P)) :- 
     writeproposition(_propkind, pr(X, S, P)).

writeproposition(verbal, pr(Q, S, P)) :- writeproposition_verbal(pr(Q, S, P)).
writeproposition(graph,  pr(Q, S, P)) :- writeproposition_graph(pr(Q, S, P)).


writeproposition_verbal(pr(au, x, y)) :- write("All "), write(x), write(" are "), write(y), write(".").
writeproposition_verbal(pr(iu, x, y)) :- write("Some "), write(x), write(" are "), write(y), write(".").
writeproposition_verbal(pr(eu, x, y)) :- write("No "), write(x), write(" are "), write(y), write(".").
writeproposition_verbal(pr(ou, x, y)) :- write("Some "), write(x), write(" are not "), write(y), write(".").


writeproposition_graph(pr(au, S, P)) :- write("All "), write(S), write(" are "), write(P), write("."),nl,
write("   "),write("[All: x] ( IF: ([x] -attr-> ["),write(S),write("])  THEN:  ([x] -attr -> ["),write(P),write("]))"),nl,
write("   "),write("[All: x] ( IF:  ~([x] -attr-> ["),write(P),write("])  THEN:  ~([x] -attr -> ["),write(S),write("]))"),nl.
// [All: x] (IF: ([x] -attr-> [S]) THEN: ([x] -attr -> [P]))
// [All: x] (IF: ~([x] -attr-> [P]) THEN: ~([x] -attr -> [S]))

writeproposition_graph(pr(iu, S, P)) :- write("Some "), write(S), write(" are "), write(P), write("."), nl, 
write("   "),write("[x](   ([x] -attr-> ["),write(S),write("])    ([x] -attr -> ["),write(P),write("])   )"),nl.
// [x] (([x] -attr-> [S]) ([x] -attr -> [P]))

writeproposition_graph(pr(eu, S, P)) :- write("No "), write(S), write(" are "), write(P), write("."), nl, 
write("   "),write("[All: x] (IF: ([x] -attr-> ["),write(S),
write("]) THEN: ~([x] -attr -> ["),
write(P),write("]))"),nl,
write("   "),write("[All: x] (IF: ([x] -attr-> ["),write(P),
write("]) THEN: ~([x] -attr -> ["),write(S),write("]))"),nl.
// [All: x] (IF: ([x] -attr-> [S]) THEN: ~([x] -attr -> [P]))
// [All: x] (IF: ([x] -attr-> [P]) THEN: ~([x] -attr -> [S]))

writeproposition_graph(pr(ou, S, P)) :- 
write("Some "), write(S), write(" are not "), write(P), write("."),nl,
write("   "),write("[x](   ([x] -attr-> ["),write(S), 
write("])    ~([x] -attr -> ["),write(P),write("])   )"),nl.
// [x] (([x] -attr-> [S]) ~([x] -attr -> [P]))

// This indicates that we have not generated a user id in this session yet.
// This will be retracted, and replaced with a randomly generated user id.
generated_uid(0).

// Generate a user id if we haven't done so already
generate_uid_if_not_there_already :- generated_uid(X), dif(0, X), /.
generate_uid_if_not_there_already :-
	generated_uid(X), eq(0, X),
	retract(generated_uid(0)), 
	rnd(10000, 100000000, _newUID), 
	assertz(generated_uid(_newUID), ()), /.
generate_uid_if_not_there_already.

// Get current time in Unix epoch milliseconds
get_time_now(_milliseconds_unix_epoch) :-
        // Get system time since January 1, 1970, midnight UTC.
        external("getTimeNow", (), _milliseconds_unix_epoch).


// Save time of creation of syllogism
syllogism_creation_time(0).
save_time :- suppress(syllogism_creation_time, 1),
	get_time_now(_creation_time_in_milliseconds),
	assertz(syllogism_creation_time(_creation_time_in_milliseconds), ()), /.
save_time.

// Get time in milliseconds taken to answer question
get_time_to_answer(_milliseconds) :-
	get_time_now(_now_milliseconds),
	syllogism_creation_time(_start_milliseconds),
	val(_milliseconds, sub(_now_milliseconds, _start_milliseconds)).


log_answer(_validity, _correct) :-
        propkind(_propkind),
	reaction(_R),
	figure_syl(_figure, _Q1,_Q2,_Q3),
	cursmp(S, M, P),
	term(S, _S),
	term(M, _M),
	term(P, _P),
	pos_syll(S, M, P, _figure, _Q1,_Q2,_Q3, _U1, _U2, _U3), 
	conclusion(_conclusion, _U3),
	get_time_to_answer(_timetaken),
	generated_uid(_uid),
	concat("uid=", _uid, _s1),
	concat(_s1, "&timelapse=", _s2),
	concat(_s2, _timetaken, _s3),
	concat(_s3, "&figure=", _s4),
	concat(_s4, _figure, _s5),
	concat(_s5, "&q1=", _s6),
	concat(_s6, _Q1,_s7),
	concat(_s7, "&q2=", _s8),
	concat(_s8, _Q2,_s9),
	concat(_s9, "&q3=", _s10),
	concat(_s10, _Q3,_s11),
	concat(_s11, "&corr=", _s12),
	concat(_s12, _correct, _s13),
	concat(_s13, "&S=", _s14),
	concat(_s14, S, _s15),
	concat(_s15, "&M=", _s16),
	concat(_s16, M, _s17),
	concat(_s17, "&P=", _s18),
	concat(_s18, P, _s19),
	concat(_s19, "&conclusion=", _s20),
	concat(_s20, _conclusion, _s21),
	concat(_s21, "&validity=", _s22),
	concat(_s22, _validity, _s23),
	concat(_s23, "&propkind=", _s24),
	concat(_s24, _propkind, _query),
	sendURL(_query).

log_answer2(_validity, _correct) :-
       	ccount(_ccount),
	figure_syl(_figure, _Q1,_Q2,_Q3),
	cursmp(S, M, P),
	term(S, _S),
	term(M, _M),
	term(P, _P),
	pos_syll(_S, _M, _P, _figure, _Q1,_Q2,_Q3, _U1, _U2, _U3), 
	conclusion(_conclusion, _U3),
	get_time_to_answer(_timetaken),
	generated_uid(_uid),
	concat("uid=", _uid, _s1),
	concat(_s1, "&timelapse=", _s2),
	concat(_s2, _timetaken, _s3),
	concat(_s3, "&figure=", _s4),
	concat(_s4, _figure, _s5),
	concat(_s5, "&q1=", _s6),
	concat(_s6, _Q1,_s7),
	concat(_s7, "&q2=", _s8),
	concat(_s8, _Q2,_s9),
	concat(_s9, "&q3=", _s10),
	concat(_s10, _Q3,_s11),
	concat(_s11, "&corr=", _s12),
	concat(_s12, _correct, _s13),
	concat(_s13, "&S=", _s14),
	concat(_s14, S, _s15),
	concat(_s15, "&M=", _s16),
	concat(_s16, M, _s17),
	concat(_s17, "&P=", _s18),
	concat(_s18, P, _s19),
	concat(_s19, "&conclusion=", _s20),
	concat(_s20, _conclusion, _s21),
	concat(_s21, "&validity=", _s22),
	concat(_s22, _validity, _s23),
	concat(_s23, "&rule_clicks=", _s24),
	concat(_s24, _ccount, _query),
	sendURL(_query).


myurlbase(_urlbase) :-
        // First get the url of the web server installation, defined 
        // at the top of this file.
        web_server_url(_url),
        // Now build the rest of it.
	concat(_url, "/logsyllog/log4/?", _urlbase).


sendURL(_query) :-
    myurlbase(_urlstring1),
    concat(_urlstring1, _query, _urlstring),
    external("visitURL", (_urlstring), _X).


quan(1, au).
quan(2, iu).
quan(3, eu).
quan(4, ou).

find_reaction(_U1, _U2, _U3, R) :- syll0(_, _, _, _, _U1, _U2, _U3, R), /.
find_reaction(_, _, _, 0).

choose_syl_numbers(_F, _N1, _N2, _N3):- rnd(1, 5, _F), rnd(1, 5, _N1), rnd(1, 5, _N2), rnd(1, 5, _N3).

conclusion(0, pr(au, males, mothers)).
conclusion(0, pr(au, males, fathers)).
conclusion(0, pr(au, males, parents)).
conclusion(0, pr(au, females, mothers)).
conclusion(0, pr(au, females, fathers)).
conclusion(0, pr(au, females, parents)).
conclusion(0, pr(au, adults, mothers)).
conclusion(0, pr(au, adults, fathers)).
conclusion(0, pr(au, adults, parents)).
conclusion(0, pr(iu, males, mothers)).
conclusion(1, pr(iu, males, fathers)).
conclusion(1, pr(iu, males, parents)).
conclusion(1, pr(iu, females, mothers)).
conclusion(0, pr(iu, females, fathers)).
conclusion(1, pr(iu, females, parents)).
conclusion(1, pr(iu, adults, mothers)).
conclusion(1, pr(iu, adults, fathers)).
conclusion(1, pr(iu, adults, parents)).
conclusion(1, pr(eu, males, mothers)).
conclusion(0, pr(eu, males, fathers)).
conclusion(0, pr(eu, males, parents)).
conclusion(0, pr(eu, females, mothers)).
conclusion(1, pr(eu, females, fathers)).
conclusion(0, pr(eu, females, parents)).
conclusion(0, pr(eu, adults, mothers)).
conclusion(0, pr(eu, adults, fathers)).
conclusion(0, pr(eu, adults, parents)).
conclusion(1, pr(ou, males, mothers)).
conclusion(1, pr(ou, males, fathers)).
conclusion(1, pr(ou, males, parents)).
conclusion(1, pr(ou, females, mothers)).
conclusion(1, pr(ou, females, fathers)).
conclusion(1, pr(ou, females, parents)).
conclusion(1, pr(ou, adults, mothers)).
conclusion(1, pr(ou, adults, fathers)).
conclusion(1, pr(ou, adults, parents)).
// conclusion(0, _U3).

// For debugging purposes

write_answer_given:- answer_given(X), write("Answer given: "), write(X), fail.
write_answer_given.


// Proof-tester

reset_proof :- retract(to_be_proved(_)), fail.
reset_proof :- retract(given_in_proof(_)), fail.
reset_proof.

reset_proof_only :- retract(given_in_proof(_)), fail.
reset_proof_only.

reset_total :- retract(total(_)), fail.
reset_total.

reset_score :- retract(score(_)), fail.
reset_score.

total(1).
score(0).
ccount(0).
reaction(0).


reset_ccount :- retract(ccount(_)), fail.
reset_ccount :- assertz(ccount(0),()), fail.
reset_ccount.

update_total:- total(N), val(N1,add(N,1)), reset_total, assertz(total(N1),()), reset_proof.
update_score:- score(N), val(N1,add(N,1)), reset_score, assertz(score(N1),()).

update_ccount :- ccount(N), retract(ccount(N)), val(N1,add(N,1)), assertz(ccount(N1),()),/.

write_total_score:- write("Your score is "), score(S), write(S), write(" of "), total(T), write(T), nl.

write_cg(exist(attr(S), attr(P))) :- 
	write("Some "),write(S), 
	write(" are "), write(P).
write_cg(exist(attr(S), neg(attr(P)))) :- 
	write("Some "), write(S), 
	write(" are not "), write(P).
write_cg(exist(neg(attr(S)), attr(P))) :- 
	write("Some non-"), write(S), 
	write(" are "), write(P).
write_cg(exist(neg(attr(S)), neg(attr(P)))) :- 
	write("Some non-"), write(S), 
	write(" are not "), write(P).
write_cg(if_then(attr(S), attr(P))) :- 
	write("All "), 
	write(S), write(" are "), write(P).
write_cg(if_then(neg(attr(S)), attr(P))) :- 
	write("All non-"), write(S), 
	write(" are "), write(P).
write_cg(if_then(attr(S), neg(attr(P)))) :- 
	write("All "), write(S), 
	write(" are non-"), write(P).
write_cg(if_then(neg(attr(S)), neg(attr(P)))) :- 
	write("All non-"), write(S), 
	write(" are non-"), write(P).

given_in_proof(0).

write_new_proof :- 
	answer_given(1), correct_answers(X),
	clearConsole, 
        reset_proof, 
	generate_uid_if_not_there_already,
	rnd(1, 4, S), term(S, _S), rnd(4, 7, P), term(P, _P), 
	rnd(7, 10, M), term(M, _M), /, 
	rnd(1,3,V),
	find_syll(V, _S, _M, _P, _F, _Q1, _Q2, _Q3, _U1, _U2, _U3), 
	reset_answer_given, reset_ccount,
	find_reaction(_U1, _U2, _U3, R), 
	save_figure_and_syl(_F,_Q1,_Q2,_Q3), save_smp(S, M, P), 
	save_reaction(R), save_time,
	translation(_U3, _V3), translation(_U2, _V2), translation(_U1, _V1), 
	assertz(to_be_proved(syl(_U1,_U2,_U3,_V3)), ()), 
	assertz(given_in_proof(_V1), ()), 
	assertz(given_in_proof(_V2), ()),
	write_status_in_proof.

to_be_proved(0).

translation(pr(au, x, y), if_then(attr(x), attr(y))).
translation(pr(eu, x, y), if_then(attr(x), neg(attr(y)))).
translation(pr(iu, x, y), exist(attr(x), attr(y))).
translation(pr(ou, x, y), exist(attr(x), neg(attr(y)))).

write_status_in_proof:- 
	clearConsole,
	to_be_proved(syl(_U1, _U2, _U3, _V3)), 
	writeproposition_verbal(_U1), nl, 
	writeproposition_verbal(_U2), nl, write("Ergo:"), nl, 
	writeproposition_verbal(_U3), nl, nl, 
	write("Here you may check if this conclusion is provable from the two premises!"),nl, nl,
	write_cg(_V3), nl, write("Proof:"), nl, 
	write_given_in_proof.

write_proof_quality :- ccount(_N), write("You have used deduction rules "), write(_N), 
	write(" times."), /,nl.

write_given_in_proof :- given_in_proof(U), write_cg(U), nl, fail.
write_given_in_proof.

apply_trans:- update_ccount, given_in_proof(if_then(G1,G2)), 
	given_in_proof(if_then(G2,G3)), 
	assert_new(if_then(G1,G3)), 
	write_status_in_proof.
apply_subst:- update_ccount, given_in_proof(if_then(G1,G2)), 
	given_in_proof(exist(G3,G1)), 
	assert_new(exist(G3,G2)), 
	write_status_in_proof.
apply_contra:- update_ccount, given_in_proof(if_then(G1,G2)), 
	negated(G1,N1), negated(G2,N2),
	assert_new(if_then(N2,N1)), 
	write_status_in_proof.
apply_ex:- update_ccount, given_in_proof(if_then(G1,G2)), 
	assert_new(exist(G1,G2)),  
	write_status_in_proof.
apply_mut:- update_ccount, given_in_proof(exist(G1,G2)),
	assert_new(exist(G2,G1)), 
	write_status_in_proof.

apply_mut1:- apply_mut,/.
apply_mut1.

negated(attr(x),neg(attr(x))).
negated(neg(attr(x)),attr(x)).

assert_new(C):- given_in_proof(C), /.
assert_new(C):- assertz(given_in_proof(C),()).

react_correct :- update_score, write_total_score,  update_total, update_answer_given1, write_next.
react_incorrect :- write_total_score, update_total, update_answer_given1, write_next.

write_next :- nl, write("Click on New to continue!"), nl.

write_explanation:- to_be_proved(syl(_U1, _U2, _U3,_)), syl_ext_validity(X,_U1, _U2, _U3), write_expl(X).

write_expl(2):- write("This syllogism is invalid.").
write_expl(1):- write("This syllogism is valid.").

apply_valid:- 
	answer_given(0), to_be_proved(syl(_U1, _U2, _U3,_)), 
	syl_ext_validity(1,_U1, _U2, _U3), nl,
	write("Correct! This syllogism is valid."), 
	log_answer2(valid,true),
	nl, react_correct,/. 
apply_valid:- answer_given(0), nl, write("No, this is wrong! "), write_explanation, nl, react_incorrect,  
	log_answer2(valid,false),
	/, nl.

apply_invalid:- answer_given(0), to_be_proved(syl(_U1, _U2, _U3,_)), 
	syl_ext_validity(2,_U1, _U2, _U3), nl,
	write("Correct! This is an invalid syllogism."), 
	nl, react_correct, 
	log_answer2(invalid,true),
	/,nl. 
apply_invalid:- answer_given(0), nl, write("No, this is wrong! This is in fact a valid syllogism."), 
	nl, react_incorrect, 
	log_answer2(invalid,false),
	/,nl.


`;

var bCompiledCorrectly = prolog.compileProgram(program);
var errorMessage = prolog.getErrorMessage();

if (!bCompiledCorrectly) {
    alert("bCompiledCorrectly = " + bCompiledCorrectly + "\nErrorMessage = " + errorMessage);
}

//var bQueriedCorrectly = prolog.runQuery("main, grandfather(abraham, X).");
var bQueriedCorrectly = prolog.runQuery("help.");
/*
if (!bQueriedCorrectly) {
    alert("bQueriedCorrectly = " + bQueriedCorrectly + "\nError = " + prolog.getErrorMessage());
}
*/

function getTimeNow() {
    var date = new Date();
    return date.getTime();
}

function playSound(filename) {
    // From https://stackoverflow.com/questions/10105063/how-to-play-a-notification-sound-on-websites

    var myfilename;
    if (filename.length > 2 && filename[0] == '"' && filename[filename.length-1] == '"') {
	// From Prolog+CG, we get the string, but with surrounding quotes.
	myfilename = filename.slice(1, filename.length-1);
    } else {
	myfilename = filename;
    }

    var mp3Source = '<source src="' + myfilename + '.mp3" type="audio/mpeg">';
    var oggSource = '<source src="' + myfilename + '.ogg" type="audio/ogg">';
    var embedSource = '<embed hidden="true" autostart="true" loop="false" src="' + myfilename +'.mp3">';
    var inner = '<audio autoplay="autoplay">' + mp3Source + oggSource + embedSource + '</audio>';
    document.getElementById("sound").innerHTML=inner;
}

function visitURL(url) {
    console.log("UP210: url = " + url);
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
	if (this.readyState == 4 && this.status == 200) {
	    document.getElementById("demo").innerHTML = this.responseText;
	    console.log("UP210: response = " + this.responseText);
	}
    };
    var myurl;
    if (url.length > 2 && url[0] == '"' && url[url.length-1] == '"') {
	myurl = url.slice(1, url.length-1);
    } else {
	myurl = url;
    }
    console.log("UP200: myurl = '" + myurl + "'");
    xhttp.open("GET", myurl, true);
    xhttp.send();
    return false;
}

function writeNewProof() {
    bQueriedCorrectly = prolog.runQuery("write_new_proof.");
}

function applySubst() {
    bQueriedCorrectly = prolog.runQuery("apply_subst.");
}

function applyContra() {
    bQueriedCorrectly = prolog.runQuery("apply_contra.");
}

function applyTrans() {
    bQueriedCorrectly = prolog.runQuery("apply_trans.");
}

function applyMut() {
    bQueriedCorrectly = prolog.runQuery("apply_mut.");
}

function applyEx() {
    bQueriedCorrectly = prolog.runQuery("apply_ex.");
}

function applyInvalid() {
    bQueriedCorrectly = prolog.runQuery("apply_invalid.");
}

function applyValid() {
    bQueriedCorrectly = prolog.runQuery("apply_valid.");
}




function clearConsole() {
    prolog.runQuery("clearscreen.");
}

function writeHelp() {
    if (prolog.runQuery("help.")) {
 	console.log("help/0 succeeded.");
    } else {
 	console.log("help/0 did not succeed.");
    }
}

