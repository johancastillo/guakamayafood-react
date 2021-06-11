import Home from './pages/Home';
import { Switch, Router, Route } from "wouter"
import Login from './pages/Login';

function RoutesApp() {
  return (
    <Router>
      
      <Switch>
        <Route path="/" component={Home} />
        <Route path="/login" component={Login} />
        <Route path="/register" component={Login} />
      </Switch>
    </Router>
  );
}

export default RoutesApp;
