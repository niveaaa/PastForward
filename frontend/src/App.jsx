import React from "react";
import VCRPlayer from "./components/VCRPlayer";

export default function App() {
  return (
    <div className="crt bg-black w-screen h-screen flex items-center justify-center text-white font-mono">
      <VCRPlayer />
    </div>
  );
}
