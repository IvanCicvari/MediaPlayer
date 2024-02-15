// VideoPage.js
import React from 'react';
import { useParams } from 'react-router-dom';

const VideoPage = ({ cards }) => {
  const { title } = useParams();
  const selectedVideo = cards.find((card) => encodeURIComponent(card.title) === title);

  if (!selectedVideo) {
    return <div>Video not found!</div>;
  }

  return (
    <div>
      <h1>{selectedVideo.title}</h1>
      <p>Author: {selectedVideo.author}</p>
      <p>Views: {selectedVideo.views}</p>
      <p>Time Posted: {selectedVideo.time_posted}</p>
      {selectedVideo.category && <p>Category: {selectedVideo.category}</p>}
      {/* Add more details as needed */}
      <video src={selectedVideo.video} controls width="640" height="360" />
    </div>
  );
};

export default VideoPage;
