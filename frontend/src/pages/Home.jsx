import '../styles/Home.css';
import Header from '../components/Header';
import MainContent from '../components/home/MainContent';
import BackgroundAnimation from '../components/BackgroundAnimation';
import About from '../components/home/About';
import Features from '../components/home/Features';
import Footer from '../components/Footer';

function App() {
  return (
    <div className="app-container">
      <BackgroundAnimation />
      <div className="content">
        <Header />
        <MainContent />
        <About />
        <Features />
        <Footer />
      </div>
    </div>
  );
}

export default App;