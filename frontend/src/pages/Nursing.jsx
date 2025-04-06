import BackgroundAnimation from "../components/BackgroundAnimation";
import NursingLayout from "../components/forms/NursingLayout";


function Nursing() {
  return (
    <div className="app-container">
      <BackgroundAnimation />
      <div className="content">
        <NursingLayout />
      </div>
    </div>
  );
}

export default Nursing;