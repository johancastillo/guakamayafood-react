import banner from "../images/login-banner.jpg";
import background from "../images/background.jpg";
import logo from "../images/logo.svg";

const Login = () => {
  return (
    <div className="login-page" style={{ 'background': `url(${background})` }}>
      <div className="box-login">
        <div className="box-banner">
          <img src={banner} alt="" />
        </div>

        <div className="box-form">

          <div className="text-center">
            <img src={logo} alt="" />
            
            <br/>
            <br/>
            
            <h1 className="text-center text-uppercase">
              ¡Ordena ahora!
            </h1>
          </div>

          <br />

          <form>
            <div className="mb-3">
              <label htmlFor="exampleInputEmail1" className="form-label">
                Email
              </label>
              <input
                type="email"
                className="form-control"
                id="exampleInputEmail1"
                aria-describedby="emailHelp"
              />

              {/* 
              <div id="emailHelp" className="form-text">
                We'll never share your email with anyone else.
              </div>
              */}

            </div>
            <div className="mb-3">
              <label htmlFor="exampleInputPassword1" className="form-label">
                Contraseña
              </label>
              <input
                type="password"
                className="form-control"
                id="exampleInputPassword1"
                placeholder=""
              />
            </div>

            <br/>
            
            <button type="submit" className="btn btn-primary">
              Iniciar sesión
            </button>

          </form>

          <br/>

          <div>
            <p>
              ¿No tienes cuenta? <b>Regístrate.</b>
            </p>
          </div>

        </div>
      </div>
    </div>
  );
};

export default Login;
