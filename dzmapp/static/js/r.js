function saveform_submit(){
    sd = $("#visit_date").val().replace(/-/gm,'');
    $("#record_form input[name='map_level1']").val($("#map_level1").val());
    $("#record_form input[name='map_level2']").val($("#map_level2").val());
    if($("#record_form input[name='bmapx']").val() == "" || $("#record_form input[name='bmapy']").val() == "" ){
        alert("请在左侧地图上点击地址");
        return;
    }
    record_form.submit();
}
$(document).ready(function(){
    $( "#visit_date" ).datepicker({ dateFormat: "yy-mm-dd" });
});