import './App.scss';
import 'bootstrap/dist/css/bootstrap.min.css';
import Application from './pages/Application';
import Help from './pages/Help';
import Header from './components/Header';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

function App() {
  const pages = [
    {name: 'Application', link:'/'},
    {name: 'Help', link: '/help'}
  ]

  return (
    <div className="App">
      <Router>
      <Header pages={pages} />
        <Routes>
          <Route exact path="/" element={<Application />}/>
          <Route exact path="/help" element={<Help />}/>
        </Routes>
      </Router>
    </div>
  );
}

export default App;
