#include <Arduino.h>
#include <WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>
#include <ArduinoJson.h>

// Configurações Wi-Fi
const char* ssid = "";
const char* password = "";

// Configurações MQTT
const char* mqtt_server = "";
const int mqtt_port = 1883;
const char* mqtt_topic = "/sensor_data";
const char* sensor_id = "sensor_01"; // Identificador do sensor

// Configuração do DHT
#define DHTPIN 4         // Pino conectado ao DHT
#define DHTTYPE DHT22    // DHT11 ou DHT22
DHT dht(DHTPIN, DHTTYPE);

// Objetos WiFi e MQTT
WiFiClient espClient;
PubSubClient client(espClient);

void setup_wifi() {
  delay(10);
  Serial.println();
  Serial.print("Conectando ao WiFi: ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi conectado");
  Serial.println(WiFi.localIP());
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Conectando ao MQTT...");
    if (client.connect(sensor_id)) {
      Serial.println("conectado");
    } else {
      Serial.print("falhou, rc=");
      Serial.print(client.state());
      Serial.println(" tentando novamente em 5 segundos");
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  dht.begin();
  setup_wifi();
  client.setServer(mqtt_server, mqtt_port);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("Falha ao ler do sensor DHT!");
    delay(10000);
    return;
  }

  // Monta o JSON
 JsonDocument doc;
  doc["sensor_id"] = sensor_id;
  doc["temperature"] = temperature;
  doc["humidity"] = humidity;

  char payload[128];
  serializeJson(doc, payload);

  // Publica no tópico MQTT
  if (client.publish(mqtt_topic, payload)) {
    Serial.print("Dados enviados: ");
    Serial.println(payload);
  } else {
    Serial.println("Falha ao enviar dados MQTT");
  }

  delay(300000); 
}