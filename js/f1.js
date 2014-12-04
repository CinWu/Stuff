var base = 10;

var otherfunc = function() {
    console.log('the other function f1');
}

//like java classes
var f1 = {
    base : 30,
    f : function(x) {
	console.log(base)
	this.base = this.base + 2;
	console.log(f1.base)
    }
}

var makeCounter = function() {
    var i = 0;
    return function() {
	i = i + 1;
	return i;
    }
}

var makeAdder = function(n) {
    return function(x) {
	return n + x;
    };
}

var makeCounter = function() {
    var i = 0;
    return { x : "some value",
	     get : function() { return i; },
	     inc : function() { i = i + 1; },
	     dec : function() { i = i - 1; },
	     set : function(x) { i = x; },
	     fx : function() { console.log(i); },
	   }
}

//not good for when there are multiple scripts
/*var base = 100;
var f1 = function(x){
    return x * base;
}
*/
