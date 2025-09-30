from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from src.models.user import db

class Bot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    bot_type = db.Column(db.String(50), nullable=False)  # crypto, forex, affiliate, dropshipping, social, mining
    status = db.Column(db.String(20), default='Pausiert')  # Aktiv, Pausiert, Wartung
    total_profit = db.Column(db.Float, default=0.0)
    today_earnings = db.Column(db.Float, default=0.0)
    progress = db.Column(db.Integer, default=0)  # 0-100%
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Configuration settings (JSON stored as text)
    config = db.Column(db.Text)  # JSON string for bot-specific configuration
    
    def __repr__(self):
        return f'<Bot {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'bot_type': self.bot_type,
            'status': self.status,
            'total_profit': self.total_profit,
            'today_earnings': self.today_earnings,
            'progress': self.progress,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'config': self.config
        }

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bot_id = db.Column(db.Integer, db.ForeignKey('bot.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    transaction_type = db.Column(db.String(20), nullable=False)  # earning, withdrawal, deposit
    description = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    bot = db.relationship('Bot', backref=db.backref('transactions', lazy=True))
    
    def __repr__(self):
        return f'<Transaction {self.id}: {self.amount}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'bot_id': self.bot_id,
            'amount': self.amount,
            'transaction_type': self.transaction_type,
            'description': self.description,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None
        }

class DashboardMetrics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, unique=True)
    total_profit = db.Column(db.Float, default=0.0)
    daily_earnings = db.Column(db.Float, default=0.0)
    active_bots = db.Column(db.Integer, default=0)
    success_rate = db.Column(db.Float, default=0.0)
    roi_30_days = db.Column(db.Float, default=0.0)
    
    def __repr__(self):
        return f'<DashboardMetrics {self.date}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date.isoformat() if self.date else None,
            'total_profit': self.total_profit,
            'daily_earnings': self.daily_earnings,
            'active_bots': self.active_bots,
            'success_rate': self.success_rate,
            'roi_30_days': self.roi_30_days
        }
