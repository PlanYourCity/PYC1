$('document').ready(function(){

	$('.botonesForm').click(function(e){
		
		var url = "/ofertar/"+$('input[type="hidden"]').val();
		var datosForm = $('#formOfertar').serialize();

		$.ajax({
		  method: "POST",
		  url: url,
		  data: datosForm,
		  success: function(data){
		  	alert("Evento creado");
		  },
		  error: function(err){
		  	alert("Error al crear evento: "+err.message);
		  }
		});

		return false;		
		
	});
		
});