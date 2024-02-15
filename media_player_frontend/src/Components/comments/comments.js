// Comments.js
import React, { useState } from 'react';
import '../../style/MainCssFile.css';

const Comments = () => {
  // Sample comments data (you can replace this with your actual data)
  const [comments, setComments] = useState([
    { id: 1, text: 'This is the first comment', author: 'User1', timestamp: '2 hours ago' },
    { id: 2, text: 'Great video!', author: 'User2', timestamp: '1 hour ago' },
    // Add more comments as needed
  ]);

  // State for tracking the new comment input
  const [newComment, setNewComment] = useState('');

  // Function to handle comment update
  const handleUpdate = (id, newText) => {
    // Update the comment with the new text
    setComments((prevComments) =>
      prevComments.map((comment) =>
        comment.id === id ? { ...comment, text: newText } : comment
      )
    );
  };

  // Function to handle comment delete
  const handleDelete = (id) => {
    // Remove the comment with the specified id
    setComments((prevComments) => prevComments.filter((comment) => comment.id !== id));
  };

  // Function to handle form submission and add a new comment
  const handleAddComment = (e) => {
    e.preventDefault();
    // Create a new comment object
    const newCommentObj = {
      id: comments.length + 1,
      text: newComment,
      author: 'Current User', // You can replace this with the actual user information
      timestamp: 'Just now', // You can use a timestamp library for accurate timestamps
    };
    // Update the comments state with the new comment
    setComments((prevComments) => [...prevComments, newCommentObj]);
    // Clear the input field
    setNewComment('');
  };

  return (
    <div className='comments'>
      {/* Form for adding new comments */}
      <form onSubmit={handleAddComment} className='comments-form'>
  <div className='comments-input-container'>
    <textarea
      className='comments-new-comments'
      value={newComment}
      onChange={(e) => setNewComment(e.target.value)}
      placeholder='Add a comment...'
    />
    <button type='submit'>Add Comment</button>
  </div>
</form>


      {/* Iterate over comments and display each one */}
      {comments.map((comment) => (
        <div key={comment.id} className='comment'>
          {/* Comment text */}
          <p className='comment-text'>{comment.text}</p>

          {/* Comment author and timestamp */}
          <div className='comment-info'>
            <span>{comment.author}</span>
            <span>{comment.timestamp}</span>
          </div>

          {/* Update and delete buttons */}
          <div className='comment-buttons'>
            <button onClick={() => handleUpdate(comment.id, prompt('Enter new text:'))}>
              Update
            </button>
            <button onClick={() => handleDelete(comment.id)}>Delete</button>
          </div>
        </div>
      ))}
    </div>
  );
};

export default Comments;
