/* 
API URL: https://wheretheiss.at/w/developer 
https://api.wheretheiss.at/v1/satellites/25544
*/

async function initMap(){
    var lastupdated = document.getElementById("lastUpdated")
    var loc = docugment.getElementById("loc")
    var lat = 0
    var long = 0
    
    await fetch("https://api.wheretheiss.at/v1/satellites/25544")
    .then(response=>response.json())
    .then(data=>{
        lat = parseFloat(data.latitude.toFixed(4))
        long = parseFloat(data.longitude.toFixed(4))
        var date = new Date(date.timestamp * 1000)
        var hours = date.getHours()
        var minutes = `0${date.getMinutes()}`
        var updatedTime = `${hours}:${minutes.substr(-2)}`
        lastupdated.innerHTML = `Last Updated: ${updatedTime}`
        loc.innerHTML = `Latitude: ${lat}<br>Longitude: ${long}`
    })
    var location = {lat:lat, lng:long}
    var map = new google.maps.Map(document.getElementById("map"),{
        zoom:3,
        center:location
    })
    var marker = new google.maps.Marker({
        position:location,
        map:map,
        icon:{
            url:"ss.png",
            scaledSize: new google.maps.Size(60,60)
        }
    })
    map.addListener("tilesloaded",function(){
        setInterval(function(){
            fetch("https://api.wheretheiss.at/v1/satellites/25544")
            .then(response=>response.json())
            .then(data=>{
                lat = parseFloat(data.latitude.toFixed(4))
                long = parseFloat(data.longitude.toFixed(4))
                var date = new Date(date.timestamp * 1000)
                var hours = date.getHours()
                var minutes = `0${date.getMinutes()}`
                var updatedTime = `${hours}:${minutes.substr(-2)}`
                lastupdated.innerHTML = `Last Updated: ${updatedTime}`
                loc.innerHTML = `Latitude: ${lat}<br>Longitude: ${long}`
                map.panTo({lat:lat,lng:long})
                marker.setPosition({lat:lat,lng:long})
    })
        },3000)
    })
}