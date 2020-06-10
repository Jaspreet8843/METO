
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


//for viewport check

jQuery('body').on('appear', function(){
    console.log("das");
});


//for loader
window.onload = function () { 
	//$("#loading").addEventListener('animationend', () => {jQuery('#loading').remove()});
	jQuery('#loading').remove();
	$("body").addClass('animate__animated animate__fadeIn');
	$('#signup').hide();
	
	//$("#myModal").addClass('animate__animated animate__fadeInLeft animate__fast');
	//$("#fspace").addClass('animate__animated animate__fadeInRight animate__fast');
	//$("p").addClass('animate__animated animate__tada animate__fast');
	//var visible = $(#more).visible( detectPartial );
	
}

function signupclick()
{
	//$("#login").addClass('animate__animated animate__bounceOut')
		 $('#login').hide(); $('#signup').show();
		 $("#signup").addClass('animate__animated animate__flipInY');
}
function loginclick()
{
		$('#signup').hide(); $('#login').show();
	$("#login").addClass('animate__animated animate__flipInY');
}


//google button

function onSuccess(googleUser) {
      console.log('Logged in as: ' + googleUser.getBasicProfile().getName());
    }
    function onFailure(error) {
      console.log(error);
    }
    function renderButton() {
      gapi.signin2.render('my-signin2', {
        'scope': 'profile email',
        'width': 200,
        'height': 40,
        'align': 'center',
        'longtitle': true,
        'theme': 'dark',
        'onsuccess': onSuccess,
        'onfailure': onFailure
      });
    }



