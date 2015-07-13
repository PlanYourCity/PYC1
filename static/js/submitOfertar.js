$('document').ready(function(){

	$('#buttonForm').click(function(e){

		var url = "/ofertar/"+$('input[type="hidden"]').val()+"/";
		var img = "&Imagen="+$('input[type="file"]').val();
		var datosForm = $('#formOfertar').serialize();

		$.ajax({
		  method: "POST",
		  url: url,
		  data: datosForm+img,
		  success: function(data){
		  	if(data.message == true){
		  		alertify.set('notifier','position','top-right');
				alertify.success('¡¡Evento registrado!!');
		  	}
		  	else{
		  		alertify.set('notifier','position','top-right');
				alertify.error('¡¡El evento ya existe!!');
		  	}
		  }
		});

		return false;		
	
	});
		
});