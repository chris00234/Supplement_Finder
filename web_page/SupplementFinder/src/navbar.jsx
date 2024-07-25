import React from 'react';
import './CSS/navbar.css';
import { useState } from 'react';

const Navbar = () => {
    const [isDropdownOpen, setIsDropdownOpen] = useState(false);
    const toggleDropdown = () => {
        setIsDropdownOpen(!isDropdownOpen);
    };


    return(
        <nav className="navbar">
            <div className="navbar-left">
                <a href="/" className="logo">
                <b>Home</b>
                </a>
            </div>
            <div className="navbar-center">
                <ul className="nav-links">
                <li>
                    <button className="dropbtn" onClick={toggleDropdown}><b>Products</b></button>
                    {isDropdownOpen && (<div className="dropdown-content">
                            <a href="/products">All Products</a>
                            <a href="/products/vitamins">Vitamins</a>
                            <a href="/products/minerals">Minerals</a>
                            <a href="/products/amino-acids">Amino Acids</a>
                            <a href="/products/herbs">Herbs</a>
                            <a href="/products/other">Other</a>
                        </div>)}
                </li>
                <li>
                    <a href="/update"><b>Update</b></a>
                </li>
                <li>
                    <a href="/instructions"><b>Instructions</b></a>
                </li>
                </ul>
            </div>
            <div className="navbar-right">
                <div className="search-box">
                    <input type="text" className="search-bar" placeholder="Search..."/>
                    <button className="search-btn">search</button>
                </div>
            </div>
        </nav>
    );
};

export default Navbar;