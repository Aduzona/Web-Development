$(document).ready(() =>{
    $('#cart').on('click',()=>{
      $('#cartMenu').show();
    });
    $('#account').on('click',()=>{
      $('#accountMenu').show();
    });
    $('#help').on('click',()=>{
      $('#helpMenu').show();
    });
    $('.dropdown-menu').on('mouseleave',()=>{
      $('.dropdown-menu').hide();
    });
})
// REFERENCE
//https://youtu.be/Fj2j643chAw