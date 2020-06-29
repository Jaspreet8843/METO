
// for navbar scroll
//var prevScrollpos = window.pageYOffset;
//window.onscroll = function() {
//  var currentScrollPos = window.pageYOffset;
//  if (prevScrollpos > currentScrollPos) {
//    document.getElementById("myModal").style.top = "0";
//  } else {
//    document.getElementById("myModal").style.top = "-100px";
//  }
//  prevScrollpos = currentScrollPos;
//}

window.onscroll = function(){
    if ($(window).scrollTop()>50 &&  $(window).width()<993 ){
        $("#navbar_open").show();
        $("#navbar_open").addClass('animate__animated animate__fadeInRight');
    }
    else{
        $("#navbar_open").fadeOut();
    }

}
//for viewport check

jQuery('body').on('appear', function(){
    console.log("das");
});

//smooth scroll to service categories
window.service_btn=function(){
   
    $(window).scrollTop($('#cat').position().top);
        
};

// PROFILE PAGE MOBILE VIEW SWITCH

function switch_bookings(){
    $("#bookings_view").fadeIn();
    $("#profile_view").hide();
    $("#settings_view").hide();
    $("#settings_view").hide();

}

function switch_settings(){
    $("#settings_view").fadeIn();
    $("#profile_view").hide();
    $("#bookings_view").hide();
}

function switch_profile(){
    $("#profile_view").fadeIn();
    $("#bookings_view").hide();
    $("#settings_view").hide();
}

//show services
function show_service(id){
    if( $(window).width()>992)
    {
        /*
        var flag=0;
        if(!$("#"+id).height()>0)
        {
            flag=1;
            $("#card-"+id).addClass('permahover');
            $("#"+id).show();
            $("#"+id).toggleClass("slidedown");
        }
        

        for(var i=1; i<9;i++)
        {
            if($("#cat"+i).height()>0 && ("cat"+i != id)){
                $("#card-cat"+i).removeClass('permahover');
                $("#cat"+i).toggleClass("slidedown");
                $("#cat"+i).delay(350).fadeOut();
            }   
            
        }
        if(flag!=1){
         $("#card-"+id).removeClass('permahover');
         $("#"+id).toggleClass("slidedown");
         $("#"+id).delay(350).fadeOut();
     }
        */
        var flag=0;
        if($("#"+id).is(":visible"))
        {
            flag=1;
            $("#card-"+id).removeClass('permahover');
             $("#"+id).velocity('slideUp');
        }
        

        for(var i=1; i<9;i++)
        {
            if($("#cat"+i).is(":visible") && ("cat"+i != id)){
                $("#card-cat"+i).removeClass('permahover');
                $("#cat"+i).velocity('slideUp');
            }   
            
        }
        if(flag!=1){
            $("#card-"+id).addClass('permahover');
            $("#"+id).velocity('slideDown');
        }



    }
    else{
    /*
        var flag=0;
        if(!$("#m"+id).height()>0)
        {
            flag=1;
            $("#card-"+id).addClass('permahover');
            $("#m"+id).show();
            $("#m"+id).toggleClass("slidedown");
        }
        

        for(var i=1; i<9;i++)
        {
            if($("#mcat"+i).height()>0 && ("cat"+i != id)){
                $("#card-cat"+i).removeClass('permahover');
                $("#mcat"+i).toggleClass("slidedown");
                $("#mcat"+i).delay(400).fadeOut();
            }   
            
        }
        if(flag!=1){
         $("#card-"+id).removeClass('permahover');
         $("#m"+id).toggleClass("slidedown");
         $("#m"+id).delay(400).fadeOut();
     }
    */
        var flag=0;
        if($("#m"+id).is(":visible"))
        {
            flag=1;
            $("#card-"+id).removeClass('permahover');
             $("#m"+id).delay(300).fadeOut();
             $("#m"+id).addClass('animate__animated animate__fadeOut');
        }
        

        for(var i=1; i<9;i++)
        {
            if($("#mcat"+i).is(":visible") && ("cat"+i != id)){
                $("#card-cat"+i).removeClass('permahover');
                $("#mcat"+i).hide();
            }   
            
        }
        if(flag!=1){
            $("#card-"+id).addClass('permahover');
            $("#m"+id).show();
            $("#m"+id).removeClass('animate__animated animate__fadeOut');
            $("#m"+id).addClass('animate__animated animate__fadeIn');
        }

    }
    
}


//Check password

function check_pass() {
      if (document.getElementById('password').value == '' &&
        document.getElementById('confirm_password').value == '') {
        document.getElementById('message').innerHTML = '';
      }
      else if (document.getElementById('password').value ==
        document.getElementById('confirm_password').value) {
        document.getElementById('message').innerHTML = '';
      } else {
        document.getElementById('message').style.color = 'red';
        document.getElementById('message').innerHTML = 'Password not matching';
      }
    }

function check_pass_pc() {
      if (document.getElementById('password_pc').value == '' &&
        document.getElementById('confirm_password_pc').value == '') {
        document.getElementById('message').innerHTML = '';
      }
      else if (document.getElementById('password_pc').value ==
        document.getElementById('confirm_password_pc').value) {
        document.getElementById('message').innerHTML = '';
      } else {
        document.getElementById('message').style.color = 'red';
        document.getElementById('message').innerHTML = 'Password not matching';
      }
    }


// for navbar hide on click mobile
/*
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
*/
window.passcheck=function(){
if($("#change_password").is(":visible")){
    $("#change_password").slideUp();
}
else{
    $("#change_password").slideDown();
    $('html,body').animate({
        scrollTop: $("#change_password").offset().top
    });
    $("#change_password").addClass('animate__animated animate__fadeIn');
}
}
window.passcheck_pc=function(){
if($("#change_password_pc").is(":visible")){
    $("#change_password_pc").slideUp();
}
else{
    $("#change_password_pc").slideDown();
    $("#change_password_pc").addClass('animate__animated animate__fadeIn');
}
}
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
    if (document.getElementById('header_id').innerHTML=="" || document.getElementById('visiting_date'+id).value=="")
    {
        alert("Booking or date not selected!");
    }
    else
    {
        document.getElementById('book_id_form').value=document.getElementById('header_id').innerHTML;
        document.getElementById('work_id_form').value=id;
        document.getElementById('visiting_date_form').value=document.getElementById('visiting_date'+id).value;
        document.forms['info_form'].submit();
        /*location.href=id+"/"+document.getElementById('header_id').innerHTML;*/

    }
}

window.trclick=function(id){
if($("#"+id).is(":visible")){
    $("#"+id).slideUp();
}
else{
    $("#"+id).slideDown();
}
}

function trclick_pc(id){
if($("#pc"+id).is(":visible")){
    $("#pc"+id).slideUp();
}
else{
    $("#pc"+id).slideDown();
}
}

//for loader
window.onload = function () {
    $("#change_password").hide();
	//$("#loading").addEventListener('animationend', () => {jQuery('#loading').remove()});
	jQuery('#loading').remove();
	$("body").addClass('animate__animated animate__fadeIn');
	$('#signup').hide();
	$('#forgot_password').hide();
	$('#more').hide();
    $("#inner_ring").addClass('animate__animated animate__backInLeft');
    $("#middle_ring").addClass('animate__animated animate__backInLeft animate__delay-1s');
    $("#outer_ring").addClass('animate__animated animate__backInLeft animate__delay-2s');
     $("#inner_ring_mob").addClass('animate__animated animate__backInLeft');
    $("#middle_ring_mob").addClass('animate__animated animate__backInLeft animate__delay-1s');
    $("#outer_ring_mob").addClass('animate__animated animate__backInLeft animate__delay-2s');
    $(".nav-btn").addClass('animate__animated animate__bounceIn animate__delay-5s');
    $("#signup-bar").addClass('animate__animated animate__fadeInDown animate__delay-4s');

	//$("#myModal").addClass('animate__animated animate__fadeInLeft animate__fast');
	//$("#fspace").addClass('animate__animated animate__fadeInRight animate__fast');
	//$("p").addClass('animate__animated animate__tada animate__fast');
	//var visible = $(#more).visible( detectPartial );

}

function navbar_close(){
    $('#mobile_nav').fadeOut();
     $('#bg-dark').fadeOut();
}
function navbar_open(){
 $('#mobile_nav').fadeIn();
 $('#bg-dark').fadeIn();   
}
function signupclick()
{
	//$("#login").addClass('animate__animated animate__bounceOut')
		 $('#login').hide(); $('#signup').show();$('#forgot_password').hide();
		 $("#signup").addClass('animate__animated animate__flipInY');
}
function loginclick()
{
		$('#signup').hide();$('#signup_2').hide(); $('#login').show(); $('#forgot_password').hide();
	$("#login").addClass('animate__animated animate__flipInY');
}
function signup_1_click(){
    $('#signup_2').hide();$('#login').hide(); $('#signup').show();
    $("#signup").addClass('animate__animated animate__flipInY');
}
function signup_2_click()
{
    $('#signup').hide(); $('#signup_2').show();
    $("#signup_2").addClass('animate__animated animate__flipInY');
}
function forgot_click()
{
		$('#signup').hide(); $('#login').hide(); $('#forgot_password').show();
	$("#forgot_password").addClass('animate__animated animate__flipInY');
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

