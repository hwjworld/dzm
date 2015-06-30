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
$(document).ready(function(){
    $.datepicker.setDefaults({
    dateFormat: "yy-mm-dd"
    });
    $( "#visit_date" ).val(formatDate(now));
});