jQuery(document).ready(function($){
    let url = window.location.pathname;
    $('.nav a[href="'+url+'"]').parent().addClass('active');
});
