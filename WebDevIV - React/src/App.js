import MyButton from "./MyButton"
import { useState } from "react";

import { BrowserRouter, Routes, Route } from "react-router-dom";
import About from "./About";
import Home from "./Home";


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/">
          <Route path="Home" element={<Home />} />
          <Route path="About" element={<About />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
