
function CreateBlog() {
    $('.ajaxProgress').show();
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/blog/search2/",
        dataType: 'json',
        async: true,
        data: {
            'blogTitle': $('#blogTitle').val(),
            'csrfmiddlewaretoken':  $('input[name="csrfmiddlewaretoken"]').first().val()
        },
        success: function (json) {
            $('#output').html(json.message);
            $('.ajaxprogress').hide();
        }

    });
}







////$(function(){
//$(document).ready(function(){
//    $("#search3").keyup(function(){
//        $.ajax({
//            type: "POST",
//            url : "http://127.0.0.1:8000/blog/search2/" ,
//            data : {
//                'search_text': $('#search3').val(),
//                csrfmiddlewaretoken :'{{ csrf_token }}'
//            },
//            success: searchSuccess,
//            //success: function(){alert("Create User");}
//            dataType: 'html'
//        });
//    });
//
//});
//
//function searchSuccess(data, textStatus, jqXHR)
//{
//    $('#search-results').html(data)
//}
