var
    canv = document.getElementById('canvas'),
    ctx = canv.getContext('2d'),
    btnSend = document.querySelector("#drawn_img_submit"),
    btnClear = document.querySelector("#clear_btn"),
    isMouseDown = false,
    penWidth = 10;

function clearCanv(){
    ctx.fillStyle = 'white';
    ctx.rect(0, 0, canv.width, canv.height);
    ctx.fill();
    ctx.fillStyle = 'black';
    ctx.beginPath();
}

window.addEventListener("load",function(){
    clearCanv();
});

canv.addEventListener('mousedown', function(e) {
    isMouseDown = true;
});

canv.addEventListener('mouseup', function(e) {
    isMouseDown = false;
    ctx.beginPath();
});

ctx.lineWidth = penWidth;
canv.addEventListener('mousemove', function(e) {
    if (isMouseDown)
    {
        ctx.lineTo(e.clientX, e.clientY);
        ctx.stroke();

        ctx.beginPath();
        ctx.arc(e.clientX, e.clientY, penWidth / 2, 0, Math.PI * 2);
        ctx.fill();

        ctx.beginPath();
        ctx.moveTo(e.clientX, e.clientY);
    }
});

btnSend.addEventListener("click", function() {
    img = canvas.toDataURL('image/png');
    document.getElementById('drawn_img').value = img;
});

btnClear.addEventListener("click", function() {
    clearCanv()
});