import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [inputResult, setinputResult] = useState('');
  const [search, setSearch] = useState('');
  const [searchResult, setSearchResult] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/add_user', {
        username,
        email
      });
      console.log('User added:', response.data);
      setinputResult('User Added')
    } catch (error) {
      console.error('Error adding user:', error);
      setinputResult('Error adding user: ' + error);
    }
  };

  const handleSearch = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.get(`http://localhost:5000/find_user?username=${search}`);
      if (response.data) {
        setSearchResult(`Email: ${response.data.email}`);
      } else {
        setSearchResult('User not found');
      }
    } catch (error) {
      console.error('Error searching for user:', error);
      setSearchResult('Error searching for user');
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            placeholder="Username"
          />
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Email"
          />
          <button type="submit">Add User</button>
        </form>
        {inputResult && <p>{inputResult}</p>}
        <form onSubmit={handleSearch}>
          <input
            type="text"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder="Search Username"
          />
          <button type="submit">Search User</button>
        </form>
        {searchResult && <p>{searchResult}</p>}
      </header>
    </div>
  );
}

export default App;
