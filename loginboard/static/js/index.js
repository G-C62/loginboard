$(function(){
    is_check = false;



    //처음 회원가입버튼 클릭시
    $('button[data-target="#registerModal"]').on('click',function(event){
        $('#register-form')[0].reset();
        is_check = false;
         $('input[name=username]').attr('readOnly',false);
    })

    //회원가입 모달 이벤트
    $('#registerModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget); // Button that triggered the modal
        var modal = $(this);
    })

    //로그인 모달 이벤트
    $('#loginModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget); // Button that triggered the modal
        var modal = $(this);
    })

    //error alert이벤트
    function alert_error(error){
        bootbox.alert(error)
    }

    //submit전 유효성검사 이벤트
    $('#register-form').on('submit',function(event){
        username = $('input[name=username]').val();
        password = $('input[name=password]').val();
        checkpassword = $('input[name=checkpassword]').val();

        is_valid = false;
        if(!is_check){
            is_valid = false;
        }
        else if(username.length < 4 || username.length > 50){
            is_valid = false;
        }
        else if((password !== checkpassword) || (password.length < 3)){
            is_valid = false;
        }
        else{
            is_valid = true;
        }

        //alert메시지 출력
        if(is_valid){
            bootbox.alert('전송되었습니다.');
            return;
        }
        bootbox.alert('전송조건이 부족합니다.');
        event.preventDefault();

    })


    //중복검사 버튼 이벤트
    $('#register-checkname').on('click',function(event){
        if ($('input[name=username]').val() != '') {
        $.ajax({
        	url         : '/user/check_name'
           ,type        : 'POST'
           ,cache       : false
           ,data        : JSON.stringify({
        	   username: $('input[name=username]').val()
             })
           ,contentType : 'application/json; charset=utf-8'
           ,dataType    : 'json'
           ,success     : function(data) {
        	   username = $('input[name=username]').val();
        	   if (data.result) {

                   $('#registerModal').modal('hide');

                   bootbox.alert(username + '는 사용 가능한 아이디입니다.', function() {
                       $('#registerModal').modal('show');
                       is_check = true
                       $('input[name=username]').attr('readOnly',true);
                   });
        	   } else {
        	       $('#registerModal').modal('hide');

                   bootbox.alert(username + '는 이미 사용중입니다. 다른 아이디를 사용하세요.', function() {
                       $('#registerModal').modal('show');
                	   $('input[name=username]').val('');
                       $('input[name=username]').focus().select();
                   });
        	   }
             }
           ,error: function(result) {
               $('#registerModal').modal('hide');
        	   bootbox.alert('통신에 오류가 발생했습니다. 잠시 후에 다시 사용하세요.', function() {
                   $('#registerModal').modal('show');
        	   });
           }
        });

      } else {
          $('#registerModal').modal('hide');
    	  bootbox.alert('사용자명을 넣어주세요.', function() {
              $('#registerModal').modal('show');
              $('input[name=username]').focus();
    	  });
      }
    })


})