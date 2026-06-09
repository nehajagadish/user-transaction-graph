import { BrowserRouter, Routes, Route } from "react-router-dom";

import Navbar from "./components/Navbar";
import Users from "./pages/Users";
import Transactions from "./pages/Transactions";
import Graph from "./pages/Graph";

function App() {
  return (
    <BrowserRouter>
      <Navbar />

      <Routes>
        <Route path="/" element={<Users />} />
        <Route path="/users" element={<Users />} />
        <Route path="/transactions" element={<Transactions />} />
        <Route path="/graph" element={<Graph />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;