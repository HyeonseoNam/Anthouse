// $(function() {
//   $("#stock_title").autocomplete({
//     source: "/sdata/api/stock/",
//     minLength: 2,
//   });
// });


$(document).ready(function() {
     $('#stock_title').tipuedrop({
          'mode': 'json',
          'contentLocation': '/sdata/api/stock/'
     });
});
