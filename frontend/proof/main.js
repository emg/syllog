var prolog = new PrologPlusCG.PPCGJS("#console");

var program = `
//
// Copyright (c) 2010-2021 Peter Oehrstroem and Ulrik Sandborg-Petersen
//
// License terms: MIT License.
// See the file LICENSE in the Syllog distribution.
//

repeat.
repeat :- repeat.

term(1, "males").
term(2, "females").
term(3, "adults").
term(4, "mothers").
term(5, "fathers").
term(6, "parents").
term(7, "students").
term(8, "teachers").
term(9, "doctors").

quan(1, au).
quan(2, iu).
quan(3, eu).
quan(4, ou).

pos_syll(S, M, P, 1, _Q1, _Q2, _Q3, pr(_Q1, M, P), pr(_Q2, S, M), pr(_Q3, S, P)).
pos_syll(S, M, P, 2, _Q1, _Q2, _Q3, pr(_Q1, P, M), pr(_Q2, S, M), pr(_Q3, S, P)).
pos_syll(S, M, P, 3, _Q1, _Q2, _Q3, pr(_Q1, M, P), pr(_Q2, M, S), pr(_Q3, S, P)).
pos_syll(S, M, P, 4, _Q1, _Q2, _Q3, pr(_Q1, P, M), pr(_Q2, M, S), pr(_Q3, S, P)).

find_syll(_V, _S, _M, _P, _F, _Q1, _Q2, _Q3, _U1, _U2, _U3) :- 
	repeat, choose_syl_numbers(_F, _N1, _N2, _N3), 
	quan(_N1, _Q1), quan(_N2, _Q2), quan(_N3, _Q3), 
	pos_syll(_S, _M, _P, _F, _Q1, _Q2, _Q3, _U1, _U2, _U3), 
	syl_validity(_V1, _U1, _U2, _U3), validity_check(_V1, _V), /.

choose_syl_numbers(_F, _N1, _N2, _N3) :- 
	rnd(1, 5, _F), rnd(1, 5, _N1), rnd(1, 5, _N2), rnd(1, 5, _N3).

syl_validity(1, _U1, _U2, _U3) :- syll0(_, _, _, _, _U1, _U2, _U3, _), /.
syl_validity(2, _, _, _).

validity_check(1, 1).
validity_check(2, 2).

writeproposition_verbal(pr(au, x, y)) :- write("All "), write(x), write(" are "), write(y), write(".").
writeproposition_verbal(pr(iu, x, y)) :- write("Some "), write(x), write(" are "), write(y), write(".").
writeproposition_verbal(pr(eu, x, y)) :- write("No "), write(x), write(" are "), write(y), write(".").
writeproposition_verbal(pr(ou, x, y)) :- write("Some "), write(x), write(" are not "), write(y), write(".").

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


// Proof-tester

reset_proof :- retract(to_be_proved(_)), fail.
reset_proof :- retract(given_in_proof(_)), fail.
reset_proof.

write_cg(exist(attr(S), attr(P))) :- 
	write("   "), write("[x](   ([x] -attr-> ["), write(S), 
	write("])    ([x] -attr -> ["), write(P), write("])   )").
write_cg(exist(attr(S), neg(attr(P)))) :- 
	write("   "), write("[x](   ([x] -attr-> ["), write(S), 
	write("])    ~([x] -attr -> ["), write(P), write("])   )").
write_cg(if_then(attr(S), attr(P))) :- 
	write("   "), write("[All: x] ( IF: ([x] -attr-> ["), 
	write(S), write("])  THEN:  ([x] -attr -> ["), write(P), write("]))").
write_cg(if_then(neg(attr(S)), attr(P))) :- 
	write("   "), write("[All: x] ( IF: ~([x] -attr-> ["), write(S), 
	write("])  THEN:  ([x] -attr -> ["), write(P), write("]))").
write_cg(if_then(attr(S), neg(attr(P)))) :- 
	write("   "), write("[All: x] ( IF: ([x] -attr-> ["), write(S), 
	write("])  THEN:  ~([x] -attr -> ["), write(P), write("]))").
write_cg(if_then(neg(attr(S)), neg(attr(P)))) :- 
	write("   "), write("[All: x] ( IF: ~([x] -attr-> ["), write(S), 
	write("])  THEN:  ~([x] -attr -> ["), write(P), write("]))").

given_in_proof(0).

write_new_proof :- 
	clearConsole, reset_proof, rnd(1, 4, S), term(S, _S), rnd(4, 7, P), term(P, _P), 
	rnd(7, 10, M), term(M, _M), /, 
	find_syll(1, _S, _M, _P, _F, _Q1, _Q2, _Q3, _U1, _U2, _U3), 
	translation(_U3, _V3), translation(_U2, _V2), translation(_U1, _V1), 
	assertz(to_be_proved(syl(_U1,_U2,_U3,_V3)), ()), 
	assertz(given_in_proof(_V1), ()), 
	assertz(given_in_proof(_V2), ()), apply_com1,
	write_status_in_proof.

to_be_proved(0).

translation(pr(au, x, y), if_then(attr(x), attr(y))).
translation(pr(eu, x, y), if_then(attr(x), neg(attr(y)))).
translation(pr(iu, x, y), exist(attr(x), attr(y))).
translation(pr(ou, x, y), exist(attr(x), neg(attr(y)))).

write_status_in_proof:- 
	clearConsole, to_be_proved(syl(_U1, _U2, _U3,_V3)), 
	writeproposition_verbal(_U1), nl, 
	writeproposition_verbal(_U2), nl, write("Ergo:"), nl, 
	writeproposition_verbal(_U3), nl, nl, 
	write("Conclusion:"),nl,
	write_cg(_V3), nl, write("Proof:"), nl, 
	write_given_in_proof, check_proved(_V3).

check_proved(_V):- given_in_proof(_V), write("The conclusion has been proved!"), /, nl.
check_proved(_V):- write("The conclusion has not yet been proved!"), /, nl.

write_given_in_proof :- given_in_proof(U), write_cg(U), nl, fail.
write_given_in_proof.

apply_trans:- given_in_proof(if_then(G1,G2)), 
	given_in_proof(if_then(G2,G3)), 
	assert_new(if_then(G1,G3)), 
	write_status_in_proof.
apply_subst:- given_in_proof(if_then(G1,G2)), 
	given_in_proof(exist(G1,G3)), 
	assert_new(exist(G2,G3)), 
	assert_new(exist(G3,G2)), 
	write_status_in_proof.
apply_contra:- given_in_proof(if_then(G1,G2)), 
	negated(G1,N1), negated(G2,N2),
	assert_new(if_then(N2,N1)), 
	write_status_in_proof.
apply_ex:- given_in_proof(if_then(G1,G2)), 
	assert_new(exist(G1,G2)), 
	assert_new(exist(G2,G1)), 
	write_status_in_proof.
apply_com:- given_in_proof(exist(G1,G2)), /,
	assert_new(exist(G2,G1)), 
	write_status_in_proof.

apply_com1:- apply_com,/.
apply_com1.

negated(attr(x),neg(attr(x))).
negated(neg(attr(x)),attr(x)).

assert_new(C):- given_in_proof(C), /.
assert_new(C):- assertz(given_in_proof(C),()).

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
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
	if (this.readyState == 4 && this.status == 200) {
	    // document.getElementById("demo").innerHTML = this.responseText;
	    // console.log("UP210: response = " + this.responseText);
	}
    };
    var myurl;
    if (url.length > 2 && url[0] == '"' && url[url.length-1] == '"') {
	myurl = url.slice(1, url.length-1);
    } else {
	myurl = url;
    }
    // console.log("UP200: myurl = '" + myurl + "'");
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

function applyEx() {
    bQueriedCorrectly = prolog.runQuery("apply_ex.");
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

