$('document').ready(function(){
	$('.submenuBuscar li').click(function(){
		var a = $(this).find("a").text();

		window.location = "http://localhost:8000/busqueda"+a;
	});

	$('.submenuOfertar li').click(function(){
		var a = $(this).find("a").text();

		window.location = "http://localhost:8000/ofertar"+a;
	});
});