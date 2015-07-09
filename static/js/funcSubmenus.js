$('document').ready(function(){
	$('.submenuBuscar li').click(function(){
		var a = $(this).find("a").text().toLowerCase();

		window.location = "http://localhost:8000/buscar/"+a+"/";
	});

	$('.submenuOfertar li').click(function(){
		var a = $(this).find("a").text().toLowerCase();

		window.location = "http://localhost:8000/ofertar/"+a+"/";
	});
});