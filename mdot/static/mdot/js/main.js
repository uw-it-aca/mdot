// document.ready shorthand
$(function() {
    
    // initiate the slide
 	$( '#feature_slider' ).sliderPro({
     	width : '100%',
     	autoHeight : true,
     	buttons : false,
     	autoplay : false,
     	
     	slideDistance : 0,
     	thumbnailHeight : 'auto',
     	thumbnailWidth : 80,
     	
    });
 	
 	// handle what happens when a slide is shown
 	$( '#feature_slider' ).on( 'gotoSlideComplete', function( event ) {
        console.log("you are on slide: " + event.index);
    })
    
    var static_header = $(".sp-thumbnails-container");
    var stickyRibbonTop = $('.mdot-resources').offset().top + 270;
          
    $(window).scroll(function(){
        if( $(window).scrollTop() > stickyRibbonTop ) {
            static_header.addClass("stuuuuuuuuuuck");
            $("#thumb_back").addClass("stuuuuuuuuuuck");
        }
        else {
            static_header.removeClass("stuuuuuuuuuuck");
            $("#thumb_back").removeClass("stuuuuuuuuuuck");
        }
    });


    

});