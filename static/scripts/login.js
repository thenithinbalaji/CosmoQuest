var nStars = 0;
var colours = ["#E5D8D8", "#FFF6E5", "white", '#F3A75B', "yellow", "orange", "red"];

function generateStar(id) {
    var tempNStar = nStars;
    var starDiv = document.createElement('div');
    starDiv.className = 'star';
    starDiv.id = 'star' + nStars;
    document.querySelector(id).appendChild(starDiv);

    var randY = Math.random() * (window.innerHeight - 500); // Random Y position within viewport height
    var randX = Math.random() * (window.innerWidth - 500); // Random X position within viewport width
    var randDX = (Math.random() - 0.5) * 10; // Random horizontal velocity
    var randDY = (Math.random() - 0.5) * 10; // Random vertical velocity
    var randO = 0.5 + (Math.random() / 2); // Random opacity
    var randOT = Math.floor(Math.random() * 300) + 1; // Random opacity transition time
    var randC = Math.floor(Math.random() * colours.length); // Random color index
    var randDelay = Math.floor(Math.random() * 8000); // Random delay before animation starts
    var randDirectionY = (Math.random() < 0.5) ? '-' : '+'; // Random direction for Y axis
    var randDirectionX = (Math.random() < 0.5) ? '-' : '+'; // Random direction for X axis

    setTimeout(function () {
        starDiv.style.top = randY + 'px';
        starDiv.style.left = randX + 'px';
        starDiv.style.backgroundColor = colours[randC];
        starDiv.style.opacity = randO;

        setTimeout(function () {
            starDiv.style.transition = 'top ' + randOT + 'ms linear, left ' + randOT + 'ms linear, opacity 4s linear';
            starDiv.style.top = 'calc(' + randY + 'px ' + randDirectionY + ' ' + randDY + 'px)';
            starDiv.style.left = 'calc(' + randX + 'px ' + randDirectionX + ' ' + randDX + 'px)';
            starDiv.style.opacity = 0;

            setTimeout(function () {
                starDiv.parentNode.removeChild(starDiv);
                generateStar(id);
            }, 1000);
        }, 0);
    }, randDelay);

    nStars++;
}

function generateStars(id, number) {
    for (var i = 0; i < number; i++) {
        generateStar(id);
    }
}


window.onload = function () {

    // generateStars('body', 240);

    document.getElementById('loginForm').classList.add('animate__fadeInUp');
    document.getElementById('navbar').classList.add('animate__fadeInDown');

    setTimeout(function () {
        document.getElementById('loginForm').style.visibility = 'visible';
        document.getElementById('navbar').style.visibility = 'visible';

    }, 1000);
};

