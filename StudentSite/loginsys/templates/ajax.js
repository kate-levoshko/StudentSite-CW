/**
 * Created by Levoshko on 12/15/2016.
 */


$(document).ready(function(){
        $("#searchAddButton").click(function(){
            btn = $(this);
            inp = $("#searchAdd");
            $.ajax({type: "GET", data: {search: inp.val(), xhr: true}, success: function(result){
                var audios = jQuery.parseJSON(result);
                $(".addAudioPost").remove();
                for (i in audios){
                    $("#addAudioModal").prepend('<div class="post addAudioPost"><h4 style="display: inline-block;"><a href="/author/' + audios[i].author.id + '">' + audios[i].author.name + '</a> - ' + audios[i].name + '</h4><button class="btn pull-right addAudioInInput" type="submit" value="' + audios[i].id + '">+</button><hr></div>');
                };
                audioBtnEvent();
            }});
        });
    });