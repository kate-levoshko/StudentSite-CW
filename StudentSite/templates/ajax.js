/**
 * Created by Levoshko on 12/15/2016.
 */


$(document).ready(function(){
              $("#searchButton").click(function(){
                  btn = $(this);
                  inp = $("#search");
            $.ajax({type: "GET", url:"/search", data: {search: inp.val(), xhr: true}, success: function(result){

                var materials = jQuery.parseJSON(result);
                $(".addMaterial").remove();
                for (i in materials){
                    $("#addMaterial").append('<div class="post addMaterial"> <h6><a href="/materials/get/' +  materials[i].id + '/">' + materials[i].upload_material + ' </a></h6> </div>');
                };
            }});
        });
    });

          function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
        $(document).ready(function(){
            $(".add").click(function(){
                btn = $(this);
               alert(btn.attr("value"));
                $.ajax({type: "POST", url:"/bucket", data: {add: btn.attr("value"), xhr: true}, success: function(result){

                    if(result.status !== "ok"){
                        alert(result.status);
                    }
                    else{
                       btn.hide();
                    };
            }});
        });
    });