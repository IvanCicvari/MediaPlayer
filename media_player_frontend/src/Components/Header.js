import React from 'react';
import SearchInput from './custom_header_components/SearchInput';
import '../style/MainCssFile.css'; // Correct path to the CSS file
const Header = ({ title, onSearch, buttons }) => {
  const handleSearchChange = (e) => {
    onSearch(e.target.value);
  };

  return (
    <div className='nav'>
      <p className='title'>{title}</p>
      <SearchInput placeholder="Search..." onChange={handleSearchChange} />
        <div className='nav-item-afther-search'>
          {buttons}
        </div>
    </div>
  );
};

export default Header;
