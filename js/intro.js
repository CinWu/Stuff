console.log("HELLO WORLD");
var i = 10;
var s = "this is a a string";
console.log(i);
/*
  function f(x) {
  var i = x;
  i=i+1;
  console.log(i);
  }
*/
var f = function(x) {
    return x + 1;
}

var fact = function(n) {
    var p = 1;
    for (; n > 1; n--)
	p = p*n
    return p
}
var o = { 'name':'joe',
	  age:15,
	  n:[1,2,3,4,5],
	  f:function(x) {
	      return x+1
	  }
	}

var addItem = function(text) {
    var list = document.getElementByTagName('ol')[0];
    var newitem = document.createElement('li');
    newitem.innerHTML = text;
    list.addChild(newitem);
    
