/*********
  Complete project details at https://randomnerdtutorials.com  
*********/

#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>
#include "EspMQTTClient.h"

/*#include <SPI.h>
#define BME_SCK 14
#define BME_MISO 12
#define BME_MOSI 13
#define BME_CS 15*/

#define SEALEVELPRESSURE_HPA (1013.25)
#define TOPIC String("Kharkiv/pressureSensor")

EspMQTTClient client(
  "ntu_khpi",
  "",
  "mqtt.korotach.com",  // MQTT Broker server ip
  "student",   // Can be omitted if not needed
  "student-password",   // Can be omitted if not nomeeded
  "sensor1",     // Client name that uniquely identify your device
  1883              // The MQTT port, default to 1883. this line can be omitted
);

Adafruit_BME280 bme; // I2C
//Adafruit_BME280 bme(BME_CS); // hardware SPI
//Adafruit_BME280 bme(BME_CS, BME_MOSI, BME_MISO, BME_SCK); // software SPI

unsigned long delayTime;

void setup() {
  Serial.begin(115200);
  Serial.println(F("BME280 test"));

  client.enableDebuggingMessages(); // Enable debugging messages sent to serial output
  client.enableHTTPWebUpdater(); // Enable the web updater. User and password default to values of MQTTUsername and MQTTPassword. These can be overridden with enableHTTPWebUpdater("user", "password").
  client.enableLastWillMessage("TestClient/lastwill", "I am going offline");  // You can activate the retain flag by setting the third parameter to true

  bool status;

  // default settings
  // (you can also pass in a Wire library object like &Wire2)
  status = bme.begin(0x76);  
  if (!status) {
    Serial.println("Could not find a valid BME280 sensor, check wiring!");
    while (1);
  }

  Serial.println("-- Default Test --");
  delayTime = 1000;

  Serial.println();
}

void onConnectionEstablished()
{
  // Publish a message to "mytopic/test"
  client.publish("mytopic/test", "This is a message"); // You can activate the retain flag by setting the third parameter to true
}

void loop() { 
  auto msg = getValues();
  client.publish(TOPIC, msg);
  client.loop();
  delay(delayTime);
}

String getValues() {

  auto temperature = bme.readTemperature();
  auto pressure = bme.readPressure() / 100.0F;
  auto alt = bme.readAltitude(SEALEVELPRESSURE_HPA);
  auto humidity = bme.readHumidity();

  String message = "{\n";
  message += "  \"temperature\": "; message += temperature; message += ",\n";
  message += "  \"pressure\": "; message += pressure; message += ",\n";
  message += "  \"altitude\": "; message += alt; message += ",\n";
  message += "  \"humidity\": "; message += humidity; message += "\n";
  message += "}";
  // Convert temperature to Fahrenheit
  /*Serial.print("Temperature = ");
  Serial.print(1.8 * bme.readTemperature() + 32);
  Serial.println(" *F");*/
  Serial.print("Temperature = ");
  Serial.print(temperature);
  Serial.println(" *C");
  
  Serial.print("Pressure = ");
  Serial.print(pressure);
  Serial.println(" hPa");

  Serial.print("Approx. Altitude = ");
  Serial.print(alt);
  Serial.println(" m");

  Serial.print("Humidity = ");
  Serial.print(humidity);
  Serial.println(" %");

  Serial.print("RAM = ");
  Serial.print(ESP.getFreeHeap());

  Serial.println();
  return message;
}
