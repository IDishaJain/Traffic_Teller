import { useEffect, useState } from "react";
 import axios from "axios";
 import Skeleton from 'react-loading-skeleton';
 import 'react-loading-skeleton/dist/skeleton.css';
 import PieChart from "../components/PieChart";

 export default function Result() {
  const [northCount, setNorthCount] = useState({});
  const [southCount, setSouthCount] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const getResults = async () => {
      setLoading(true);
      setError(null);
      try {
        const response = await axios.get('http://127.0.0.1:8000/get-results');
        console.log("Get Results Response:", response);
        if (response.data && response.data.north_count && response.data.south_count) {
          setNorthCount(response.data.north_count);
          setSouthCount(response.data.south_count);
        } else {
          console.warn("Results data is incomplete:", response.data);
        }
      } catch (err) {
        console.error("Error fetching results:", err);
        setError("Failed to fetch results. Please try again.");
      } finally {
        setLoading(false);
      }
    };
    getResults();
  }, []);

  return (
    <div className="max-w-screen-2xl mx-20 mt-10">
      {loading ? (
        <div className="flex flex-col justify-center align-center mt-10 mx-24">
          <div className="flex flex-col justify-center align-center ">
            <Skeleton containerClassName="flex-1" baseColor='#E8CBF4' highlightColor="#EAE8E7" count={6} height={20} />
            <Skeleton containerClassName="flex-1" baseColor='#E8CBF4' highlightColor="#EAE8E7" width="50%" height={20} />
          </div>
          <p>Loading results...</p>
        </div>
      ) : error ? (
        <div>{error}</div>
      ) : (
        <div className="flex flex-col justify-center align-center mt-10 mb-10">
          <h2 className="text-4xl font-bold text-center mt-2 text-primary ">Vehicle Distribution Chart</h2>
          <div className="flex flex-row justify-center align-center gap-16 mt-10 ">
            <div className="chartGradientBg rounded-3xl p-10">
              <PieChart data={northCount} />
              <h3 className="text-2xl font-bold text-center mt-2 text-black">North</h3>
            </div>
            <div className="chartGradientBg rounded-3xl p-10">
              <PieChart data={southCount} />
              <h3 className="text-2xl font-bold text-center mt-2 text-black">South</h3>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}


