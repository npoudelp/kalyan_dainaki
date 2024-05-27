import './index.css'
import { Layout } from './Component/Layout/Layout'
import { Route, BrowserRouter as Router, Routes } from 'react-router-dom'
import { Newpost } from './Component/NewPost/Newpost'


function App() {
  

  return (
    <>

    <Router>
      <Routes>
        <Route path='' element={<Layout/>} >
          <Route path='newPost' element={<Newpost/>}></Route>


        </Route>
      </Routes>
    </Router>

  
  
    </>
  )
}

export default App
