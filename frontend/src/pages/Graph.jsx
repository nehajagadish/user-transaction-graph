import { useEffect, useState } from "react";
import axios from "axios";
import CytoscapeComponent from "react-cytoscapejs";

function Graph() {

  const [elements, setElements] = useState([]);
  const [userId, setUserId] = useState("U1");

 const loadGraph = () => {

  axios
    .get("http://localhost:8000/graph")
    .then((res) => {

      console.log(res.data);

      setElements(
        Array.isArray(res.data)
          ? res.data
          : []
      );
    })
    .catch((err) => {
      console.log(err);
      setElements([]);
    });
};

const loadUserGraph = () => {

  axios
    .get(
      `http://localhost:8000/graph/user/${userId}`
    )
    .then((res) => {

      console.log(res.data);

      setElements(
        Array.isArray(res.data)
          ? res.data
          : []
      );
    })
    .catch((err) => {
      console.log(err);
      setElements([]);
    });
};

  useEffect(() => {
    loadGraph();
  }, []);

  return (
    <div style={{ padding: "20px" }}>

      <h1>Graph Visualization</h1>

      <input
        type="text"
        value={userId}
        onChange={(e) => setUserId(e.target.value)}
        placeholder="Enter User ID"
        style={{
          padding: "8px",
          marginRight: "10px"
        }}
      />

      <button onClick={loadUserGraph}>
        Load User Graph
      </button>

      <button
        onClick={loadGraph}
        style={{
          marginLeft: "10px"
        }}
      >
        Load Default Graph
      </button>

      <p>
        Elements Loaded: {elements ? elements.length : 0}
      </p>

      <CytoscapeComponent
        elements={elements}
        style={{
          width: "100%",
          height: "900px",
          border: "1px solid black"
        }}
        layout={{
          name: "grid",
          fit: true,
          padding: 150
        }}
        stylesheet={[
          {
            selector: 'node[type="user"]',
            style: {
              label: 'data(label)',
              shape: 'ellipse',
              width: 60,
              height: 60,
              'font-size': 12,
              'text-valign': 'center',
              'text-halign': 'center'
            }
          },
          {
            selector: 'node[type="transaction"]',
            style: {
              label: 'data(label)',
              shape: 'rectangle',
              width: 60,
              height: 60,
              'font-size': 12,
              'text-valign': 'center',
              'text-halign': 'center'
            }
          },
          {
            selector: 'edge',
            style: {
              width: 2,
              'curve-style': 'bezier'
            }
          }
        ]}
      />

    </div>
  );
}

export default Graph;