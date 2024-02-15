import React from 'react';
import Comments from './comments/comments';
import '../style/MainCssFile.css';

const VideoPage = ({ selectedCard }) => {

  // Check if a video is selected
  if (!selectedCard) {
    return <div>Video not found!</div>;
  }

  // Render the video player and additional information
  return (
    <div>
      <div className='video-container'>
        {/* Video player element with controls */}
        <video
          className='video'
          src={selectedCard.video}
          controls
          width="640"
          height="360"
        ></video>

        {/* Video details */}
        <h1 className='video-title'>{selectedCard.title}</h1>
        <p className='video-author'>Author: {selectedCard.author}</p>
        <div className='video-description'>
          <p className='video-views'>Views: {selectedCard.views}</p> 
          <p className='video-time-posted'>Time Posted: {selectedCard.time_posted}</p>
        </div>
        
        {/* Display category if available */}
        {selectedCard.category && <p className='video-category'> Category: {selectedCard.category}</p>}
      </div>

      <div className='comments'>
        {/* create crud operations to add comments  */}
            <Comments/>
      </div>
    </div>
  );
};

export default VideoPage;
