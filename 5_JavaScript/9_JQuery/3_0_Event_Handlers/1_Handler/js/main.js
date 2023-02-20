$(document).ready(() => {
    //click event
    $('.login-button').on('click', () => {
      $('.login-form').show();
    });
    //on mouseenter event
    $('.menu-button').on('mouseenter',()=>{
      $('.nav-menu').show()
    });
    // on mouseleave
    $('.nav-menu').on('mouseleave', () => {
      $('.nav-menu').hide()
    });

    /*
    //Chaining Events
    $('.product-photo').on('mouseenter',()=>{
      $('.product-photo').addClass('photo-active')
    }).on('mouseleave',()=>{
      $('.product-photo').removeClass('photo-active')
    });
    */

    //currentTarget
    $('.product-photo').on('mouseenter', event => {
      $(event.currentTarget).addClass('photo-active')
    }).on('mouseleave', event => {
      $(event.currentTarget).removeClass('photo-active')
    })
  }); 
  /*
Reference
http://jqapi.com/
*/