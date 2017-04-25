function saveform_submit(){
    sd = $("#visit_date").val().replace(/-/gm,'');
    $("#record_form input[name='map_level1']").val($("#map_select_level1").val());
    $("#record_form input[name='map_level2']").val($("#map_select_level2").find("option:selected").text());
    if($("#record_form input[name='bmapx']").val() == "" || $("#record_form input[name='bmapy']").val() == "" ){
        alert("请在左侧地图上点击地址");
        return;
    }
    if($("#record_form input[name='num']").val() == "" || $("#record_form input[name='num']").val() == "" ){
        alert("请填写门牌");
        return;
    }
    record_form.submit();
}
function setShowOffRecord(show){
    if(show){
        $("#showoff90dayrecord_btn").text("显示90天记录");
    }else{
        $("#showoff90dayrecord_btn").text("隐藏90天记录");
    }
}
$(document).ready(function(){
    $.datepicker.setDefaults({
    dateFormat: "yy-mm-dd"
    });
    $( "#visit_date" ).val(formatDate(now));
    showoff90dayrecord = false;
    $("#showoff90dayrecord_btn").click(function(){
        if(showoff90dayrecord == false){
            addAllVisitedRecordToMap();
            showoff90dayrecord = true;
            setShowOffRecord(false);
        }else{
            hideAllVisitedRecordFromMap();
            showoff90dayrecord = false;
            setShowOffRecord(true);
        }
    });
});