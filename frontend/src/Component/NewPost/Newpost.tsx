import React from 'react'

export const Newpost = () => {
  return (
    <div>

<form>
  <div>
    <label htmlFor="title">Title</label>
    <input  type="text" id="title" name="title" typeof=''required />
  </div>
  <div>
    <label htmlFor="content">Content</label>
    <textarea id="content" name="content"  required></textarea>
  </div>
  <div>
    <label htmlFor="summary">Summary</label>
    <textarea id="summary" name="summary" ></textarea>
  </div>
  <div>
    <label htmlFor="author_id">Author ID</label>
    <input type="text" id="author_id" name="author_id" required/>
  </div>
  <div>
    <label htmlFor="image">Image</label>
    <input type="file" id="image" name="image" accept="image/*" />
  </div>
  <div>
    <label htmlFor="created_at">Created At</label>
    <input type="datetime-local" id="created_at" name="created_at" required />
  </div>
  <div>
    <label htmlFor="updated_at">Updated At</label>
    <input type="datetime-local" id="updated_at" name="updated_at" required/>
  </div>
  <button type="submit">Submit</button>
</form>


    </div>
  )
}
