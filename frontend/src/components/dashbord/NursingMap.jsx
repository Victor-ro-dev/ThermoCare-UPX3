import React, { useState, useEffect } from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import "../../styles/Dashboard.css";
import "../../styles/Login.css";
import { getNursingHome } from "../../services/nursingApi";

// Função para buscar latitude e longitude apenas pelo logradouro e número usando Nominatim
async function getLatLngByAddress(logradouro, numero) {
  try {
    const endereco = `${logradouro}, ${numero}`;
    const nominatimRes = await fetch(
      `https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(endereco)}`
    );
    const nominatimData = await nominatimRes.json();
    if (nominatimData && nominatimData.length > 0) {
      return {
        lat: parseFloat(nominatimData[0].lat),
        lng: parseFloat(nominatimData[0].lon),
      };
    }
    return null;
  } catch {
    return null;
  }
}

const NursingMap = () => {
  const [editing, setEditing] = useState(false);
  const [nursingHome, setNursingHome] = useState(null);
  const [form, setForm] = useState({
    name: "",
    logradouro: "",
    numero: "",
    bairro: "",
    cidade: "",
    estado: "",
    complemento: "",
  });
  const [loading, setLoading] = useState(true);
  const [coords, setCoords] = useState(null);
  const [mapLoading, setMapLoading] = useState(false);

  useEffect(() => {
    async function fetchNursingHome() {
      try {
        const data = await getNursingHome();
        setNursingHome(data);
        setForm({
          name: data.name || "",
          logradouro: data.logradouro || "",
          numero: data.numero || "",
          bairro: data.bairro || "",
          cidade: data.cidade || "",
          estado: data.estado || "",
          complemento: data.complemento || "",
        });
        // Busca coordenadas iniciais baseadas no logradouro e número do backend
        if (data.logradouro && data.numero) {
          setMapLoading(true);
          const latlng = await getLatLngByAddress(data.logradouro, data.numero);
          setCoords(latlng);
          setMapLoading(false);
        }
      } catch (err) {
        setNursingHome(null);
      } finally {
        setLoading(false);
      }
    }
    fetchNursingHome();
  }, []);

  // Atualiza o mapa ao editar logradouro ou número
  useEffect(() => {
    async function updateCoords() {
      if (form.logradouro && form.numero) {
        setMapLoading(true);
        const latlng = await getLatLngByAddress(form.logradouro, form.numero);
        setCoords(latlng);
        setMapLoading(false);
      }
    }
    if (!loading && (editing || coords === null)) {
      updateCoords();
    }
    // eslint-disable-next-line
  }, [form.logradouro, form.numero]);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSave = (e) => {
    e.preventDefault();
    setNursingHome({ ...form });
    setEditing(false);
    // Aqui você pode implementar a chamada para atualizar no backend, se desejar
  };

  if (loading) {
    return <div className="dashboard-main-content"><p>Carregando informações do asilo...</p></div>;
  }

  return (
    <div className="dashboard-main-content" style={{ display: "flex", flexDirection: "row", justifyContent: "center", alignItems: "flex-start", gap: "2rem", color: "#fff", padding: "2rem" }}>
      {/* Bloco de informações */}
      <div className="profile-group" style={{ minWidth: 320, maxWidth: 400 }}>
        <h2 style={{ marginBottom: "1rem", textAlign: "center" }}>Informações do Asilo</h2>
        {editing ? (
          <form onSubmit={handleSave}>
            <div className="form-group-login">
              <label>Nome:</label>
              <input name="name" type="text" value={form.name} onChange={handleChange} />
            </div>
            <div className="form-group-login">
              <label>Logradouro:</label>
              <input name="logradouro" type="text" value={form.logradouro} onChange={handleChange} />
            </div>
            <div className="form-group-login">
              <label>Número:</label>
              <input name="numero" type="text" value={form.numero} onChange={handleChange} />
            </div>
            <div className="form-group-login">
              <label>Bairro:</label>
              <input name="bairro" type="text" value={form.bairro} onChange={handleChange} />
            </div>
            <div className="form-group-login">
              <label>Cidade:</label>
              <input name="cidade" type="text" value={form.cidade} onChange={handleChange} />
            </div>
            <div className="form-group-login">
              <label>Estado:</label>
              <input name="estado" type="text" value={form.estado} onChange={handleChange} />
            </div>
            <div className="form-group-login">
              <label>Complemento:</label>
              <input name="complemento" type="text" value={form.complemento} onChange={handleChange} />
            </div>
            <button className="login-button" type="submit" style={{ marginTop: "1rem" }}>Salvar</button>
            <button className="login-button" type="button" style={{ background: "#ccc", color: "#222", marginLeft: "1rem" }} onClick={() => setEditing(false)}>Cancelar</button>
          </form>
        ) : (
          <div>
            <p><strong>Nome:</strong> {nursingHome?.name}</p>
            <p><strong>Logradouro:</strong> {nursingHome?.logradouro}</p>
            <p><strong>Número:</strong> {nursingHome?.numero}</p>
            <p><strong>Bairro:</strong> {nursingHome?.bairro}</p>
            <p><strong>Cidade:</strong> {nursingHome?.cidade}</p>
            <p><strong>Estado:</strong> {nursingHome?.estado}</p>
            <p><strong>Complemento:</strong> {nursingHome?.complemento}</p>
            <button className="login-button" style={{ marginTop: "1rem" }} onClick={() => setEditing(true)}>Editar</button>
          </div>
        )}
      </div>

      {/* Bloco do mapa */}
      <div style={{ flex: 1, minWidth: 350 }}>
        <h2 style={{ margin: "0 0 1rem 0", fontSize: "2rem", color: "#fff", textAlign: "center" }}>
          Localização do Asilo
        </h2>
        {mapLoading && <p style={{ color: "#fff" }}>Carregando mapa...</p>}
        {coords ? (
          <MapContainer center={[coords.lat, coords.lng]} zoom={15} style={{ height: "300px", width: "100%", borderRadius: "10px" }}>
            <TileLayer
              attribution='&copy; <a href="https://osm.org/copyright">OpenStreetMap</a> contributors'
              url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            <Marker position={[coords.lat, coords.lng]}>
              <Popup>
                <strong>{form.name}</strong><br />
                {form.logradouro}, {form.numero} <br />
                {form.bairro} - {form.cidade}/{form.estado}
              </Popup>
            </Marker>
          </MapContainer>
        ) : (
          <p style={{ color: "#fff" }}>Informe um logradouro e número válidos para exibir o mapa.</p>
        )}
      </div>
    </div>
  );
};

export default NursingMap;