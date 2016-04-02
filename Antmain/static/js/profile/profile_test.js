    //For doing AJAX post
     $("#submit3").click(function(e) {

     e.preventDefault();


     var name = $('#name').val();

     var nickname = $('#nickname').val();

     var email = $('#email').val();



    //This is the Ajax post.Observe carefully. It is nothing but details of where_to_post,what_to_post

     $.ajax({
             url : window.location.href, // the endpoint,commonly same url
             type : "POST", // http method
             data : {
             name : name,
             nickname : nickname,
             email : email,
                 new_sub : '1'
     }, // data sent with the post request

     // handle a successful response
     success : function(json) {
          console.log(json); // another sanity check
          //On success show the data posted to server as a message
          alert('Hi '+json['name'] +'!.' + ' You have entered password:'+      json['nickname']);
     },

     // handle a non-successful response
     error : function(xhr,errmsg,err) {
     console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
     }
     });
    });

    //
    // $("#submit2").click(function(e) {
    //
    // e.preventDefault();
    //
    // var csrftoken = getCookie('csrftoken');
    //
    // var testtext = $('#testtext').val();
    //
    // var testnumber = $('#testnumber').val();
    //
    ////This is the Ajax post.Observe carefully. It is nothing but details of where_to_post,what_to_post
    //
    // $.ajax({
    //         url : window.location.href, // the endpoint,commonly same url
    //         type : "POST", // http method
    //         data : { csrfmiddlewaretoken : csrftoken,
    //         testtext : testtext,
    //         testnumber : testnumber,
    //             new_unsub : '1'
    //
    // }, // data sent with the post request
    //
    // // handle a successful response
    // success : function(json) {
    //      console.log(json); // another sanity check
    //      //On success show the data posted to server as a message
    //      alert('Hi2 '+json['testtext'] +'!.' + ' You have entered password2:'+      json['testnumber']);
    // },
    //
    // // handle a non-successful response
    // error : function(xhr,errmsg,err) {
    // console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    // }
    // });
    //});
    //
