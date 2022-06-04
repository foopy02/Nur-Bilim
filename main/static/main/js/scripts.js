var owl = $('.owl-carousel');
owl.owlCarousel({
    items:1,
    loop:true,
    margin:10,
    autoplay:true,
    autoplayTimeout:1000,
    autoplayHoverPause:false
});
$('.play').on('click',function(){
    owl.trigger('play.owl.autoplay',[1000])
})
$('.stop').on('click',function(){
    owl.trigger('stop.owl.autoplay')
})


function burger(){
    left_block = document.getElementById("left_block")
    left_block.classList.toggle("width300");
}


function user(){
    opportunities = document.getElementById("user_menu_list")
    opportunities.classList.toggle("displayF")
}

var modals = document.getElementsByClassName("modal");

var btn = document.getElementById("myBtn");

var span = document.getElementsByClassName("close");

function show_modal(button){
    var modal = button.nextElementSibling;
    modal.style.display = "block";
}

function close_modal(close_button){
    var modal = close_button.parentElement.parentElement
    modal.style.display = "none";
}

window.onclick = function(event) {
        if (event.target == element) {
            element.style.display = "none";
          }

}   

window.onload = function() {
    var duration = 2000; //2 seconds
    setTimeout(function () { $('#alert').hide(); }, duration);
};