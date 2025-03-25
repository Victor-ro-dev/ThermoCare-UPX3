import BackgroundAnimation from '../components/BackgroundAnimation';
import LoginLayout from '../components/forms/LoginLayout';

function Login() {
    return (
      <div className="app-container">
        <BackgroundAnimation />
        <div className="content">
        <LoginLayout />
        </div>
      </div>
    );
  }
  
  export default Login;