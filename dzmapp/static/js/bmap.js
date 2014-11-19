
function setBmapXY(x,y){
    $("#record_form input[name='bmapx']").val(x);
    $("#record_form input[name='bmapy']").val(y);
}

	var map = new BMap.Map("mapbody");
	var point = new BMap.Point(116.404, 39.915);
	map.centerAndZoom(point, 17);
	map.enableScrollWheelZoom()
	var data_info = [[116.417854,39.921988,"地址：北京市东城区王府井大街88号乐天银泰百货八层"],
					 [116.406605,39.921585,"地址：北京市东城区东华门大街"],
					 [116.412222,39.912345,"地址：北京市东城区正义路甲5号"]
					];
	var opts = {
				width : 250,     //
				height: 80,     // 信息窗口高度
				title : "信息窗口" , // 信息窗口标题
				enableMessage:true//设置允许信息窗发送短息
			   };
	for(var i=0;i<data_info.length;i++){
		var marker = new BMap.Marker(new BMap.Point(data_info[i][0],data_info[i][1]));  // 创建标注
		var content = data_info[i][2];
		map.addOverlay(marker);               // 将标注添加到地图中
		addClickHandler(content,marker);
	}
	function addClickHandler(content,marker){
		marker.addEventListener("click",function(e){
			openInfo(content,e)}
		);
	}
	function openInfo(content,e){
		var p = e.target;
		var point = new BMap.Point(p.getPosition().lng, p.getPosition().lat);
		var infoWindow = new BMap.InfoWindow(content,opts);  // 创建信息窗口对象
		map.openInfoWindow(infoWindow,point); //开启信息窗口
	}
	var overlays = [];
	function clearAll() {
		for(var i = 0; i < overlays.length; i++){
            map.removeOverlay(overlays[i]);
        }
        overlays.length = 0
    }
	map.addEventListener("click",function(e){
	    setPointOnMap(e.point.lng,e.point.lat);
	    setBmapXY(e.point.lng,e.point.lat);
	});
	function setPointOnMap(x,y){
	    clearAll();
        var marker = new BMap.Marker(new BMap.Point(x,y));
        map.addOverlay(marker);
	    map.panTo(new BMap.Point(x,y));
        overlays[0] = marker;
	}

    function changemap(e){
        x=$("#selectedmap option:selected").attr("mapx");
        y=$("#selectedmap option:selected").attr("mapy");
	    map.panTo(new BMap.Point(x,y));
    }