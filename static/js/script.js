$(document).ready(function() {

    /* Sets copyright date in footer to current year
        https://www.youtube.com/watch?v=e0SnNNryAjQ*/
    $('#footer-year').text(new Date().getFullYear());
});

var options = {
    bottom: '32px', // default: '32px'
    right: '32px', // default: '32px'
    left: 'unset', // default: 'unset'
    time: '0.5s', // default: '0.3s'
    mixColor: '#fff', // default: '#fff'
    backgroundColor: '#fff', // default: '#fff'
    buttonColorDark: '#100f2c', // default: '#100f2c'
    buttonColorLight: '#fff', // default: '#fff'
    saveInCookies: false, // default: true,
    label: '🌓', // default: ''
    autoMatchOsTheme: true // default: true
}

const darkmode = new Darkmode(options);
darkmode.showWidget();

$(".darkmode-toggle").click(function() {
    $('h1').each(function() {
        $(this).toggleClass('darkmode');
    });
    $('h2').each(function() {
        $(this).toggleClass('darkmode');
    });
    $('h3').each(function() {
        $(this).toggleClass('darkmode');
    });
    $('h4').each(function() {
        $(this).toggleClass('darkmode');
    });
    $('h5').each(function() {
        $(this).toggleClass('darkmode');
    });
    $('p').each(function() {
        $(this).toggleClass('darkmode');
    });
    $('legend').each(function() {
        $(this).toggleClass('darkmode');
    });
    $('form').each(function() {
        $(this).toggleClass('darkmode');
    });
    $('.dm-btn').each(function() {
        $(this).toggleClass('darkmode-button');
    });
    $('.btn-outline-primary').each(function() {
        $(this).toggleClass('dm-btn-outline');
    });
    $('.hr').each(function() {
        $(this).toggleClass('hr-dm');
    });
});