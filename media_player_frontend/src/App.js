import React, { useState } from 'react';
import Header from './Components/Header';
import Card from './Components/card';
import './style/MainCssFile.css'; // Correct path to the CSS file
import Filter from './Components/filter';



// Array of buttons with specific labels and the same class name "nav-item"
const buttons = [
  <button key="Notification" className="nav-item" onClick={() => console.log('Notification clicked!')}>
    <i className="fas fa-bell"></i> {/* Font Awesome bell icon */}
  </button>,
  <button key="profile" className="nav-item" onClick={() => console.log('Profile clicked!')}>
    <i className="fas fa-user"></i> {/* Font Awesome user icon */}
  </button>,
];

// Array of cards with sample data
const generateRandomCards = () => {
  const categories = ["Music", "Gaming", "Tech", "News"];
  const titles = ["Awesome Video", "Fantastic Clip", "Incredible Vlog", "Exciting Movie", "Entertaining Show"];
  const authors = ["John Doe", "Jane Smith", "Alice Johnson", "Bob Williams", "Charlie Brown"];

  const getRandomItem = (array) => array[Math.floor(Math.random() * array.length)];

  const generatedCards = [];
  for (let i = 0; i < 100; i++) {
    const randomTitle = getRandomItem(titles);
    const randomAuthor = getRandomItem(authors);
    const randomCategory = getRandomItem(categories);

    const card = {
      video: `https://example.com/thumbnail-${i + 1}.jpg`,
      title: randomTitle,
      author: randomAuthor,
      views: Math.floor(Math.random() * 2000) + 500, // Random views between 500 and 2500
      time_posted: `${Math.floor(Math.random() * 7) + 1} days ago`,
      category: randomCategory,
    };

    generatedCards.push(card);
  }

  return generatedCards;
};

const cards = generateRandomCards();
const App = () => {
  const [filteredCards, setFilteredCards] = useState(cards); // Assuming you have a 'cards' state initialized with your data
  const filters = ["All", "Music", "Gaming", "Tech", "News"];
  const handleSearch = (input) => {
    const filtered = cards.filter((card) => card.title.toLowerCase().includes(input.toLowerCase()));
    setFilteredCards(filtered);
  };
  const handleFilterChange = (selectFilter) => {
    if (selectFilter === 'All') {
      setFilteredCards(cards);
    } else {
      const filteredCards = cards.filter((card) => card.category === selectFilter);
      setFilteredCards(filteredCards);
    }
  }
  return (
    <div>
      <Header title="Media Player app" onSearch={handleSearch} buttons={buttons} />
      <Filter filters={filters} onSelectFilter={handleFilterChange} />
      <div className="card-container">
        {filteredCards.map((card, index) => (
          <Card key={index} {...card} />
        ))}
      </div>
    </div>
  );
}

export default App;
