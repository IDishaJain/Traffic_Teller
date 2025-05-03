import { motion } from 'framer-motion'
import { Link } from 'react-router-dom'
import banner from '../assets/banner1.png'
import { variants } from '../animations/variants'

export default function Landing() {
  return (
    <div className="max-w-screen-2xl mx-20 mt-10">
      <div className='gradientBg rounded-xl rounded-br-[80px]'>
        <div className="flex flex-col-reverse md:flex-row justify-between items-center gap-1">
          <div className='px-4 ml-4 mt-4 md:mt-4'>
            <h2 className='text-5xl text-white mb-4'>Vehicle Detection</h2>
           
            <h2 className='text-5xl text-white mb-4'>& Counting</h2>
            {/* <div className='w-2/3 mt-[6px] mb-[30px]'> */}
              <p className='text-white text-[14px] w-2/3'>
              Want to keep a sharp eye on your property or fleet like never before?
              Experience next-level monitoring with our intelligent web application that uses cutting-edge computer vision to detect and track vehicles in real-time empowering you with smart insights and enhanced security at your fingertips.
              </p>
            <div className='mt-4 md:mb-8 mb-4'>
              <button className="py-2 px-4 bg-primary text-white rounded cursor-pointer hover:shadow-boxshadowcolor" >
                <Link to="/detect">Get Started</Link>
                </button>
            </div>
          </div>
          <motion.div 
          variants={variants("up")}
          initial="hidden"
          whileInView="visible"
          className='md:mr-8 '> 
            <img src={banner}/>
          </motion.div>
        </div>
      </div>
    </div>
  )
}

