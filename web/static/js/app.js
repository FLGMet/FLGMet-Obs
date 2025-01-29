let temperatureElement = document.getElementById("temperature");
let humidityElement = document.getElementById("humidity");

let socket = new WebSocket('ws://192.168.1.100:8080');

socket.onmessage = function(event) {
    let data = event.data.split(',');
    let temperature = data[0];
    let humidity = data[1];

    temperatureElement.innerText = temperature;
    humidityElement.innerText = humidity;
};