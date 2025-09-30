# Geld Maschine - Full-Stack Application

A sophisticated full-stack web application for managing and monitoring automated online income streams in real-time. This application features a Flask backend with SQLite database and a React frontend, providing comprehensive bot management and dashboard functionality.

## 🚀 Features

### Backend Features
- **RESTful API**: Complete API for bot management, dashboard metrics, and transactions
- **Database Management**: SQLite database with models for bots, transactions, and metrics
- **Real-time Data**: Live bot status updates and earnings simulation
- **CORS Support**: Cross-origin resource sharing for frontend-backend communication

### Frontend Features
- **Interactive Dashboard**: Real-time earnings display and bot status monitoring
- **Bot Management**: Start, pause, and configure various automated bots
- **Live Charts**: Dynamic earnings visualization with Recharts
- **Responsive Design**: Optimized for all device sizes
- **Toast Notifications**: User feedback for all actions

### Supported Bot Types
- **Crypto Arbitrage Bot**: Automated cryptocurrency trading between exchanges
- **Forex Trading Bot**: AI-powered foreign exchange trading
- **Affiliate Marketing Bot**: Automated affiliate campaign management
- **Dropshipping Bot**: Product listing and order processing automation
- **Social Media Bot**: Automated content monetization
- **Mining Pool Bot**: Optimized crypto mining management

## 🛠️ Technology Stack

### Backend
- **Framework**: Flask 3.1.1
- **Database**: SQLite with SQLAlchemy ORM
- **CORS**: Flask-CORS for cross-origin requests
- **Python**: 3.11+

### Frontend
- **Framework**: React 18 with Vite
- **Styling**: Tailwind CSS with shadcn/ui components
- **Charts**: Recharts for data visualization
- **Icons**: Lucide React icons
- **Notifications**: Sonner for toast messages

## 📦 Installation & Setup

### Prerequisites
- Python 3.11+
- Node.js 18+
- Git

### Backend Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Aaronlinke/geld-maschine-fullstack.git
   cd geld-maschine-fullstack
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Initialize the database:
   ```bash
   python src/seed_data.py
   ```

5. Start the Flask server:
   ```bash
   python src/main.py
   ```

The application will be available at `http://localhost:5000`

### Development Mode (Separate Frontend)

If you want to run the frontend separately for development:

1. Navigate to the frontend directory and install dependencies:
   ```bash
   cd ../geld-maschine-frontend
   pnpm install
   ```

2. Start the development server:
   ```bash
   pnpm run dev
   ```

The frontend will be available at `http://localhost:5173`

## 🚀 Deployment

### Vercel Deployment

This application is configured for easy deployment on Vercel:

1. Push your code to GitHub
2. Connect your repository to Vercel
3. Vercel will automatically detect the Flask application and deploy it

### Manual Deployment

For other platforms:

1. Ensure all dependencies are in `requirements.txt`
2. Set the Flask app entry point to `src/main.py`
3. Configure environment variables as needed

## 📁 Project Structure

```
├── src/
│   ├── models/
│   │   ├── user.py          # User model and database setup
│   │   └── bot.py           # Bot, Transaction, and Metrics models
│   ├── routes/
│   │   ├── user.py          # User-related API routes
│   │   └── bot.py           # Bot management API routes
│   ├── static/              # Built frontend files
│   ├── database/
│   │   └── app.db           # SQLite database
│   ├── main.py              # Flask application entry point
│   └── seed_data.py         # Database seeding script
├── requirements.txt         # Python dependencies
└── README.md
```

## 🔧 API Endpoints

### Bot Management
- `GET /api/bots` - Get all bots
- `GET /api/bots/{id}` - Get specific bot
- `POST /api/bots` - Create new bot
- `POST /api/bots/{id}/action` - Perform bot action (start/pause/stop)
- `PUT /api/bots/{id}/settings` - Update bot settings

### Dashboard
- `GET /api/dashboard/metrics` - Get dashboard metrics
- `GET /api/dashboard/earnings-chart` - Get earnings chart data

### Transactions
- `GET /api/transactions` - Get all transactions
- `POST /api/payout` - Request payout

### Simulation
- `POST /api/simulate-earnings` - Simulate bot earnings (demo feature)

## 🎮 Usage

1. **Dashboard Overview**: View real-time earnings, active bots, success rate, and ROI
2. **Bot Management**: Start, pause, or configure individual bots
3. **Earnings Simulation**: Use the "Einnahmen simulieren" button to simulate bot earnings
4. **Payout Requests**: Request payouts using the "Auszahlung anfordern" button
5. **Real-time Updates**: All changes are reflected immediately in the dashboard

## 🔒 Security Notes

- This is a demonstration application with simulated data
- In production, implement proper authentication and authorization
- Use environment variables for sensitive configuration
- Implement rate limiting and input validation
- Use HTTPS in production

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

For support and questions, please open an issue in the GitHub repository.

---

**Note**: This application uses simulated data for demonstration purposes. For a production environment, integrate with real financial APIs and implement proper security measures.
