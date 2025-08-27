import { Link, Navigate } from 'react-router';
import styles from './Header.module.css';

const Header = () => {
  return (
    <header TheHeader={styles.header}>
      <h1>Plant Tracker</h1>
        <menu>
          <nav class= "main-container">
            <li> <Link to='/'>Main</Link> </li>
          </nav>
          <nav class= "full-collection-container">
              <li> <Link to='/Full_Collection'>Full Collection</Link> </li>
          </nav >
          <nav class= "new-plant-container">
            <li> <Link to='/New_Plant'>New Plant</Link> </li> 
          </nav>
          <nav class= "meet-the-creator">
            <li> <Link to='/Meet_The_Creator'>Meet The Creator</Link> </li> 
          </nav>
        </menu>
    </header>
  );
};

export default Header;

