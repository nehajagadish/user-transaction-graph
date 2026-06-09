import { Link } from "react-router-dom";

function Navbar() {
  return (
    <div style={{ padding: "20px", borderBottom: "1px solid #ccc" }}>
      <Link to="/">Users</Link>

      {" | "}

      <Link to="/transactions">Transactions</Link>

      {" | "}

      <Link to="/graph">Graph</Link>
    </div>
  );
}

export default Navbar;