import React from "react";
import { RecentPost } from "./RecentPost";

export const Newpost = () => {
  return (
    <>
      <div className="flex justify-evenly  mt-[3em] ">
        <div>
          <RecentPost />
        </div>

        <div className="bg-yellow h-[60em] w-[30em]  border border-black border-black-1 ">
         <div className='w-full h-[3em] bg-black flex justify-center text-white items-center'>Add New Post</div>
        
          <div className="flex mt-[1em] ">
            <div>
              <label htmlFor="topic">Topic</label>

              <input
                type="text"
                name="topic"
                id="topic"
                className="border border-black border-black-1 h-[2em] w-[10em] ml-[5px]"
              />
            </div>

            <div>
              <div className="ml-[10px]">
                <label htmlFor="author">Author</label>
                <input
                  type=" text"
                  name="author"
                  id="author"
                  className="border border-black border-black-1 h-[2em] w-[10em] ml-[4px]"
                />
              </div>
            </div>
          </div>

          <div>
            <label htmlFor="content">Content</label>
            <input
              type=" textbox"
              name="content"
              id="name"
              className="border border-black border-black-1 h-[3em] w-[8em]"
            />
          </div>

          <div>
            <label htmlFor="image">Image</label>
            <input
              type="file"
              name="image"
              id="image"
              className="border border-black border-black-1 h-[3em] w-[8em]"
            />
          </div>
        </div>

        <div className="bg-yellow h-[30em] w-[10em]  border border-black border-black-1 "></div>
      </div>
    </>
  );
};
