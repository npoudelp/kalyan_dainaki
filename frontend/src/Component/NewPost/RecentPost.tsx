import React from 'react'
import  post from '../../assets/post.JPG'



export const RecentPost = () => {
  return (

      <div >
    
    <div className=' h-[30em] w-[30em]  '> 
        
        <div className='w-full h-[3em] bg-black flex justify-center text-white items-center'>Recent Post</div>
        
        <div className='w-full h-[7em] mt-2 flex  items-center'>
             <div className='w-[8em] ml-3 h-[6em] bg-blue-600'>
            
                 <img src={post} alt="" className='w-[8em] h-[6em]' />
                
             </div>

             <div className=' w-full  ml-3 h-[6em] bg-blue-600 flex justify-evenly flex-col  text-justify leading-tignt'>
                <div><h3><b>This is an Image </b></h3></div>
                <div className='p-2'><p>Lorem ipsum dolor consectetur adipisicing elit.
                 
                     recusandae at odit accusamus ... <i>Readmore</i>
                     </p></div>

             </div>
     

        </div>
        
        <div className='w-full h-[7em] mt-2 flex  items-center'>
             <div className='w-[8em] ml-3 h-[6em] bg-blue-600'>
            
                 <img src={post} alt="" className='w-[8em] h-[6em]' />
                
             </div>

             <div className=' w-full  ml-3 h-[6em] bg-blue-600 flex justify-evenly flex-col  text-justify leading-tignt'>
                <div><h3><b>This is an Image </b></h3></div>
                <div className='p-2'><p>Lorem ipsum dolor consectetur adipisicing elit.
                 
                     recusandae at odit accusamus ... <i>Readmore</i>
                     </p></div>

             </div>
     

        </div>
        
        <div className='w-full h-[7em] mt-2 flex  items-center'>
             <div className='w-[8em] ml-3 h-[6em] bg-blue-600'>
            
                 <img src={post} alt="" className='w-[8em] h-[6em]' />
                
             </div>

             <div className=' w-full  ml-3 h-[6em] bg-blue-600 flex justify-evenly flex-col  text-justify leading-tignt'>
                <div><h3><b>This is an Image </b></h3></div>
                <div className='p-2'><p>Lorem ipsum dolor consectetur adipisicing elit.
                 
                     recusandae at odit accusamus ... <i>Readmore</i>
                     </p></div>

             </div>
     

        </div>
        
        <div className='w-full h-[7em] mt-2 flex  items-center'>
             <div className='w-[8em] ml-3 h-[6em] bg-blue-600'>
            
                 <img src={post} alt="" className='w-[8em] h-[6em]' />
                
             </div>

             <div className=' w-full  ml-3 h-[6em] bg-blue-600 flex justify-evenly flex-col  text-justify leading-tignt'>
                <div><h3><b>This is an Image </b></h3></div>
                <div className='p-2'><p>Lorem ipsum dolor consectetur adipisicing elit.
                 
                     recusandae at odit accusamus ... <i>Readmore</i>
                     </p></div>

             </div>
     

        </div>
        
     
     </div>

    </div>
  
  )
}
