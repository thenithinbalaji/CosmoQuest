window.onload = function () {

    document.getElementById('navbar').classList.add('animate__fadeInDown');
    document.getElementById('title').classList.add('animate__fadeInUp');
    document.getElementById('heroimg').classList.add('animate__fadeInUp2');

    setTimeout(function () {
        document.getElementById('navbar').style.visibility = 'visible';
        document.getElementById('title').style.visibility = 'visible';

    }, 500);

    setTimeout(function () {
        document.getElementById('title').style.visibility = 'visible';
    }, 1000);

    setTimeout(function () {
        document.getElementById('heroimg').style.visibility = 'visible';
    }, 2000);
};
