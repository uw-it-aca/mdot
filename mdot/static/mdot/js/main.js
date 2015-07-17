// document.ready shorthand
$(function() {
    
    // initiate the slide
 	$( '#feature_slider' ).sliderPro({
     	width : '100%',
     	autoHeight : true,
     	buttons : false,
     	autoplay : false,
     	
     	thumbnailHeight : 'auto',
     	thumbnailWidth : 70,
     	
    });
 	
 	// handle what happens when a slide is shown
 	$( '#feature_slider' ).on( 'gotoSlideComplete', function( event ) {
        console.log("you are on slide: " + event.index);
    })


});

 
