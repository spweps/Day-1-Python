/* API URL
http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=imperial
*/
function getData(e){
    e.preventDefault()
    var getWeather = document.getElementById("getWeather")
    var form = new FormData(getWeather)
    console.log(form.get("city"))
    var output = ""
    fetch("http://localhost:5000/weather",{method:"POST",body:form})
        .then(res=>res.json())
        .then(data =>{
            output += `
                <b>City</b>: ${data.name}<br>
                <b>Country</b>: ${data.sys.country}<br>
                <b>Description</b>: ${data.weather[0].description}<br>
                <img src="static/icons/${data.weather[0].icon}.png"><br>
                <b>Current Temp</b>: ${data.main.temp}&deg; <br>
                `
            document.getElementById("output").innerHTML = output
        })
}

