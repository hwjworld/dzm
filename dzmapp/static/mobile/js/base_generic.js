
    //init level1
    //console.log("get map1");
function changemap(){
     $.ajaxSetup({
        async : false
    });
    $.get('/map/level1/', {},function (data,status){
        $.each(eval(data), function(key, val) {
            $("#map_select_level1").append("<option value='"+val+"'>"+val+"</option>");
        });
      //console.log("get map1 finish");
      }
    );
    //console.log("bind map1 change");
    $("#map_select_level1").change(changemap1);
    //console.log("bind map2 change");
    $("#map_select_level2").change(changemap2);

    //console.log("start change 2 default");
    //change2defaultmap1();
    //console.log("end change 2 default");

}


function changemap1(){
        if(defaultlevel1!=""){
            $("#map_select_level1").val(defaultlevel1).selectmenu("refresh");
            defaultlevel1 = "";
        }
        //console.log("start get map1 levels");
        $.get('/map/level1/'+$("#map_select_level1").val()+"/level2/", {},function (data1,status){
            $("#map_select_level2").empty();
            $.each(eval(data1), function(key, val) {
                $("#map_select_level2").append("<option value='"+val[1]+"'>"+val[0]+"</option>");
            });
        });
        //console.log("finish get map1 levels");
        changemap2();
}

function changemap2(){
    /*
    $.get('/map/level1/'+$("#map_select_level1").val()+"/level2/"+$("#map_select_level2").val(), {},function (data,status){
        remove_linelays();
        map.panTo(addPolyline(data));
    });
    */

    if(defaultlevel2 != ""){
        $("#map_select_level2").children("option").each(function(){
            //console.log("===");
            if($(this).text()==defaultlevel2){
                //console.log("text -- "+$(this).text());
                //console.log("defaultlevel2 -- "+defaultlevel2);
                $("#map_select_level2").val($(this).val());
            }
        });
        $("#map_select_level2").selectmenu("refresh");
        defaultlevel2 = "";
    }

    //console.log("move bmap to map2");
    //暂停一秒，等map加载
    setTimeout(function(){
        remove_linelays();
        var tmp = addPolyline($("#map_select_level2").val());
        moveToPoint(tmp);
        //console.log("end move bmap to map2");
    },1000);
}


function get_current_territory_l1(){
    return $("#map_select_level1").val();
}
function get_current_territory_l2(){
    return $("#map_select_level2").find("option:selected").text();
}

function m_record_url(){
    window.location.href="/m?l1="+get_current_territory_l1()+"&l2="+get_current_territory_l2();
}
function ml_record_url(){
    window.location.href="/ml?l1="+get_current_territory_l1()+"&l2="+get_current_territory_l2();
}