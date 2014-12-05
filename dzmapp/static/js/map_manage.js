
//show current zoom in zoom input text
$(document).ready(function(){
    function setCenterText(){
        center = map.getCenter();
        $("#mapaddform input[name='mapx']").val(center.lng);
        $("#mapaddform input[name='mapy']").val(center.lat);
    }
    $("#mapaddform input[name='zoom']").val(map.getZoom());
    map.addEventListener("zoomend",function(e){
        $("#mapaddform input[name='zoom']").val(map.getZoom());
        setCenterText();
    });
    map.addEventListener("moveend",setCenterText);
    $("#mapaddform input[name='polyline']").change(function(e){
        clearAll();
        map.panTo(addPolyline($(this).val()));
    });
    $(".mapslist").change(function(e){
        clearAll();
        map.panTo(addPolyline($(this).children("option:selected").val()));
    });

});
//TOTO check valid
function saveMap(){
    form = $("#mapaddform");
    $.post('/map/s', {
        level1:form.children("[name='level1']").val(),
        level2 : form.children("[name='level2']").val(),
        polyline : form.children("[name='polyline']").val(),
        zoom : form.children("[name='zoom']").val(),
        mapx : form.children("[name='mapx']").val(),
        mapy : form.children("[name='mapy']").val()
      },function (data,status){
        alert(data);
        if(status == 200){
            clearform("mapdeleteform");
        }
      }
    );
}
function deleteMap(){
    form = $("#mapdeleteform");
    $.post('/map/d', {
        level1:form.children("[name='level1']").val(),
        level2 : form.children("[name='level2']").val()
      },function (data,status){
        alert(data);
        if(status == 200){
            clearform("mapdeleteform");
        }
      }
    );
}
function clearform(formid){
    $("#"+formid).children("input").val();
}
