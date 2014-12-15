var quoteFactory = function(){

    var makeQuoteElt = function(d) {
	var elt = "<blockquote><p>" + d.quote + "</p></blockquote>";
	$("#aquote").append(elt);
    };
    //takes a json blob including a quote from quotes.com and add it to the aquote div
    
    var insertQuote = function(d) {
	//make a new element with the quote
	makeQuoteElt(d);
	//append to div aquote

    };

    var addQuote = function(d) {
	$.getJSON("/quote", insertQuote);
    };

    var clearQuotes = function() {
	$("#aquote").empty();
    };

    var changeRandomQuote = function() {
	$.getJSOn("/quote", function(d) {
	    var q = makeQuoteElt(d);
	    var elt = $("#quote");
	    //get rid of old quote after new quote
	    elt.fadeOut(2000,function(){
		elt.empty();
		elt.append(q);
		elt.fadeIn(2000);
	    });

	});
    };

    var interval;
    
    return {
//	add: insertQuote
	add: addQuote,
//	interval:inverval,
	rand: changeRandomQuote,
	clear: clearQuotes
    };
};

$(document).ready(function() {
    console.log("HELLO");
    quotes = quoteFactory();
    $("#add").bind('click', quotes.add);
    $("#clear").bind('click', quotes.clear);
});

//"add" = tag
//"#add" = id

/*IN CONSOLE

d = {quote:'sample'}
quotes.add(d)

*/
