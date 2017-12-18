$(function(){
	

	$(".todo-item input[type=checkbox]").click(function(){
		if($(this).prop("checked")){
			$(this).parent().addClass('cross-text')
		}else{
			$(this).parent().removeClass('cross-text')
		}
	});

	$("#btn-clear").click(function(){
		$.post( "addtodo/", { 'todo_name': "test12" } ) .done(function( data ) {
		    //refresh
		    window.location=""
		  });
	});
});
