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
function frommonth_submit(){
    recent30daystart = new Date();
    recent30daystart.setDate(-(30-recent30daystart.getDate()));
    sd = $("#start_date").val(formatDate(recent30daystart)).val().replace(/-/gm,'');
    ed = $("#end_date").val(formatDate(now)).val().replace(/-/gm,'');
    window.location.href = "/l/" + sd + "-" + ed;
}
function csvexport_submit(){
    sd = $("#start_date").val().replace(/-/gm,'');
    ed = $("#end_date").val().replace(/-/gm,'');
    window.location.href = "/csv/" + sd + "-" + ed;
}


$(document).ready(function(){
    $( "#start_date" ).datepicker({ dateFormat: "yy-mm-dd" });
    $( "#end_date" ).datepicker({ dateFormat: "yy-mm-dd" });
    $("[name='recordtr']").mouseover(function(){$(this).css("background","#FFD2D2");}).mouseout(function(){$(this).css("background","");}).click(function(){
        moveToPoint($(this).attr("mapx"),$(this).attr("mapy"))
    });
});