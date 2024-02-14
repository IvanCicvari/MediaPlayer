import React from 'react';
import '../style/MainCssFile.css'; // Correct path to the CSS file

const Filter = ({ onSelectFilter }) => {
  const filters = ["All", "Music", "Gaming", "Tech", "News"];

  return (
    <div className="filter-container">
      {filters.map((filter, index) => (
        <button
          key={index}
          className="filter-button"
          onClick={() => onSelectFilter(filter)}
        >
          {filter}
        </button>
      ))}
    </div>
  );
};

export default Filter;
