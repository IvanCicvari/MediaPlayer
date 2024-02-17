import React, { useState } from 'react';
import '..//..//../style//Header and sidebar.css'; // Import your CSS file

const ProfileButton = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const handleButtonClick = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  const handleMenuItemClick = (menuItem) => {
    console.log(`Menu item clicked: ${menuItem}`);
    setIsMenuOpen(false);
  };

  return (
    <div className={`profile-button-container ${isMenuOpen ? 'active' : ''}`}>
      <button className="nav-item-user" onClick={handleButtonClick}>
        <i className="fas fa-user"></i>
      </button>

      {isMenuOpen && (
        <div className="profile-menu">
          <button onClick={() => handleMenuItemClick('Option 1')}>Option 1</button>
          <button onClick={() => handleMenuItemClick('Option 2')}>Option 2</button>
          <button onClick={() => handleMenuItemClick('Option 3')}>Option 3</button>
          {/* Add more menu items as needed */}
        </div>
      )}
    </div>
  );
};

export default ProfileButton;
