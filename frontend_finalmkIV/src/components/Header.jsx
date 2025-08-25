import { Link } from 'react-router';
import styles from './Header.module.css';

const Header = () => {
  return (
    <header className={styles.header}>
      <h1>SHRINK RAY!</h1>
      <nav className={styles.nav}>
        <ul>
          <li>
            <Link to='/'>Main</Link>
          </li>
          <li>
            <Link to='/Full_Collection'>Full Collection</Link>
          </li>
          <li>
            <Link to='/New_Plant'>New Plant</Link>
          </li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;

// this is currently broken, I feel like I should be having to dig into other folders,
//  so ../src/pages.jsx but maybe not. 