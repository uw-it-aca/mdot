// document.ready shorthand
$(function() {
    
    // initiate the slider
 	/*
 	$( '#feature_slider' ).sliderPro({
     	width : '100%',
     	autoHeight : true,
     	buttons : false,
     	autoplay : false,
     	
     	slideDistance : 0,
     	thumbnailHeight : 'auto',
     	thumbnailWidth : 85,
     	//thumbnailTouchSwipe : false,
     	
    });
 	
 	// handle what happens when a slide is shown
 	$( '#feature_slider' ).on( 'gotoSlideComplete', function( event ) {
        console.log("you are on slide: " + event.index);
    })
    */
    
    $(window).scroll(function(){
        
        var nav_container = $(".sp-thumbnails-container");
        var nav_header = $(".mdot-navbar").height();
        var user_header = $(".mdot-user").height();    
        var feaure_header = $(".mdot-feature").height() - 40;
        var sticky_point = nav_header + user_header + feaure_header;
        var page_top = $(window).scrollTop() + nav_header;
        
        /*
        console.log("scrolltop: " + page_top);
        console.log("resourcetop: " + stuck_location);
        console.log("navheight: " + nav_header);
        console.log("userheight: " + user_header);
        console.log("fetheight: " + feaure_header);
        */
                
        if( page_top > sticky_point) {
            nav_container.addClass("stuck");
            $("#nav_back").addClass("stuck");
            $("#nav_shim").show();
        }
        else {
            nav_container.removeClass("stuck");
            $("#nav_back").removeClass("stuck");
            $("#nav_shim").hide();
        }
    });



});