import React from 'react'
import { useNavigate  } from 'react-router-dom'

export const Navbar = () => {
    const navigate =useNavigate()
  return (
      
    <>

    <div className="h-[3em] w-[100%] bg-red-800  flex justify-start">
         <div className='w-[20%] bg-yellow-500 h-full'>
            <h1>Dainiki</h1>
         </div>

         <div>
              <div>Home</div>
              <div  onClick={()=>navigate('newPost')} className='cursor-pointer'>New Post</div>
              
         </div>

    </div>
    </>


   
  )
}
