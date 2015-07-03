$('document').ready(function(){

	$('.evento').mouseenter(function(){
		$(this).addClass('hoverEvento');
	});

	$('.evento').mouseleave(function(){
		$(this).removeClass('hoverEvento');
	});

	$('.evento').click(function(){
		var a = $(this).find("h3").text();
		
		window.location = "http://localhost:8000/detalle/"+a;
	});

});