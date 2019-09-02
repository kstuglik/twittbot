function scrollToBottom(){
  bottom = document.body.scrollHeight;
  current = window.innerHeight+ document.body.scrollTop;
  if((bottom-current) >0){
    window.scrollTo(0, bottom);
    setTimeout ( 'scrollToBottom()', 1000 );
  }
};
for(var i=0;i<10;i++)scrollToBottom();
