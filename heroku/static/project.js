$(document).ready(function() {
	$('.message a').click(function(){
		   $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
		});

	$('#loginButton').click(function(){
		alertify.success("Success log message");
	});


	$('#createUser').click(function (event) {

        event.preventDefault();

        var jqxhr = $.post( baseUrl.concat('createUser/'), $( ".register-form" ).serialize(), function(response) {
            alert(response.status);
        })
        .done(function() {

        })
        .fail(function(error) {
        alert("error="+error.statusText);
        })
        .always(function() {

        });


//        $.ajax({
//                type: "POST",
//                url: baseUrl.concat('createUser/'),
//                dataType: 'json',
//                data:$( ".register-form" ).serialize(),
//                //async: false,
//                //xhrFields: {
//                //    withCredentials: true
//                //},
//                crossDomain: true,
//                beforeSend: function(request) {
//                     request.setRequestHeader("X-Requested-With", "XMLHttpRequest");
//                     request.setRequestHeader("content-type", "application/json");
//                },
//                success: function(response){
//                    alert(response);
//                },
//                error: function (response) {
//                    alert(response.statusText);
//                }
//            }
//);



        //var postString = "userName="+$('#userName').val()+"&password="+$('#password').val()+"&phone="+$('#phone').val()+"&email="+$('#email').val();
        //
        //$.ajax({
        //    type: "POST",
        //    url: baseUrl.concat('createUser/'),
        //    xhrFields: {
        //        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
        //    },
        //    data: postString,
        //    success: function(response){
        //    alert(response.status);
        //    }
        //});

        //$.post(baseUrl.concat('createUser'),
        //{userName: $('#userName').val(),password: $('#password').val(),phone: $('#phone').val(),email: $('#email').val()},
        //function(data, status){
        //    alert("Data: " + data + "\nStatus: " + status);
        //});
	});

});