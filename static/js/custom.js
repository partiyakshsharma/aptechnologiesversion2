/* -------------------------------------------------------------------
 * Template         : Rundal - Modern Multi-Purpose HTML5 Template
 * Author           : SeparateWeb
 * File             : Custom.js - main template custom js file
------------------------------------------------------------------- */
(function ($) {
  "use strict";


//page loader
$(window).on('load', function() {
  $('.preloader').addClass('page-loaded');
});
  
 //Sticky Header 
  function updateScroll() {
    if ($(window).scrollTop() >= 80) {
      $(".rundal-header").addClass('sticky');
    } else {
      $(".rundal-header").removeClass("sticky");
    }
  }
  $(function () {
    $(window).scroll(updateScroll);
    updateScroll();
  });

//home slider
$(window).on("load", function () {
  var owl = $('.review-slider');
  owl.owlCarousel({
    items: 1,      
    nav: false,    
    dots: false,
    autoplay: false,
    loop: true,     
    autoplayHoverPause: true,     
    smartSpeed: 1000,  
    mouseDrag: false,    
  });
  // Custom html Button
  $('.customNextBtn').click(function() {
    owl.trigger('next.owl.carousel');
  });
  $('.customPreviousBtn').click(function() {
    owl.trigger('prev.owl.carousel');
  });  
});


//hero logo slider
$(window).on("load", function () {
  $('.logo---set').owlCarousel({        
      nav: false,     
      dots: false,
      autoplay: true,
      loop: true,   
      center: false,   
      margin: 30,
      autoplayTimeout: 2500,
      autoplayHoverPause: true,
      autoHeight: true,
      smartSpeed: 2000,   
     responsive: {
      0: {
        items: 2
      },
      520: {
        items: 3
      },
      768: {
        items: 4
      },
      1200: {
        items: 5
      },
      1400: {
        items: 5
      },
      1600: {
        items: 6
      },
    }
  });
});


//testimonial slider
$(window).on("load", function () {
  $('.testimonial-slider--').owlCarousel({        
      nav: false,     
      dots: false,
      autoplay: true,
      loop: true,   
      center: false,   
      margin: 30,
      autoplayTimeout: 3000,
      autoplayHoverPause: true,
      autoHeight: true,
      smartSpeed: 2000,   
     responsive: {
      0: {
        items: 1
      },
      520: {
        items: 1
      },
      768: {
        items: 2
      },
      1200: {
        items: 3
      },
      1400: {
        items: 3
      },
      1600: {
        items: 3
      },
    }
  });
});


//technology slider
$(window).on("load", function () {
  $('.technology-slider').owlCarousel({        
      nav: false,     
      dots: false,
      autoplay: true,
      loop: true,   
      center: false,   
      margin: 30,
      autoplayTimeout: 3000,
      autoplayHoverPause: true,
      autoHeight: true,
      smartSpeed: 2000,   
     responsive: {
      0: {
        items: 3
      },
      520: {
        items: 3
      },
      768: {
        items: 5
      },
      1200: {
        items: 8
      },
      1400: {
        items: 8
      },
      1600: {
        items: 10
      },
    }
  });
});


//about us page 2 office view slider
$(window).on("load", function () {
  $('.gallery-slider').owlCarousel({        
      nav: false,     
      dots: false,
      autoplay: true,
      loop: true,   
      center: false,   
      margin: 30,
      autoplayTimeout: 3000,
      autoplayHoverPause: true,
      autoHeight: true,
      smartSpeed: 2000,   
     responsive: {
      0: {
        items: 2
      },
      520: {
        items: 2
      },
      768: {
        items: 3
      },
      1200: {
        items: 3
      },
      1400: {
        items: 3
      },
      1600: {
        items: 3
      },
    }
  });
});


//Background image ------------------
$("[data-background]").each(function () {
  $(this).css("background-image", "url(" + $(this).attr("data-background") + ")")
})


//bootstrap popover
document.querySelectorAll('[data-bs-toggle="popover"]')
.forEach(popover => {
  new bootstrap.Popover(popover)
})

//Video magnificPopup
$('.video-play').magnificPopup({
  type: 'iframe',
  mainClass: 'mfp-fade',
  removalDelay: 160,
});


//gallery img and video
$('.gallery').each(function() {   
	$(this).magnificPopup({
		delegate: 'a',
		type: 'image',
    easing: 'ease-in-out', 
		gallery: {
			enabled:true
		},
    zoom: {
      enabled: true,   
      duration: 300, 
      easing: 'ease-in-out',      
      }
	});
});

//back to top
var progressPath = document.querySelector('.progress-wrap path');
var pathLength = progressPath.getTotalLength();
progressPath.style.transition = progressPath.style.WebkitTransition = 'none';
progressPath.style.strokeDasharray = pathLength + ' ' + pathLength;
progressPath.style.strokeDashoffset = pathLength;
progressPath.getBoundingClientRect();
progressPath.style.transition = progressPath.style.WebkitTransition = 'stroke-dashoffset 10ms linear';		
var updateProgress = function () {
  var scroll = $(window).scrollTop();
  var height = $(document).height() - $(window).height();
  var progress = pathLength - (scroll * pathLength / height);
  progressPath.style.strokeDashoffset = progress;}
updateProgress();
$(window).scroll(updateProgress);	
var offset = 50;
var duration = 550;
jQuery(window).on('scroll', function() {
  if (jQuery(this).scrollTop() > offset) {
    jQuery('.progress-wrap').addClass('active-progress');
  } else {
    jQuery('.progress-wrap').removeClass('active-progress');
  } });				
jQuery('.progress-wrap').on('click', function(event) {
  event.preventDefault();
  jQuery('html, body').animate({scrollTop: 0}, duration);
  return false;})	


//separateweb collapsible footer
var coll = document.getElementsByClassName("collapsible");
var i;
for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.maxHeight){
      content.style.maxHeight = null;
    } else {
      content.style.maxHeight = content.scrollHeight + "px";
    } 
  });
}

//Contact Us Address Block
$(document).ready(function() {
  $("#address-1").click(function() {
    $("#addressblock-1").show();
    $("#addressblock-2").hide();
    $("#addressblock-3").hide();
    $("#addressblock-4").hide();
  });

  $("#address-2").click(function() {
    $("#addressblock-2").show();
    $("#addressblock-1").hide();
    $("#addressblock-3").hide();
    $("#addressblock-4").hide();
  });

  $("#address-3").click(function() {
    $("#addressblock-3").show();
    $("#addressblock-1").hide();
    $("#addressblock-2").hide();
    $("#addressblock-4").hide();
  });

  $("#address-4").click(function() {
    $("#addressblock-4").show();
    $("#addressblock-1").hide();
    $("#addressblock-2").hide();
    $("#addressblock-3").hide();
  });    
});

 // initialize scrollCue.js
 scrollCue.init({
  duration : 800,   
  percentage :0.85
});


  
})(jQuery);






      
      