$(window).resize(function(){
   var width = $(window).width();
 
   if(width <1024){

   	$('fspace').addClass('w-100');
   }
   
})
.resize();//trigger the resize event on page load.


// for navbar scroll
var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("myModal").style.top = "0";
  } else {
    document.getElementById("myModal").style.top = "-100px";
  }
  prevScrollpos = currentScrollPos;
}

setTimeout(fade_out, 3000);

function fade_out() {
  $('#myModal').modal('hide');
}



//for loader
jQuery(document).ready(function() {
	setTimeout(() => {  jQuery('#loading').remove(); }, 00);
});

