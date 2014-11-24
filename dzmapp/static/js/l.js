function seachform_submit(){
    sd = $("#start_date").val().replace(/-/gm,'');
    ed = $("#end_date").val().replace(/-/gm,'');
    if(sd == "" || ed == ""){
        alert("请选择 开始 和 结束 日期.");
        return;
    }
    window.location.href = "/l/" + sd + "-" + ed;
}

function thismonth_submit(){
    sd = $("#start_date").val(getMonthStartDate()).val().replace(/-/gm,'');
    ed = $("#end_date").val(getMonthEndDate()).val().replace(/-/gm,'');
    window.location.href = "/l/" + sd + "-" + ed;
}
function lastmonth_submit(){
    sd = $("#start_date").val(getLastMonthStartDate()).val().replace(/-/gm,'');
    ed = $("#end_date").val(getLastMonthEndDate()).val().replace(/-/gm,'');
    window.location.href = "/l/" + sd + "-" + ed;
}

$(document).ready(function(){
    $( "#start_date" ).datepicker({ dateFormat: "yy-mm-dd" });
    $( "#end_date" ).datepicker({ dateFormat: "yy-mm-dd" });
    $("[name='recordtr']").mouseover(function(){$(this).css("background","#FFD2D2");}).mouseout(function(){$(this).css("background","");}).click(function(){
        setPointOnMap($(this).attr("mapx"),$(this).attr("mapy"))
    });
});