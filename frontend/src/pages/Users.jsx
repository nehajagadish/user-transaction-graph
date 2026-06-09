import { useEffect, useState } from "react";
import axios from "axios";

function Users() {

  const [users, setUsers] = useState([]);
  const [search, setSearch] = useState("");

  const loadUsers = () => {

    axios
      .get(
        `http://localhost:8000/users?name=${search}&limit=50`
      )
      .then((res) => {
        setUsers(res.data);
      });
  };

  useEffect(() => {
    loadUsers();
  }, []);

  return (
    <div style={{ padding: "20px" }}>

      <h1>Users</h1>

      <input
        type="text"
        placeholder="Search user name"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        style={{
          padding: "8px",
          marginRight: "10px"
        }}
      />

      <button onClick={loadUsers}>
        Search
      </button>

      <br />
      <br />

      <table border="1" cellPadding="10">

        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
          </tr>
        </thead>

        <tbody>

          {users.map((user) => (
            <tr key={user.user_id}>
              <td>{user.user_id}</td>
              <td>{user.name}</td>
              <td>{user.email}</td>
            </tr>
          ))}

        </tbody>

      </table>

    </div>
  );
}

export default Users;