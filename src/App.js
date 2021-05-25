import { Router, Route, Switch } from "wouter"

import './App.css';
import Navigation from "./components/Navigation";
import AboutUs from "./pages/AboutUs";
import Home from './pages/Home';
import Login from "./pages/Login";

function App() {
  return (
    <Router>
      <Navigation />

      <Switch>
        <Route path="/" component={Home} />
        <Route path="/nosotros" component={AboutUs} />
        <Route path="/login" component={Login} />
      </Switch>

    </Router>
  );
}

export default App;
