import React, { useState, useEffect } from "react";
import "../../styles/Dashboard.css";
import { registerSensor, getSensors, sendWhatsappAlert } from "../../services/sensorApi";

const DashboardMainContent = () => {
  const [showModal, setShowModal] = useState(false);
  const [sensorName, setSensorName] = useState("");
  const [sensorLocal, setSensorLocal] = useState("");
  const [sensorPhone, setSensorPhone] = useState("");
  const [loading, setLoading] = useState(false);
  const [sensors, setSensors] = useState([]);
  const [selectedSensorId, setSelectedSensorId] = useState("");
  const [showAlertModal, setShowAlertModal] = useState(false); // Novo estado para alerta
  const [alertMessage, setAlertMessage] = useState(""); // Mensagem do alerta

  useEffect(() => {
    async function fetchSensors() {
      try {
        const data = await getSensors();
        setSensors(data);
      } catch (err) {
        console.error("Erro ao buscar sensores:", err);
      }
    }
    fetchSensors();
  }, []);

  const handleAddSensor = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const sensorData = {
        name: sensorName,
        location: sensorLocal,
        phone: sensorPhone,
      };
      await registerSensor(sensorData);
      setShowModal(false);
      setSensorName("");
      setSensorLocal("");
      setSensorPhone("");
      // Atualiza a lista de sensores após adicionar
      const updatedSensors = await getSensors();
      setSensors(updatedSensors);
    } catch (err) {
      alert("Erro ao registrar sensor: " + err.message);
    } finally {
      setLoading(false);
    }
  };

  // Busca o sensor selecionado
  const selectedSensor = sensors.find(sensor => sensor.id === selectedSensorId);

  useEffect(() => {
    if (
      selectedSensor &&
      selectedSensor.last_data
    ) {
      const temp = selectedSensor.last_data.temperature;
      const phoneRaw = selectedSensor.phone.replace(/\D/g, "");
      if (temp > 27 || temp < 15) {
        sendWhatsappAlert(temp,phoneRaw); // Envia alerta via WhatsApp
        setAlertMessage(
          temp > 27
            ? `Alerta: Temperatura crítica detectada (${temp}°C).`
            : `Alerta: Temperatura muito baixa detectada (${temp}°C).`
        );
        setShowAlertModal(true);
      }
    }
  }, [selectedSensor]);

  // Função para formatar o telefone automaticamente no padrão (99) 99999-9999
  function formatPhone(value) {
    // Remove tudo que não for número
    let v = value.replace(/\D/g, "");
    // Limita a 11 dígitos
    v = v.slice(0, 13);
    // Aplica a máscara
    if (v.length > 6) {
      v = v.replace(/^(\d{2})(\d{5})(\d{0,4}).*/, "($1) $2-$3");
    } else if (v.length > 2) {
      v = v.replace(/^(\d{2})(\d{0,5})/, "($1) $2");
    } else if (v.length > 0) {
      v = v.replace(/^(\d{0,2})/, "($1");
    }
    return v.trim();
  }

  return (
    <div className="dashboard-main-content">
      <div className="dashboard-header">
        <div className="dashboard-header-title">
          <h2>Dashboard</h2>
        </div>
        <div className="dashboard-header-actions">
          <button className="dashboard-button" onClick={() => setShowModal(true)}>
            <i className="fa-solid fa-plus"></i> Adicionar sensor
          </button>
          <select
            className="dashboard-select"
            value={selectedSensorId}
            onChange={e => setSelectedSensorId(Number(e.target.value))}
          >
            <option value="" disabled>
              Selecione um Sensor
            </option>
            {sensors.map(sensor => (
              <option key={sensor.id} value={sensor.id}>
                {sensor.name} - {sensor.location}
              </option>
            ))}
          </select>
        </div>
      </div>
      <div className="dashboard-content">
        <div className="dashboard-sensor-config">
          <div className="dashboard-sensor-config-cards">
            {selectedSensor ? (
              <>
                <div className="sensor-card">
                  <h4>Sensor</h4>
                  <p>{selectedSensor.name}</p>
                </div>
                <div className="sensor-card">
                  <h4>Local</h4>
                  <p>{selectedSensor.location}</p>
                </div>
                <div className="sensor-card">
                  <h4>Status</h4>
                  <p>{selectedSensor.status || "Desconhecido"}</p>
                </div>
              </>
            ) : (
              <p style={{ padding: "1rem" }}>Selecione um sensor para ver os detalhes.</p>
            )}
          </div>
        </div>

        <div className="dashboard-sensor-infos">
  <div className="sensor-info-card">
    <header>
      <h3>Temperature Monitor</h3>
      <button
        className="refresh-button"
        onClick={async () => {
          const updatedSensors = await getSensors();
          setSensors(updatedSensors);
        }}
      >
        <i className="fa-solid fa-arrows-rotate"></i>
      </button>
    </header>
    <i id="temperature" className="fa-solid fa-temperature-high"></i>
    <p>
      {selectedSensor && selectedSensor.last_data
        ? `${selectedSensor.last_data.temperature}°C`
        : "--"}
    </p>
  </div>
  <div className="sensor-info-card">
    <header>
      <h3>Umity Monitor</h3>
      <button
        className="refresh-button"
        onClick={async () => {
          const updatedSensors = await getSensors();
          setSensors(updatedSensors);
        }}
      >
        <i className="fa-solid fa-arrows-rotate"></i>
      </button>
    </header>
    <i id="umity" className="fa-solid fa-droplet"></i>
    <p>
      {selectedSensor && selectedSensor.last_data
        ? `${selectedSensor.last_data.humidity}%`
        : "--"}
    </p>
  </div>
</div>
      </div>

      {showModal && (
        <div className="modal-overlay">
          <div className="modal-content">
            <h3>Adicionar Sensor</h3>
            <form onSubmit={handleAddSensor}>
              <div className="form-group">
                <label>Nome do Sensor</label>
                <input
                  type="text"
                  value={sensorName}
                  onChange={e => setSensorName(e.target.value)}
                  required
                />
              </div>
              <div className="form-group">
                <label>Local</label>
                <input
                  type="text"
                  value={sensorLocal}
                  onChange={e => setSensorLocal(e.target.value)}
                  required
                />
              </div>
              <div className="form-group">
                <label>Celular</label>
                <input
                  type="text"
                  value={sensorPhone}
                  onChange={e => {
                    const formatted = formatPhone(e.target.value);
                    setSensorPhone(formatted);
                  }}
                  required
                  placeholder="(99) 99999-9999"
                  maxLength={20} // Aumentado para permitir DDI e números maiores
                  inputMode="numeric"
                  pattern="\(\d{2}\) \d{5}-\d{4}"
                />
              </div>
              <div style={{ display: "flex", gap: "1rem", marginTop: "1rem" }}>
                <button type="submit" className="dashboard-button" disabled={loading}>
                  {loading ? "Enviando..." : "Salvar"}
                </button>
                <button
                  type="button"
                  className="dashboard-button"
                  onClick={() => setShowModal(false)}
                  style={{ background: "#ccc", color: "#222" }}
                >
                  Cancelar
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* Modal de alerta de temperatura crítica */}
      {showAlertModal && (
        <div className="modal-overlay">
          <div className="modal-content" style={{ background: "#ffeded", color: "#b30000", textAlign: "center" }}>
            <h3>⚠️ Alerta de Temperatura</h3>
            <p>{alertMessage}</p>
            <button
              className="dashboard-button"
              style={{ background: "#b30000", color: "#fff", marginTop: "1rem" }}
              onClick={() => setShowAlertModal(false)}
            >
              Fechar
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default DashboardMainContent;