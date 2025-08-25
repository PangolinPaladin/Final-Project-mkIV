import { Routes, Route } from 'react-router';

import Default_Layout from "./Structure/Default_Layout";
import Main from "./pages/Main"
import Full_Collection from "./pages/Full_Collection";
import New_Plant from "./pages/New_Plant";

function App() {
  return (
    <Routes>
      <Route element={<Default_Layout />}>
        <Route path='/' element={<Main />} />
        <Route path='/Full_Collection' element={<Full_Collection />} />
        <Route path='/New_Plant' element={<New_Plant />} />
      </Route>
    </Routes>
  );
}

export default App;

//Having trouble with the router. ... not sure why
