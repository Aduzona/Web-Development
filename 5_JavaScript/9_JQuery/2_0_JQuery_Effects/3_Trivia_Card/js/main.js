//https://youtu.be/-T_T4NRwrWQ
$(document).ready(() =>{
    $('.hint-box').on('click',()=>{
      $('.hint').slideToggle(1000)
    });
    $('.wrong-answer-one').on('click',()=>{
      $('.wrong-test-one').fadeOut('slow');
      $('.frown').show();
    });
    $('.wrong-answer-two').on('click',()=>{
      $('.wrong-test-two').fadeOut('slow');
      $('.frown').show();
    });
    $('.wrong-answer-three').on('click',()=>{
      $('.wrong-test-three').fadeOut('slow');
      $('.frown').show();
    });
  
    $('.correct-answer').on('click',()=>{
      $('.frown').hide();
      $('.smiley').show();
      $('.wrong-answer-one').fadeOut('slow');
      $('.wrong-answer-two').fadeOut('slow');
      $('.wrong-answer-three').fadeOut('slow');
    });
  });
  //$('p').fadeOut(100)