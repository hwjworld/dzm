	var map = new BMap.Map("mapbody");
	var point = new BMap.Point(116.404, 39.915);
	map.centerAndZoom(point, 17);
	map.enableScrollWheelZoom();
    var geoc = new BMap.Geocoder();
    var geolocationControl = new BMap.GeolocationControl();
    map.addControl(geolocationControl);
    //-----------points mark------------
	function addMarkPoints(data_info){
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
	}

	function addClickHandler(content,marker){
		marker.addEventListener("click",function(e){
            openInfo(content,e);
        });
	}
	function openInfo(content,e){
		var p = e.target;
		var point = new BMap.Point(p.getPosition().lng, p.getPosition().lat);
		var infoWindow = new BMap.InfoWindow(content,opts);  // 创建信息窗口对象
		map.openInfoWindow(infoWindow,point); //开启信息窗口
	}
    //-----------points mark------------

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
	map.addEventListener("click",function(e){
	    setPointOnMap(e.point.lng,e.point.lat);
	    setBmapXY(e.point.lng,e.point.lat);
        var pt = e.point;
        geoc.getLocation(pt, function(rs){
            var addComp = rs.addressComponents;
            $("#record_form input[name='street']").val(addComp.district + ", " + addComp.street+ ","+addComp.streetNumber);
        });
	});
	function setPointOnMap(x,y){
	    remove_overlays();
        var marker = new BMap.Marker(new BMap.Point(x,y));
        map.addOverlay(marker);
	    map.panTo(new BMap.Point(x,y));
        overlays[0] = marker;
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