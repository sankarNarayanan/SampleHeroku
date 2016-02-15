$(document).ready(function() {
	$('.message a').click(function(){
		   $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
		});


	$('#createUser').click(function (event) {

        $('.loading').removeClass('displayNone');

        event.preventDefault();

        var request = $.post( baseUrl.concat('createUser/'), $( ".register-form" ).serialize(), function(response) {
            $('.loading').addClass('displayNone');
            //alert(response.status);
            alertify.success(response.status);
        })
        .done(function() {

        })
        .fail(function(error) {
        alert("error="+error.statusText);
        })
        .always(function() {

        });

	});

});