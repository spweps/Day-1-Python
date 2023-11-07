/* API URL
http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=imperial
*/
function getData(e){
    e.preventDefault()
    var getWeather = document.getElementById("getWeather")
    var form = new FormData(getWeather)
    console.log(form.get("city"))
    var output = ""
    fetch("http://localhost:5000/weather",{method:"POST", body:form})
        .then(res=>res.json())
        .then(data=>{
            output += `
                <b>City:</br>${data.name}
                <b>Country:</br>${data.sys.country}
                <b>Description:</br>${data.weather[0].description}
                <b>Current Temp</br>${data.main.temp}&deg;
                <img.src = "static/icons/${data.weather[0].icon}.pnt"><br>
                `
            document.getElementById("output").innerHTML = output
        })
}
