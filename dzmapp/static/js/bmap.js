	var map = new BMap.Map("mapbody");
	var point = new BMap.Point(116.404, 39.915);
	map.centerAndZoom(point, 16);
	map.enableScrollWheelZoom();
    var geoc = new BMap.Geocoder();
    var geolocationControl = new BMap.GeolocationControl();
    map.addControl(geolocationControl);

	var overlays = [];
	var linelays = [];
	function clearAll() {
		remove_overlays();
        remove_linelays();
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
	mapclick_fun = function(e){
	    setPointOnMap(e.point.lng,e.point.lat);
	    setBmapXY(e.point.lng,e.point.lat);
        var pt = e.point;
        geoc.getLocation(pt, function(rs){
            var addComp = rs.addressComponents;
            $("#record_form input[name='street']").val(addComp.district + ", " + addComp.street+ ","+addComp.streetNumber);
        });
	};
	map.addEventListener("click",mapclick_fun);
	function setPointOnMap(x,y){
	    remove_overlays();
        var marker = new BMap.Marker(new BMap.Point(x,y));
        map.addOverlay(marker);
	    map.panTo(new BMap.Point(x,y));
        overlays[0] = marker;
	}

	function moveToPoint(x,y){
	    map.panTo(new BMap.Point(x,y));
	}

    //------------添加折线---------------
    //return firstpoint
    function addPolyline(plPoints){
        ps = plPoints.split(",");
        var points = [];
        var firstpoint = null;
        for(var j=0;j<ps.length;j++){
            ps[j] = ps[j].replace(/\"/g,"");
            var p1 = ps[j].split("|")[0];
            var p2 = ps[j].split("|")[1];
            if(j==0){firstpoint = new BMap.Point(p1,p2);}
            points.push(new BMap.Point(p1,p2));
        }

        var line = new BMap.Polyline(eval(points),{strokeColor:"red", strokeWeight:2, strokeOpacity:0.5});
        map.addOverlay(line);
        linelays[linelays.length] = line;
        return firstpoint;
	}
	//---------------------------------
	/*
	var geolocation = new BMap.Geolocation();
	geolocation.getCurrentPosition(function(r){
		if(this.getStatus() == BMAP_STATUS_SUCCESS){
			var mk = new BMap.Marker(r.point);
			map.addOverlay(mk);
			map.panTo(r.point);
		}
		else {
			alert('你在哪里，我不知道,555~~~');
		}
	},{enableHighAccuracy: true})
	*/

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
        for(var i=0;i<data_info.length;i++){
            var marker = null;
            if(response == 1){
                marker = new BMap.Marker(new BMap.Point(data_info[i][0],data_info[i][1]),{icon:accept_icon});
            }else if(response == 0){
                marker = new BMap.Marker(new BMap.Point(data_info[i][0],data_info[i][1]));
            }else if(response == 2){
                marker = new BMap.Marker(new BMap.Point(data_info[i][0],data_info[i][1]),{icon:visited_icon});
            }
            var content = data_info[i][2];
            map.addOverlay(marker);               // 将标注添加到地图中将标注添加到地图中
		    addClickHandler(content,marker);
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