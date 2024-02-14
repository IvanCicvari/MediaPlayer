// SearchInput.js
import React from 'react';
import "../../style/MainCssFile.css";

const SearchInput = ({ placeholder, onChange }) => {
    return (
        <div className="search-container">
            <input
                className='nav-search'
                type="text"
                placeholder={placeholder}
                onChange={onChange}
            />
            <button className="search-button">
                <i className="fas fa-search"></i>
            </button>
            <button className="upload-button">
                <i className="fas fa-upload"></i>
            </button>
        </div>
    );
};

export default SearchInput;
