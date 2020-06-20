
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


// for navbar hide on click mobile
$(document).click(function() {
    var nav_clicked=0;
    $('nav').click(function () {
        nav_clicked=1;
    });

    $(document).click(function(){
        if (nav_clicked==0 && $(window).width()<1025 && $(window).scrollTop()>0){
            document.getElementById("myModal").style.top = "-100px";
        }
   });
});

window.passcheck=function(){
if($("#change_password").is(":visible")){
    $("#change_password").hide();
}
else{
    $("#change_password").show();
    $("#change_password").addClass('animate__animated animate__fadeIn');
}
};
function fill_info(ar, ct, ph, pc, nm, ds, id){
    document.getElementById('area_info').innerHTML= ar;
    document.getElementById('city_info').innerHTML= ct;
    document.getElementById('phone_info').innerHTML= ph;
    document.getElementById('pincode_info').innerHTML=pc ;
    document.getElementById('name_info').innerHTML=nm ;
    document.getElementById('desc_info').innerHTML=ds ;
    document.getElementById('header_mid_info').innerHTML="for ID :" ;
    document.getElementById('header_id').innerHTML=id ;
}

function assign(id){
    if (document.getElementById('header_id').innerHTML=="")
    {
        alert("Booking not selected!");
    }
    else
    {
        location.href=id+"/"+document.getElementById('header_id').innerHTML;

    }
}

window.trclick=function(id){
if($("#"+id).is(":visible")){
    $("#"+id).hide();
}
else{
    $("#"+id).show();
    $("#"+id).addClass('animate__animated animate__fadeIn');
}
};

//for loader
window.onload = function () {
    $("#change_password").hide();
	//$("#loading").addEventListener('animationend', () => {jQuery('#loading').remove()});
	jQuery('#loading').remove();
	$("body").addClass('animate__animated animate__fadeIn');
	$('#signup').hide();
	$('#more').hide();


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

function more_services() {
	$('#more').show();
	//$("#more").addClass('animate__animated animate__fadeIn');  //your current y position on the page

	$(window).scrollTop($('#more').position().top-100) ;
	// body...
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



