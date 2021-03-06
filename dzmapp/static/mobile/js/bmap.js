//this js for baidu map quick

	function clearAll() {
		remove_overlays();
        remove_linelays();
    }
	function remove_overlays2(){
		for(var i = 0; i < overlays2.length; i++){
            map.removeOverlay(overlays2[i]);
        }
        overlays2.length = 0;
	}

	function remove_overlays(){
		for(var i = 0; i < overlays.length; i++){
            map.removeOverlay(overlays[i]);
        }
        overlays.length = 0;
	}
	function remove_linelays(){
		for(var i = 0; i < linelays.length; i++){
            map.removeOverlay(linelays[i]);
        }
        linelays.length = 0;
	}


	function setPointOnMap(x,y){
	    remove_overlays2();
        var marker = new BMap.Marker(new BMap.Point(x,y));
        map.addOverlay(marker);
//	    map.panTo(new BMap.Point(x,y));
        overlays2[0] = marker;
        marker.enableDragging();
        marker.addEventListener("dragend", function(e){
            var pt = e.point;
            geoc.getLocation(pt, function(rs){
                var addComp = rs.addressComponents;
                $("#record_form input[name='street']").val(addComp.district + ", " + addComp.street+ ","+addComp.streetNumber);
            });
        });
	}

	function moveToPointWithXY(x,y){
	    //map.panTo(new BMap.Point(x,y));
	    moveToPoint(new BMap.Point(x,y));
	}
	function moveToPoint(point){
	    map.setCenter(point);
	}

    //------------添加折线---------------
    //return firstpoint
    function addPolyline(plPoints){
        ps = plPoints.split(",");
        var points = [];
        var fp = null;
        for(var j=0;j<ps.length;j++){
            ps[j] = ps[j].replace(/\"/g,"");
            var p1 = ps[j].split("|")[0];
            var p2 = ps[j].split("|")[1];
            if(j==0){fp = new BMap.Point(p1,p2);}
            points.push(new BMap.Point(p1,p2));
        }
        var line = new BMap.Polyline(eval(points),{strokeColor:"red", strokeWeight:2, strokeOpacity:0.5});
        map.addOverlay(line);
        linelays[linelays.length] = line;
        return fp;
	}
	function setBmapXY(x,y){
        $("#record_form input[name='bmapx']").val(x);
        $("#record_form input[name='bmapy']").val(y);
    }

    var opts = {
                width : 250,     //
                height: 80,     // 信息窗口高度
                title : "受访者信息" , // 信息窗口标题
                enableMessage:false//设置允许信息窗发送短息
               };
    //-----------points mark------------

	function addAllMarkPoints(data_info){
	    addAcceptMarkPoints(accept_data_info);
	    addRefuseMarkPoints(refuse_data_info);
	    addVisitedMarkPoints(visited_data_info);
	}

	function addAcceptMarkPoints(data_info){
	    addMarkPoints(data_info,1);
	}
	function addRefuseMarkPoints(data_info){
	    addMarkPoints(data_info,0);
	}
	function addVisitedMarkPoints(data_info){
	    addMarkPoints(data_info,2);
	}
	function addMarkPoints(data_info,response){
        var accept_icon = new BMap.Icon("http://api.map.baidu.com/img/markers.png", new BMap.Size(23, 25), {
            offset: new BMap.Size(10, 25), // 指定定位位置
            imageOffset: new BMap.Size(0, 0 - 0 * 25) // 设置图片偏移
            });
        var visited_icon = new BMap.Icon("http://api.map.baidu.com/img/markers.png", new BMap.Size(23, 25), {
            offset: new BMap.Size(10, 25), // 指定定位位置
            imageOffset: new BMap.Size(0, 0 - 10 * 25) // 设置图片偏移
            });
        var refuse_icon = new BMap.Icon("http://api.map.baidu.com/img/markers.png", new BMap.Size(23, 25), {
            offset: new BMap.Size(10, 25), // 指定定位位置
            imageOffset: new BMap.Size(0, 0 - 12 * 25) // 设置图片偏移
            });
        for(var i=0;i<data_info.length;i++){
            var marker = null;
            if(response == 1){
                marker = new BMap.Marker(new BMap.Point(data_info[i][0],data_info[i][1]),{icon:accept_icon});
            }else if(response == 0){
                marker = new BMap.Marker(new BMap.Point(data_info[i][0],data_info[i][1]),{icon:refuse_icon});
            }else if(response == 2){
                marker = new BMap.Marker(new BMap.Point(data_info[i][0],data_info[i][1]),{icon:visited_icon});
            }
            var content = data_info[i][2];
            overlays.push(marker);
//            map.addOverlay(overlays);               // 将标注添加到地图中将标注添加到地图中
		    addClickHandler(content,marker);
        }
        for(var i = 0; i < overlays.length; i++){
            map.addOverlay(overlays[i]);
        }
        map.removeEventListener("click",mapclick_fun);
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

    //-----------points mark------------



	var map = new BMap.Map("mapbody");
	var point = new BMap.Point(116.404, 39.915);
	map.centerAndZoom(point, 15);
//	map.disableDragging();
//	map.disablePinchToZoom();

    var geoc = new BMap.Geocoder();

    var navigationControl = new BMap.NavigationControl({
        // 靠左上角位置
        anchor: BMAP_ANCHOR_TOP_LEFT,
        // LARGE类型
        type: BMAP_NAVIGATION_CONTROL_LARGE,
        // 启用显示定位
        enableGeolocation: true
      });
      map.addControl(navigationControl);

  var geolocationControl = new BMap.GeolocationControl();
  map.addControl(geolocationControl);

	var overlays = [];
	var overlays2 = []; // for alternative use
	var linelays = [];


	//点击地图时的画点操作
	mapclick_fun = function(e){
	    setPointOnMap(e.point.lng,e.point.lat);
	    setBmapXY(e.point.lng,e.point.lat);
        var pt = e.point;
        geoc.getLocation(pt, function(rs){
            var addComp = rs.addressComponents;
            $("#record_form input[name='street']").val(addComp.district + ", " + addComp.street+ ","+addComp.streetNumber);
        });
	};
    map.addEventListener("touchend",mapclick_fun);
//	map.addEventListener('touchend',function(e){elem = e.domEvent.srcElement;alert(elem);elem.click();});