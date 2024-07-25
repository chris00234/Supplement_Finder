import React from 'react';
import './CSS/chatbot.css';
import { useState } from 'react';

const Chatbot = () => {
    return(
        <div className="chatbot">
            <div className="chatbot-container">
                <div className="chatbot-header">
                    <h1>Chatbot</h1>
                </div>
                <div className="chatbot-body">
                    <div className="chatbot-messages">
                        <div className="chatbot-message">
                            <p>Hi! I'm the Supplement Finder chatbot. How can I help you today?</p>
                        </div>
                    </div>
                </div>
                <div className="chatbot-input">
                        <input type="text" className="chatbot-input-box" placeholder="Type a message..."/>
                        <button className="chatbot-send-btn">Send</button>
                    </div>
            </div>
        </div>
    );
}

export default Chatbot;