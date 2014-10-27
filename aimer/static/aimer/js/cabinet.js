var addNewAim = function (event) {
    
    console.log("Add new aim!");
    //alert ("get route type: " + route_type)
    $.ajax({
      route_type: "get",
      url: route_type,
      data: {"route_type":route_type,'category_type':category},
      success : function(data){
               $('#thumbnail_wrapper').html(data);
             }
    })

}

$('#add_button').click(function() {
    console.log("Add new aim!");
    //alert ("get route type: " + route_type)
    $.ajax({
      route_type: "get",
      // url: route_type,
      // data: {"route_type":route_type,'category_type':category},
      // success : function(data){
      //          $('#thumbnail_wrapper').html(data);
      //        }
    })

})


$('#show_buttons').click(function() {
    console.log("Show aims!");
    //alert ("get route type: " + route_type)
    $.ajax({
      route_type: "get",
      // url: route_type,
      // data: {"route_type":route_type,'category_type':category},
      // success : function(data){
      //          $('#thumbnail_wrapper').html(data);
      //        }
    })

})