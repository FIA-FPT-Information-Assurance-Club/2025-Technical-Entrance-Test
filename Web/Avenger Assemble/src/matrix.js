document.addEventListener('DOMContentLoaded', () => {
    var canvas = document.getElementById('matrix');
    var ctx = canvas.getContext('2d');

    // Adjust canvas size
    canvas.height = window.innerHeight;
    canvas.width = window.innerWidth;

    // Characters - You can add your own
    var matrixChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789@#$%^&*()*&^%";
    matrixChars = matrixChars.split("");

    var font_size = 16;
    var columns = canvas.width / font_size; // Number of columns for the rain
    var drops = [];

    // Initialize drops
    for (var x = 0; x < columns; x++)
        drops[x] = 1; 

    // Draw function
    function draw() {
        // Translucent BG to show trail effect
        ctx.fillStyle = "rgba(0, 0, 0, 0.04)";
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        ctx.fillStyle = "#00FF7F"; // Emerald color
        ctx.font = font_size + "px 'Courier New'";

        // Loop over drops
        for (var i = 0; i < drops.length; i++) {
            var text = matrixChars[Math.floor(Math.random() * matrixChars.length)];
            ctx.fillText(text, i * font_size, drops[i] * font_size);

            // Reset drop to top randomly after it has crossed the screen
            if (drops[i] * font_size > canvas.height && Math.random() > 0.975)
                drops[i] = 0;

            drops[i]++;
        }
    }

    setInterval(draw, 35);

    // Resize canvas on window resize
    window.addEventListener('resize', () => {
        canvas.height = window.innerHeight;
        canvas.width = window.innerWidth;
        columns = canvas.width / font_size;
        drops = [];
        for (var x = 0; x < columns; x++)
            drops[x] = 1;
    });
});
