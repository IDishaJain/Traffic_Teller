import Detection from '../assets/detection1.png'
import Classification from '../assets/classification1.png'
import Piechart from '../assets/pie_chart.png'
import { variants } from '../animations/variants'
import { motion } from 'framer-motion'


export default function Feature() {
  return (
    <div className="max-w-screen-2xl mx-20 mt-10">
        <div className='mb-10'>
            <h2 className="text-center text-bold text-5xl text-pink-900">Features</h2>
        </div>
        {/* Detection  */}
        <div className="flex flex-col md:flex-row justify-between items-center gap-1 ml-4">
            <motion.div
            variants={variants("left")}
            initial="hidden"
            whileInView="visible"
             className='w-1/2 px-4'>
                <img src={Detection} alt="Detection image" />
            </motion.div>

            <div className='w-full px-4 md:w-2/5'>
                <h2 className='text-semibold text-2xl md:text-4xl text-pink-900 mb-4'>Detection and Counting</h2>
                <p className='text-roboto text-[14px] md:text-[18px]'>Our system efficiently detects and counts individual vehicles from video footage, maintaining high accuracy across different weather conditions and lighting scenarios.</p>
            </div>
        </div>
        {/* Classification  */}
        <div className="flex flex-col-reverse md:flex-row justify-between items-center gap-1 ml-4">
            <div className='w-full px-4 md:w-2/5'>
                <h2 className='text-semibold text-2xl md:text-4xl text-pink-900 mb-4'>Classification of Vehicles</h2>
                <p className='text-roboto text-[14px] md:text-[18px]'>Classification of vehicles based on six categories.
                    Beyond simple detection, our app goes further by classifying each vehicle into six distinct categories: Car, Truck, 2-Wheeler, Bus, MiniBus and Tempo.</p>
            </div>

            <motion.div 
            variants={variants("right")}
            initial="hidden"
            whileInView="visible"className='w-1/2 px-4'>
                <img src={Classification} alt="Classification image" />
            </motion.div>
        </div>
        {/* analytics */}
        <div className="flex flex-col md:flex-row justify-between items-center gap-1 ml-4">
            <motion.div
            variants={variants("left")}
            initial="hidden"
            whileInView="visible"
             className='w-1/2 px-4'>
                <img src={Piechart} alt="Pie Chart image" />
            </motion.div>

            <div className='w-full px-4 md:w-2/5'>
                <h2 className='text-semibold text-2xl md:text-4xl text-pink-900 mb-4'>Informative Analytics </h2>
                <p className='text-roboto text-[14px] md:text-[18px]'>Access a comprehensive dashboard that provides valuable insights derived from your video data. Track total vehicle counts, analyze trends over time, and gain detailed information about the distribution of different vehicle types. This data is available for further analysis and reporting, empowering you to make informed, data-driven decisions.</p>
            </div>
        </div>
    </div>
  )
}


