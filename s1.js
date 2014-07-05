function doit(){
    var x;
    
    if ( window.XMLHttpRequest) 
	x = new XMLHttpRequest();
    else
	x = new ActiveObject("Microsoft.XMLHTTP");
    
    x.onreadystatechange = function()
    {
	if ( x.readyState == 4 && x.status == 200 ) 
	    document.getElementById("myDiv").innerHTML = x.responseText;
    }
    x.open("GET","ajax_info.txt",true);
    x.sent();
}
