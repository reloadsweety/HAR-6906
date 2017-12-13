$(function(){
	$(".todo-item input[type=checkbox]").click(function(){
		if($(this).prop("checked")){
			$(this).parent().css({
				"text-decoration": "line-through",
    			"color": "#b5b5b5"
			})
		}else{
			$(this).parent().css({
				"text-decoration": "",
    			"color": ""
			})
		}
	});

	$("#btn-clear").click(function(){
		$(".todo-item input[type=checkbox]").prop("checked",false)
		$(".custom-control").css({
			"text-decoration": "",
			"color": ""
		})
	})
});