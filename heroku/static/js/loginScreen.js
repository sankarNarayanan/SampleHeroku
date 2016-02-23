$(document).ready(function() {

    $('#goToLogin').click(function(){
           $('.header').animate({height: "18%", opacity: "toggle"}, "slow");
           //$('.header').css('height','18%');
		   $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
		});

    $('#goToCreateUser').click(function(){
           $('.header').animate({height: "2%", opacity: "toggle"}, "slow");
		   $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
		});



    $('#loginButton').click(function (event) {
        if (($('#loginUserName').val() != '') && ($('#loginPassword').val() != '')) {
            $('.loading').removeClass('displayNone');
        }else{
            event.preventDefault();
            alertify.error('Enter all the fields');
        }
	});


	$('#createUser').click(function (event) {
        $('.loading').removeClass('displayNone');
        event.preventDefault();
        var request = $.post( baseUrl.concat('createUser/'), $( ".register-form" ).serialize(), function(response) {
            $('.loading').addClass('displayNone');
            //alert(response.status);
            alertify.success(response.status);
            $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
            $('.header').css('height','18%');
        })
        .done(function() {

        })
        .fail(function(error) {
                $('.loading').addClass('displayNone');
                alert("error="+error.statusText);
        })
        .always(function() {

        });

	});

});