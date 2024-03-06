document.getElementById("GeoButton").onclick = function(){
    navigator.geolocation.getCurrentPosition(successCallback, errorCallback);
};

function successCallback(position){
    var latitude = position.coords.latitude;
    document.getElementById("latitude").innerHTML = latitude;
    var longitude = position.coords.longitude;
    document.getElementById("longitude").innerHTML = longitude;
};

function errorCallback(error){
    alert("位置情報が取得できませんでした");
};