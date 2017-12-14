$(function(){
	

	$(".todo-item input[type=checkbox]").click(function(){
		if($(this).prop("checked")){
			$(this).parent().addClass('cross-text')
		}else{
			$(this).parent().removeClass('cross-text')
		}
	});

	$("#btn-clear").click(function(){
		$(".todo-item input[type=checkbox]").prop("checked",false)
		$(".custom-control").removeClass('cross-text')
	})

	$(".todo-item").each(function(n){
		if($(this).attr("check") == "True"){
			$(".custom-control-input:nth("+n+")").click()
		}
	});

	$("#btn-add").click(function(){
		$.post( "addtodo/", { 'todo_name': "test12" } ) .done(function( data ) {
		    //refresh
		    window.location=""
		  });
	});
});

function add_todo(){
	$.post( "addtodo/", { 'todo_name': $("#todo_name").val() } ) .done(function( data ) {
	    window.location =""
	});
}