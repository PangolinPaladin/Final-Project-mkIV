import { useState, useEffect } from 'react';
import styles from './PlantList.module.css';

const PlantList = () => {
  const [linkItems, setLinkItems] = useState([]);

  useEffect(() => {
    const getLinks = async () => {
      const url = `${import.meta.env.VITE_API_URL}/urls`;
      const data = await fetch(url).then((response) => response.json());

      setLinkItems(data);
    };
    getLinks();
  }, [setLinkItems]);

  return (
    <>
      {linkItems && linkItems.length > 0 ? (
        <ul className={styles.linkList}>
          {linkItems.map((link) => {
            return (
              <li key={link.id}>
                <a
                  href={`https://bzzt.fun/${link.short_url}`}
                  title={`Short URL for ${link.title}`}
                  className={styles.linkLink}
                >
                  {link.title}
                </a>
              </li>
            );
          })}
        </ul>
      ) : (
        <p>Plants are loading...</p>
      )}
    </>
  );
};

export default PlantList;