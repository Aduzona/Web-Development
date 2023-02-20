//https://youtu.be/6qIEyC23PSM

$(document).ready(() => {
    $('.menu').on('mouseenter',()=>{
      $('.nav-menu').show();
    }).on('mouseleave',()=>{
      $('.nav-menu').hide();
    })
    //Mouse hover
    $('.btn').on('mouseenter',event=>{
      $(event.currentTarget).addClass('btn-hover')
    }).on('mouseleave',event=>{
      $(event.currentTarget).removeClass('btn-hover')
    });
    $('.postText').on('keyup',event=>{
      $('.postText').focus();
      let post=$(event.currentTarget).val()
      let remaining=140-post.length;
      $('.characters').html(remaining);
  
      if(remaining<=0){
        $('.wordcount').addClass('red');
      }else{
        $('.wordcount').removeClass('red');
      }
     
      
    });
    
  }); 
  