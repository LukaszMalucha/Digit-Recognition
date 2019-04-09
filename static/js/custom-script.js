$('.dropdown-trigger').dropdown();


$(document).ready(function() {

    $('.sidenav').sidenav();

});

// Digit Identifier Canvas

var md = false;
    var canvas = document.getElementById('canvas');
    canvas.addEventListener('mousedown', down);
    canvas.addEventListener('mouseup', toggledraw);
    canvas.addEventListener('mousemove',
        function(evt) {
            var mousePos = getMousePos(canvas, evt);
            var posx = mousePos.x;
            var posy = mousePos.y;
            draw(canvas, posx, posy);
        });


    function down() {
        md = true;
    }

    function toggledraw() {
        md = false;
        canvas.style.cursor = "default";
    }

    function getMousePos(canvas, evt) {
        var rect = canvas.getBoundingClientRect();
        return {
            x: evt.clientX - rect.left,
            y: evt.clientY - rect.top
        };
    }

    function draw(canvas, posx, posy) {
        var context = canvas.getContext('2d');
            context.fillStyle="white";

        if (md) {
            canvas.style.cursor = "pointer"
            context.fillRect(posx, posy, 30, 30);


        }

        document.getElementById('clear').addEventListener('click', function() {
            context.clearRect(0, 0, canvas.width, canvas.height);
        }, false);

    }

