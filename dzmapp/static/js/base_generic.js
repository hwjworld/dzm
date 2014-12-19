$(document).ready(function(){

    //init level1
    $.get('/map/level1/', {},function (data,status){
        $.each(eval(data), function(key, val) {
            $("#map_select_level1").append("<option value='"+val+"'>"+val+"</option>");
        });
        $("#map_select_level1").change(changemap1);
        changemap1();
      }
    );
    $("#map_select_level2").change(changemap2);

});
function changemap1(){
        $.get('/map/level1/'+$("#map_select_level1").val()+"/level2/", {},function (data1,status){
            $("#map_select_level2").empty();
            $.each(eval(data1), function(key, val) {
                $("#map_select_level2").append("<option value='"+val[1]+"'>"+val[0]+"</option>");
            });
            changemap2();
        });
}

function changemap2(){
    /*
    $.get('/map/level1/'+$("#map_select_level1").val()+"/level2/"+$("#map_select_level2").val(), {},function (data,status){
        remove_linelays();
        map.panTo(addPolyline(data));
    });
    */
    remove_linelays();
    map.panTo(addPolyline($("#map_select_level2").val()));
}