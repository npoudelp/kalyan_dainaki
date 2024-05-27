import React from 'react'
import { Outlet } from 'react-router-dom'
import { Navbar } from '../Navbar/Navbar'

export const Layout = () => {
  return (
    <div>
        <div>
          <Navbar/>
         </div>
        <div className='bg-slate-300 h-[100vh]'>
           <Outlet />
         </div>
    </div>
  )
}
