function collapseSections() {
	var path = window.location.pathname;
	if ($("body").hasClass("template-atct_edit") || 
		path.indexOf('/++add++') != -1 || 
		path.indexOf('/++edit++') != -1) {
		$("body").find("form.enableFormTabbing").each(function() {
			$(this).removeClass("enableFormTabbing");
	});
    $("fieldset").each(function(index) {
       if(index !== 0) {
         $(this).collapse({ closed : true });
       } else {
         $(this).collapse();
       }
    });
   } 
}

$(document).ready(function() {
  collapseSections();
});
