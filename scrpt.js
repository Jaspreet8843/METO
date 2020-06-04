$(window).resize(function(){
   console.log('resize called');
   var width = $(window).width();
 
   if(width <1024){

   	$('fspace').addClass('w-100');
   	console.log(width);
   }
   
})
.resize();//trigger the resize event on page load.