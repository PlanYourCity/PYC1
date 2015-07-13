$('document').ready(function(){

	$('.boton').mouseenter(function(){
		$(this).removeClass('btn-primary-bg');
	});

	$('.evento').mouseleave(function(){
		$(this).addClass('btn-primary-bg');
	});

});