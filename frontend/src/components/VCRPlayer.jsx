import React, { useRef, useState } from "react";
import { FaPlay, FaPause, FaFastBackward, FaFastForward } from "react-icons/fa";

export default function VCRPlayer() {
  const videoRef = useRef(null);
  const [isPlaying, setIsPlaying] = useState(false);

  const handlePlay = () => {
    videoRef.current.play();
    setIsPlaying(true);
  };

  const handlePause = () => {
    videoRef.current.pause();
    setIsPlaying(false);
  };

  const handleRewind = () => {
    videoRef.current.currentTime -= 5;
  };

  const handleFastForward = () => {
    videoRef.current.currentTime += 5;
  };

  return (
    <div className="w-full max-w-3xl p-4 bg-gray-900 border-4 border-gray-700 shadow-xl rounded-xl">
      <div className="relative">
        <video
          ref={videoRef}
          className="w-full aspect-video rounded-md vhs-effect"
          controls={false}
        >
          <source src="/assets/highlight_final.mp4" type="video/mp4" />
          Your browser does not support the video tag.
        </video>
        <div className="absolute top-2 left-2 bg-black bg-opacity-60 px-2 py-1 text-xs text-lime-300 tracking-widest">
          {isPlaying ? "PLAY ▶" : "PAUSE ⏸"}
        </div>
      </div>
      <div className="mt-4 flex justify-center space-x-6 text-white">
        <button onClick={handleRewind} className="hover:text-lime-300">
          <FaFastBackward size={24} />
        </button>
        {isPlaying ? (
          <button onClick={handlePause} className="hover:text-lime-300">
            <FaPause size={24} />
          </button>
        ) : (
          <button onClick={handlePlay} className="hover:text-lime-300">
            <FaPlay size={24} />
          </button>
        )}
        <button onClick={handleFastForward} className="hover:text-lime-300">
          <FaFastForward size={24} />
        </button>
      </div>
    </div>
  );
}
