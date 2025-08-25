import {useState, useEffect } from "react";
import styles from "./Plant.module.css"

const Plants = () => {
    const  [plantItems, setPlantItems] = useState([]);

    useEffect(() => {
        const getPlants = async () => {
            const url = "https://http://localhost:8000";
            const data = await fetch(url).then((response) => response.json());
            setPlantItems(data);
        };
        getPlants();
    }, [setPlantItems])

    return (
        <>
        <p>Plants Page</p>
        </>
    )
}

// in active code