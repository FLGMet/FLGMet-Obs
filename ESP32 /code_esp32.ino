#include <Wire.h>
#include <Adafruit_SHT35.h>
#include <WiFi.h>
#include <WebSocketsClient.h>

const char* ssid = "your_SSID";
const char* password = "your_PASSWORD";

WebSocketsClient webSocket;
const char* serverAddress = "ws://192.168.1.100:8080";

Adafruit_SHT35 sht35;

void setup() {
    Serial.begin(115200);
    Wire.begin();
    sht35.begin(0x44);  

    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.println("Connexion au WiFi...");
    }
    Serial.println("Connecté au WiFi");

    webSocket.begin(serverAddress, 8080);
    webSocket.onEvent(webSocketEvent);
}

void loop() {
    webSocket.loop();
    
    float temperature = sht35.getTemperature();
    float humidity = sht35.getHumidity();
    
    String data = String(temperature) + "," + String(humidity);
    webSocket.sendTXT(data);
    
    delay(2000);
}

void webSocketEvent(WStype_t type, uint8_t * payload, size_t length) {
    if (type == WStype_TEXT) {
        Serial.printf("Message reçu: %s\n", payload);
    }
}
