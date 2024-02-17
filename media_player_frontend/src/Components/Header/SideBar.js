// Sidebar.js
import React from 'react';
import "../../style/Header and sidebar.css"

const Sidebar = () => {
  return (
    <aside className="sidebar">
      <nav className="sidebar-nav">
        <ul className="sidebar-menu">
          <li className="sidebar-menu-item">Menu Item 1</li>
          <li className="sidebar-menu-item">Menu Item 2</li>
          <li className="sidebar-menu-item">Menu Item 3</li>
        </ul>
      </nav>
    </aside>
  );
};

export default Sidebar;
