import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.models.bot import Bot, Transaction, DashboardMetrics, db
from src.models.user import User
from datetime import datetime, date
import json

def seed_database(app):
    """Seed the database with initial data"""
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        # Create initial bots
        bots_data = [
            {
                'name': 'Crypto Arbitrage Bot',
                'description': 'Automatischer Krypto-Handel zwischen Börsen',
                'bot_type': 'crypto',
                'status': 'Aktiv',
                'total_profit': 45678.23,
                'today_earnings': 1234.56,
                'progress': 87,
                'config': json.dumps({
                    'exchanges': ['Binance', 'Coinbase', 'Kraken'],
                    'min_profit_threshold': 0.5,
                    'max_trade_amount': 10000
                })
            },
            {
                'name': 'Forex Trading Bot',
                'description': 'KI-gestützter Devisenhandel',
                'bot_type': 'forex',
                'status': 'Aktiv',
                'total_profit': 32145.67,
                'today_earnings': 892.34,
                'progress': 92,
                'config': json.dumps({
                    'currency_pairs': ['EUR/USD', 'GBP/USD', 'USD/JPY'],
                    'risk_level': 'medium',
                    'max_drawdown': 5.0
                })
            },
            {
                'name': 'Affiliate Marketing Bot',
                'description': 'Automatische Affiliate-Kampagnen',
                'bot_type': 'affiliate',
                'status': 'Aktiv',
                'total_profit': 18934.21,
                'today_earnings': 456.78,
                'progress': 76,
                'config': json.dumps({
                    'networks': ['Amazon Associates', 'ClickBank', 'ShareASale'],
                    'target_niches': ['tech', 'finance', 'health'],
                    'daily_budget': 200
                })
            },
            {
                'name': 'Dropshipping Bot',
                'description': 'Produktlistung und Bestellabwicklung',
                'bot_type': 'dropshipping',
                'status': 'Pausiert',
                'total_profit': 28567.89,
                'today_earnings': 723.45,
                'progress': 45,
                'config': json.dumps({
                    'platforms': ['Shopify', 'WooCommerce'],
                    'suppliers': ['AliExpress', 'Oberlo'],
                    'product_categories': ['electronics', 'fashion', 'home']
                })
            },
            {
                'name': 'Social Media Bot',
                'description': 'Automatisierte Content-Monetarisierung',
                'bot_type': 'social',
                'status': 'Aktiv',
                'total_profit': 12345.67,
                'today_earnings': 234.56,
                'progress': 68,
                'config': json.dumps({
                    'platforms': ['Instagram', 'TikTok', 'YouTube'],
                    'content_types': ['videos', 'posts', 'stories'],
                    'posting_frequency': 'daily'
                })
            },
            {
                'name': 'Mining Pool Bot',
                'description': 'Optimierte Krypto-Mining Verwaltung',
                'bot_type': 'mining',
                'status': 'Wartung',
                'total_profit': 56789.12,
                'today_earnings': 1456.78,
                'progress': 0,
                'config': json.dumps({
                    'pools': ['Slush Pool', 'F2Pool', 'Antpool'],
                    'cryptocurrencies': ['Bitcoin', 'Ethereum', 'Litecoin'],
                    'power_cost': 0.12
                })
            }
        ]
        
        # Add bots to database
        for bot_data in bots_data:
            bot = Bot(**bot_data)
            db.session.add(bot)
        
        # Create sample user
        user = User(
            username='admin',
            email='admin@geldmaschine.com'
        )
        db.session.add(user)
        
        # Create today's dashboard metrics
        today = date.today()
        total_profit = sum(bot['total_profit'] for bot in bots_data)
        daily_earnings = sum(bot['today_earnings'] for bot in bots_data)
        active_bots = len([bot for bot in bots_data if bot['status'] == 'Aktiv'])
        
        metrics = DashboardMetrics(
            date=today,
            total_profit=total_profit,
            daily_earnings=daily_earnings,
            active_bots=active_bots,
            success_rate=94.2,
            roi_30_days=287.0
        )
        db.session.add(metrics)
        
        # Create some sample transactions
        sample_transactions = [
            Transaction(
                bot_id=1,
                amount=1234.56,
                transaction_type='earning',
                description='Crypto arbitrage profit',
                timestamp=datetime.utcnow()
            ),
            Transaction(
                bot_id=2,
                amount=892.34,
                transaction_type='earning',
                description='Forex trading profit',
                timestamp=datetime.utcnow()
            ),
            Transaction(
                bot_id=3,
                amount=456.78,
                transaction_type='earning',
                description='Affiliate commission',
                timestamp=datetime.utcnow()
            )
        ]
        
        for transaction in sample_transactions:
            db.session.add(transaction)
        
        # Commit all changes
        db.session.commit()
        
        print("Database seeded successfully!")
        print(f"Created {len(bots_data)} bots")
        print(f"Created 1 user")
        print(f"Created dashboard metrics")
        print(f"Created {len(sample_transactions)} sample transactions")

if __name__ == '__main__':
    from src.main import app
    seed_database(app)
