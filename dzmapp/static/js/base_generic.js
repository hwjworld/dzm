$(document).ready(function(){
     $.ajaxSetup({
        async : false
    });
    //init level1
    console.log("get map1");
    $.get('/map/level1/', {},function (data,status){
        $.each(eval(data), function(key, val) {
            $("#map_select_level1").append("<option value='"+val+"'>"+val+"</option>");
        });
      console.log("get map1 finish");
      }
    );
    console.log("bind map1 change");
    $("#map_select_level1").change(changemap1);
    console.log("bind map2 change");
    $("#map_select_level2").change(changemap2);
    console.log("start change map1");
    //changemap1();
    console.log("end change map1");

    console.log("start change 2 default");
    //change2defaultmap1();
    console.log("end change 2 default");



function changemap1(){
        console.log("start get map1 levels");
        $.get('/map/level1/'+$("#map_select_level1").val()+"/level2/", {},function (data1,status){
            $("#map_select_level2").empty();
            $.each(eval(data1), function(key, val) {
                $("#map_select_level2").append("<option value='"+val[1]+"'>"+val[0]+"</option>");
            });
        });
        console.log("finish get map1 levels");
        console.log("start change map2");
        changemap2();
        console.log("end change map2");
}

function changemap2(){
    /*
    $.get('/map/level1/'+$("#map_select_level1").val()+"/level2/"+$("#map_select_level2").val(), {},function (data,status){
        remove_linelays();
        map.panTo(addPolyline(data));
    });
    */
    console.log("move bmap to map2");
    remove_linelays();
    alert(map);
    var tmp = addPolyline($("#map_select_level2").val());
    moveToPoint(tmp);
    console.log("end move bmap to map2");
}
function change2defaultmap1(){
    alert("2-1");
    if(typeof(defaultlevel1)!="undefined"){
        $("#map_select_level1").val(defaultlevel1);
        $('#map_select_level1').change();
        change2defaultmap2();
    }
}
function change2defaultmap2(){
    if(typeof(defaultlevel2)!="undefined"){
        $("#map_select_level2").find("option").each(function(){
            if($(this).text()==defaultlevel2){
                $("#map_select_level2").val($(this).val());
            }
        });
        $("#map_select_level2").change();
    }
}


});