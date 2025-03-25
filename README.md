# ThermoCare - Sistema de Monitoramento para Asilos

## 🔍 Visão Geral
O **ThermoCare** é uma solução integrada que combina:
- **Sistema de cadastro** para gestão de usuários
- **Monitoramento IoT** de temperatura e umidade em tempo real
- **Alertas automáticos** para condições críticas

Focado no conforto e segurança de idosos em asilos.

## 🛠️ Funcionalidades Principais

### 👥 Gestão de Usuários
- Cadastro de cuidadores e administradores
- Autenticação segura com JWT
- Controle de níveis de acesso

### 🌡️ Monitoramento Ambiental
- Leitura em tempo real via ESP
- Dashboard com histórico de medições
- Notificações quando:
  - Temperatura > 28°C ou < 20°C
  - Umidade > 70% ou < 40%

## 💻 Stack Tecnológica

### Frontend
| Tecnologia | Descrição |
|------------|-----------|
| ![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB) | Interface dinâmica |
| ![React Router](https://img.shields.io/badge/React_Router-CA4245?style=for-the-badge&logo=react-router&logoColor=white) | Navegação SPA |
| ![Framer Motion](https://img.shields.io/badge/Framer_Motion-0055FF?style=for-the-badge) | Animações fluidas |

### Backend
| Tecnologia | Descrição |
|------------|-----------|
| ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white) | API Python rápida |
| ![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white) | Autenticação segura |
| ![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white) | Banco de dados local |

### 🔮 IoT (Próximas Implementações)
- **ESP32/ESP8266** com sensores DHT22
- Comunicação via **MQTT**
- Dashboard em tempo real

