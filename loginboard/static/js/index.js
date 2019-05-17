$(function(){
    $('button.login').click(function(){
        //부트박스 띄우기
        alert('login');
    });
    $('#registerModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget) // Button that triggered the modal
        var modal = $(this)
    })
    function alert_error(error){
        alert(error)
    }
})