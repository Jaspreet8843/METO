


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




//for loader
window.onload = function () { 
	$("#loading").addClass('animate__animated animate__fadeOut animate__fast');
	//$("#loading").addEventListener('animationend', () => {jQuery('#loading').remove()});
	jQuery('#loading').remove();
	$("#myModal").addClass('animate__animated animate__fadeInLeft animate__fast');
	$("#fspace").addClass('animate__animated animate__fadeInRight animate__fast');
	$("p").addClass('animate__animated animate__tada animate__fast');

}

$(document).ready(function() {
  setTimeout(function() {
    $('.navbar').addClass('fixed');
  }, 300);
});


