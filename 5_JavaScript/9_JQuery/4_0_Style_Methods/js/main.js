$(document).ready(() => {
 
    $('.login-button').on('click', () => {
      $('.login-form').toggle();
    });
    
    $('.menu-button').on('click', () => {
        $('.nav-menu').toggleClass('hide');
        $('.menu-button').toggleClass('button-active');
    
      })
      //or write these 2 jquery function handlers below.
    $('.menu-button').on('mouseenter', () => {
      $('.nav-menu').show();
      /*
      $('.menu-button').css({
        color:'#C3FF00',
        backgroundColor:'#535353'
        });
        */
  
        /*
      $('.menu-button').animate({
        color:'#C3FF00',
        backgroundColor:'#535353',
        fontSize:'24px'
        },200);
        */
  
        /*
        If you navigate to css/styles.css, there’s a class named .button-active, which defines the text color and background color of an element. Use the .addClass() method to add button-active to the .menu-button element when it’s moused over.
        */
        $('.menu-button').addClass('button-active');
        $('.nav-menu').removeClass('hide');
    })
    
    $('.nav-menu').on('mouseleave', () => {
      $('.nav-menu').hide();
      //$('.menu-button').css('color','#EFEFEF');
  
      /*
      $('.menu-button').css({
        color:'#EFEFEF',
        backgroundColor:'#303030'});
        */
      $('.menu-button').animate({
        color:'#EFEFEF',
        backgroundColor:'#303030',
        fontSize:'18px'
        },200);
  
    })
    
  
  
    
  }); 
  