/*
global interpretter lock
once getslow is called, python waits until that is finished before doing other stuff
*/

car log = function(d) {
    console.log(d);
};

var go = function() {
    //$.get("/getstuff");
    //x = $.get("/getstuff");

/* 
   $.get("/getstuff", function(d) {
	console.log("getstuff got:" + d);
    }
*/
/*
//random
    $.get("/getfast",log);
    $.get("/getslow",log);
    $.get("/getstuff",log);
*/
    //pyramid programming
    //make sure things happen in sequence
    $.get("/getslow",function(d) {
	log(d);
	$.get("/getfast",function(d) {
	    log(d);
	    $.get("/getstuff",function(d) {
		log(d);
	    }
		 )
	}
	     )
    }
	 )
}

var params = function() {
    $get("/upcase",{'data':'somthingtoupcase'},function(d){
	console.log(d);
    }
	)

$(document).ready(function() {
    h = document.getElementById('header');
    h.addEventListener('click',go)
    //normally "name" starter stuff goes here
}

		
