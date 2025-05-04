const API_URL = "http://localhost:8000/api/v1";

export async function registerSensor(sensorData) {
    const response = await fetch(`${API_URL}/sensor`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(sensorData),
        credentials: "include",
    });

    console.log("Response:", response); // Adicione este log para depuração
    console.log("Sensor Data:", sensorData); // Adicione este log para depuração
    
    if (!response.ok) {
        throw new Error("Erro ao registrar sensor");
    }
    return response.json();
}

export async function getSensors() {
    const response = await fetch(`${API_URL}/sensor`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
        credentials: "include",
    });
    
    if (!response.ok) {
        throw new Error("Erro ao obter sensores");
    }
    return response.json();
}

export async function sendWhatsappAlert(temperature, phone) {
    try {
      const response = await fetch('https://v2-api.gzappy.com/message/send-text', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwdWJsaWNfaW5zdGFuY2VfaWQiOiIyQUpOSioqKioqKioqKioqKioqWFZMQUsiLCJleHBpcmVzX2F0IjoiMjAyNi0wNC0yNFQwMjozNzo0Ny42ODVaIiwiaWF0IjoxNzQ1NDYyMjY3LCJleHAiOjIwMDQ2NjIyNjd9.BJDfAccgdkgKFdOlauJYs68dnUaMxzVp5mb8kQ0ufrY`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          phone: 55 + `${phone}`,
          message: `Alerta! Temperatura fora do ideal: ${temperature}°C`
        })
      });
      const data = await response.json();
      console.log('Mensagem enviada com sucesso:', data);
    } catch (error) {
      console.error('Erro ao enviar mensagem:', error);
    }
  }