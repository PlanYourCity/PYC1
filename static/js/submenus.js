$('document').ready(function(){

	$('.buscar').mouseenter(function(){

		$('.submenuBuscar').animate({
			"margin-left": "0px"
		}, 1000);
	});

	$('.buscar').mouseleave(function(){
		$('.submenuBuscar').animate({
			"margin-left": "-260px"
		}, 1000);
	});

	$('.ofertar').mouseenter(function(){
		$('.submenuOfertar').animate({
			"margin-left": "0px"
		}, 1000);
	});

	$('.ofertar').mouseleave(function(){
		$('.submenuOfertar').animate({
			"margin-left": "-260px"
		}, 1000);
	});

});