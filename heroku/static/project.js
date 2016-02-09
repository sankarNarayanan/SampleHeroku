$(document).ready(function() {
	$('.message a').click(function(){
		   $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
		});

	$('#loginButton').click(function(){
		alertify.success("Success log message");
	});
});