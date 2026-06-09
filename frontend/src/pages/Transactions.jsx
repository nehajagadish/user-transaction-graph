import { useEffect, useState } from "react";
import axios from "axios";

function Transactions() {

  const [transactions, setTransactions] = useState([]);
  const [amount, setAmount] = useState("");

  const loadTransactions = () => {

    let url =
      "http://localhost:8000/transactions?limit=50";

    if (amount !== "") {
      url += `&min_amount=${amount}`;
    }

    axios
      .get(url)
      .then((res) => {
        setTransactions(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  useEffect(() => {
    loadTransactions();
  }, []);

  return (
    <div style={{ padding: "20px" }}>

      <h1>Transactions</h1>

      <input
        type="number"
        placeholder="Minimum Amount"
        value={amount}
        onChange={(e) => setAmount(e.target.value)}
        style={{
          padding: "8px",
          marginRight: "10px"
        }}
      />

      <button onClick={loadTransactions}>
        Search
      </button>

      <br />
      <br />

      <table border="1" cellPadding="10">

        <thead>
          <tr>
            <th>ID</th>
            <th>Amount</th>
            <th>Device</th>
          </tr>
        </thead>

        <tbody>

          {transactions.map((tx) => (
            <tr key={tx.transaction_id}>
              <td>{tx.transaction_id}</td>
              <td>{tx.amount}</td>
              <td>{tx.device_id}</td>
            </tr>
          ))}

        </tbody>

      </table>

    </div>
  );
}

export default Transactions;