import { Link } from 'react-router';
import styles from './NavBar.module.jsx'


const NavBar = () => {
    return (
<nav className="navbar">
  <div className="navbar-container">
    <Link to="/" className="navbar-brand">Plant App</Link>
    <ul className="navbar-nav">
      <li className="nav-item">
        <Link to="/" className="nav-link">Home</Link>
      </li>
      <li className="nav-item">
        <Link to="/Full_Collection" className="nav-link">Full Collection</Link>
      </li>
      <li className="nav-item">
        <Link to="/New_Plant" className="nav-link">New Plant</Link>
      </li>
    </ul>
  </div>
</nav>
    );
};

export default NavBar;