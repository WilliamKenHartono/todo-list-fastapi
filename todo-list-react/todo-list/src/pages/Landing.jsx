import { Link } from "react-router-dom";

export default function Landing() {
  return (
    <div>
      <h1>Hey, welcome</h1>

      <Link to="/Todo">
        <button className="btn">Go to Todo List</button>
      </Link>
    </div>
  );
}
