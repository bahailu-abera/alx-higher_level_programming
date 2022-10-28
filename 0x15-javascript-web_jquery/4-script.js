$(function () {
    $('DIV#toggle_header').addClass('red');

    $('DIV#toggle_header').click(function () {
	$(this).toggleClass('red');
	$(this).toggleClass('green');
    });
});
