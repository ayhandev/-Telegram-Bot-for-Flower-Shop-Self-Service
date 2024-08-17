# 🌸 Telegram Bot for Flower Shop Self-Service

Welcome to the **Flower Shop Self-Service Bot** project! This bot is designed to streamline the shopping experience for customers in a flower shop, allowing them to browse, purchase, and collect their bouquets with ease.

## 🚀 Features

- **Product Selection:** Browse a curated selection of bouquets directly within the Telegram bot.
- **Real-Time Inventory:** Stay up-to-date with the latest inventory, seamlessly integrated with the [MoySklad](https://moysklad.ru/) API.
- **In-App Payments:** Pay securely within the Telegram app (payment integration is currently emulated).
- **Smart Life Integration:** After payment, the bot automatically unlocks the refrigerator door via Smart Life, so you can collect your bouquet.

## 🛠 Project Structure

```bash
├── main.py                  
├── requirements.txt         
├── README.md                
├── .gitignore 
└── LICENSE.md       
```
## ⚙️ Installation

To get started with this project, follow these steps:

# Clone the Repository:
```
git clone https://github.com/yourusername/flower-shop-bot.git](https://github.com/ayhandev/-Telegram-Bot-for-Flower-Shop-Self-Service.git
```

# Install Dependencies:

```
pip install -r requirements.txt
```

#Set Up API Tokens:

Open main.py and replace the placeholder values with your actual API tokens:

- **MOYSKLAD_API_TOKEN: Your MoySklad API token.
- **SMART_LIFE_API_TOKEN: Your Smart Life API token.
- **SMART_LIFE_DEVICE_ID: ID of the Smart Life device (relay).
- **TELEGRAM_BOT_TOKEN: Your Telegram Bot API token.

#Run the Bot:
```
python main.py
```

##🎯 Usage

1. Start the bot by sending the /start command in your Telegram app.
2. Browse bouquets from the list provided.
3. Complete your purchase (currently emulated) and let the bot handle the rest.
4. Collect your bouquet from the refrigerator, which will automatically unlock after payment.

##🌟 Future Enhancements

- **Payment Integration: Implement real-world payment solutions such as  YooMoney.
- **Enhanced Error Handling: Improve error responses and fallback mechanisms.
- **User Authentication: Add secure user authentication and registration.

##📄 License

*This project is licensed under the MIT License - see the LICENSE file for details.

##🤝 Contributing

#Contributions are highly appreciated! Feel free to fork this repository, submit a pull request, or open an issue.

##📧 Contact

#For any questions or support, please contact jumanyyazowayhan32@gmail.com
