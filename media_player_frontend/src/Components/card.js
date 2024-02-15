import React from 'react';
import '../style/MainCssFile.css'; // Correct path to the CSS file

const Card = ({ video, title, author, views, time_posted, category }) => {
  return (
    <div className="card">
      <img src={video} alt="Video Thumbnail" className="card-image" />
      <div className="card-content">
        <h2 className="card-title">{title}</h2>
        <p className="card-author">{author}</p>
        <p className="card-views">{views} views</p>
        <p className="card-time-posted">{time_posted}</p>
        {category && <p className="card-category">{category}</p>}
      </div>
    </div>
  );
};

export default Card;
