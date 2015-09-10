// document.ready shorthand
$(function() {
    
    console.log("ready!");
    
    // truncate feature descriptions
    $('.mdot-resource-desc').succinct({
        size: 65
    });
    
});