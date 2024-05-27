import React from 'react'
import { useNavigate  } from 'react-router-dom'


export const Navbar = () => {
    const navigate =useNavigate()
  return (
      
    <>

    <div className="h-[3em] w-[100%] bg-green-500 flex justify-start">
         <div className='w-[20%] bg-green-600 h-full'>
            <h1>Dainiki</h1>
         </div>

         <div className='flex justify-between w-[10em] items-center' >
              <div onClick={()=>navigate('home')}>Home</div>
              <div  onClick={()=>navigate('newPost')} className='cursor-pointer'>New Post</div> 
              
              
         </div>

    </div>
    </>


   
  )
}
