

const FooterMobile = () => {
    return (
        <div className="footer-device-mobile">
            <div className="wapper">
                <div className="footer-device-mobile-item device-home">
                    <a href="index.html">
                        <span className="icon">
                            <span className="pe-7s-home" />
                        </span>
        Home
      </a>
                </div>
                <div className="footer-device-mobile-item device-home device-wishlist">
                    <a href="wishlist.html">
                        <span className="icon">
                            <span className="pe-7s-like" />
                        </span>
        Wishlist
      </a>
                </div>
                <div className="footer-device-mobile-item device-home device-cart">
                    <a href="cart.html">
                        <span className="icon">
                            <span className="pe-7s-shopbag" />
                            <span className="count-icon">
                                0
          </span>
                        </span>
                        <span className="text">Cart</span>
                    </a>
                </div>
                <div className="footer-device-mobile-item device-home device-user">
                    <a href="my-account.html">
                        <span className="icon">
                            <span className="pe-7s-user" />
                        </span>
        Account
      </a>
                </div>
            </div>
        </div>

    )
}


export default FooterMobile


