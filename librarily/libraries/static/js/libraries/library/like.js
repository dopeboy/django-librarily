$( document ).ready(function() 
{
	$("#like").click(function(event) 
	{
		console.log($(this).attr("href"));
		$.ajax(
		{
			url : $(this).attr("href"), // the endpoint
			type : "POST", // http method
			data : { 'csrfmiddlewaretoken': $.cookie('csrftoken')}, // data sent with the post request

			// handle a successful response
			success : function(json) 
			{
				$("#likes").text(json.likes);
				console.log(json); // log the returned json to the console
				console.log("success"); // another sanity check
			},

			// handle a non-successful response
			error : function(xhr,errmsg,err) {
				console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
			}
		});

		event.preventDefault();
	});
});
