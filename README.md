# 1:10 Ratio Strategy using Zerodha Kite Connect API

This repository implements a **1:10 Ratio options strategy** using the **Zerodha Kite Connect (paid) API**. The strategy automates both **login and order execution**, and is designed to enter a specific ratio of positions — selling 1 lot of premium strike vs buying 10 lots of far OTM hedges — optimizing risk and reward.

## 🧠 Strategy Overview
- **1:10 Ratio**: Sell 1 lot of ATM/near-the-money options and buy 10 lots of cheaper OTM options.
- Designed to balance limited risk with amplified reward potential.
- Utilizes market behavior, volatility crush, and time decay as edges.

## 🔑 Key Features
- 🔐 Full Zerodha login flow with token generation and storage
- ⚙️ Position sizing with 1:10 strike ratio logic
- 📈 Real-time market feed integration
- 💼 Order management & execution with safety checks
- 🧾 Logging of trades and session info
- 🔁 Looping / scheduled strategy runs

## 🔗 Tech Stack
- Zerodha Kite Connect (paid API)
- Python with requests/session handling
- Modular and extendable code structure

## 🤝 Community & Learning
The goal of this public release is to **help others understand ratio-based trading**, proper use of **Zerodha’s API**, and **build confidence in automating real strategies**. Whether you're learning or customizing your own bot, you're welcome to explore, fork, or contribute.

---

> **Disclaimer**: This strategy is shared for educational purposes only. Real-money trading involves significant risk. Please backtest thoroughly and understand the logic before live use.

