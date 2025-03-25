import BackgroundAnimation from '../components/BackgroundAnimation';
import RegisterLayout from '../components/forms/RegisterLayout';

function Register() {
    return (
      <div className="app-container">
        <BackgroundAnimation />
        <div className="content">
        <RegisterLayout />
        </div>
      </div>
    );
  }
  
  export default Register;