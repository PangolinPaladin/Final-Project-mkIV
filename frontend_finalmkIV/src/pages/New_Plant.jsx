import { useState } from "react";
import { useNavigate } from "react-router";
import { nanoid } from "nanoid";

const NewPlant = () => {
  const [linkCommon_Name, setLinkCommon_Name] = useState("");
  const [linkScientific_Name, setLinkScientific_Name] = useState("");
  const [linkPurchase_Date, setLinkPurchase_Date] = useState("");
  const [linkPurchase_Location, set_Purchase_Location] = useState("");
  const [linkPurchase_Condition, setLinkPurchase_Condition] = useState("");
  const [linkCurrent_Condition, setLinkCurrent_Condition] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (event) => {
    event.preventDefault();

    const shortUrl = nanoid(6);
    const apiUrl = `${import.meta.env.VITE_API_URL}/urls/add`;

    const body = {
      Common_Name: commonName,
      Scientific_Name: scientificName,
      Purchase_Date: purchaseDate,
      Purchase_Location: purchaseLocation,
      Purchase_Condition: purchaseCondition,
      Current_Condition: currentCondition, 
      user_id: 1,
    };

    try {
      const response = await fetch(apiUrl, {
        method: "POST",
        body: JSON.stringify(body),
        headers: {
          "Content-Type": "application/json",
        },
      });
      const data = await response.json();
      console.log("DATA: ", data);
      navigate("/links");
    } catch (error) {
      console.error(error);
      navigate("/404")
    }
  };

  return (
    <form method="POST" onSubmit={(e) => handleSubmit(e)}>
      <label>
        Common Name of Plant
        <input
          type="text"
          name="commonName"
          value={commonName}
          onChange={(e) => setCommonName(e.target.value)}
        />
      </label>
      <label>
        Scientific Name of Plant
        <input
          type="text"
          name="scientificName"
          value={scientificName}
          onChange={(e) => setScientificName(e.target.value)}
        />
      </label>
      <label>
        Purchase Date
        <input
          type="text"
          name="purchaseDate"
          value={purchaseDate}
          onChange={(e) => setPurchaseDate(e.target.value)}
        />
      </label><label>
        Purchase Location
        <input
          type="text"
          name="purchaseLocation"
          value={purchaseLocation}
          onChange={(e) => setPurchaseLocation(e.target.value)}
        />
      </label><label>
        Purchased Condition
        <input
          type="text"
          name="purchaseCondition"
          value={purchaseCondition}
          onChange={(e) => setPurchaseCondition(e.target.value)}
        />
      </label>
      <label>
        Current Condition
        <input
          type="text"
          name="currentCondition"
          value={currentCondition}
          onChange={(e) => setCurrentCondition(e.target.value)}
        />
      </label>
      
      <button type="submit">NEW PLANT!!</button>
    </form>
  );
};

export default NewPlant;

// {
//   "long_url": "google.com",
//   "short_url": "goo2",
//   "title": "Google",
//   "user_id": 1
// }