import BackToTop from "../components/BackToTop"
import Banners from "../components/Banners"
import Comments from "../components/Comments"
import Footer from "../components/Footer"
import FooterMobile from "../components/FooterMobile"
import InstagramSection from "../components/InstagramSection"
import LastPosts from "../components/LastPosts"
import Navigation from "../components/Navigation"
import Slider from "../components/Slider"
import TopTrends from "../components/TopTrends"



const Home = () => {
    return (
        <>
            <Navigation />
            <div class="fullwidth-template">
                <Slider />
                <Banners />
                <TopTrends />
                <Comments />
                <LastPosts />
                <InstagramSection />
            </div>

            <Footer />
            <FooterMobile />

            <BackToTop />
        </>
    )
}


export default Home



