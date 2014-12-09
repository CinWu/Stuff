var mouseX, mouseY;

var track = function() {
    document.write(mouseX)
    document.write(mouseY)
}

window.addEventListener('mousemove', function(e) {
    mouseX = e.pageX;
    mouseY = e.pageY;
});

