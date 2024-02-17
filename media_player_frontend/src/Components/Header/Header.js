// Header.js
import React from 'react';
import "../../style/Header and sidebar.css"
import SearchInput from './custom_header_components/SearchInput';
import ProfileButton from './custom_header_components/ProfileButton ';
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
            <ProfileButton />
          </div>
      </div>
    );
  };

export default Header;
