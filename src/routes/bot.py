from flask import Blueprint, request, jsonify
from src.models.bot import Bot, Transaction, DashboardMetrics, db
from datetime import datetime, date
import json
import random

bot_bp = Blueprint('bot', __name__)

@bot_bp.route('/bots', methods=['GET'])
def get_bots():
    """Get all bots"""
    try:
        bots = Bot.query.all()
        return jsonify([bot.to_dict() for bot in bots]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bot_bp.route('/bots/<int:bot_id>', methods=['GET'])
def get_bot(bot_id):
    """Get a specific bot"""
    try:
        bot = Bot.query.get_or_404(bot_id)
        return jsonify(bot.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bot_bp.route('/bots', methods=['POST'])
def create_bot():
    """Create a new bot"""
    try:
        data = request.get_json()
        
        bot = Bot(
            name=data.get('name'),
            description=data.get('description'),
            bot_type=data.get('bot_type'),
            status=data.get('status', 'Pausiert'),
            config=json.dumps(data.get('config', {}))
        )
        
        db.session.add(bot)
        db.session.commit()
        
        return jsonify(bot.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bot_bp.route('/bots/<int:bot_id>/action', methods=['POST'])
def bot_action(bot_id):
    """Perform action on bot (start, pause, stop)"""
    try:
        bot = Bot.query.get_or_404(bot_id)
        data = request.get_json()
        action = data.get('action')
        
        if action == 'start':
            bot.status = 'Aktiv'
        elif action == 'pause':
            bot.status = 'Pausiert'
        elif action == 'stop':
            bot.status = 'Pausiert'
        elif action == 'maintenance':
            bot.status = 'Wartung'
        
        bot.updated_at = datetime.utcnow()
        db.session.commit()
        
        return jsonify({
            'message': f'Bot {action} successful',
            'bot': bot.to_dict()
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bot_bp.route('/bots/<int:bot_id>/settings', methods=['PUT'])
def update_bot_settings(bot_id):
    """Update bot settings"""
    try:
        bot = Bot.query.get_or_404(bot_id)
        data = request.get_json()
        
        if 'config' in data:
            bot.config = json.dumps(data['config'])
        
        bot.updated_at = datetime.utcnow()
        db.session.commit()
        
        return jsonify(bot.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bot_bp.route('/dashboard/metrics', methods=['GET'])
def get_dashboard_metrics():
    """Get current dashboard metrics"""
    try:
        # Get today's metrics or create if doesn't exist
        today = date.today()
        metrics = DashboardMetrics.query.filter_by(date=today).first()
        
        if not metrics:
            # Calculate metrics from bots
            bots = Bot.query.all()
            total_profit = sum(bot.total_profit for bot in bots)
            daily_earnings = sum(bot.today_earnings for bot in bots)
            active_bots = len([bot for bot in bots if bot.status == 'Aktiv'])
            
            metrics = DashboardMetrics(
                date=today,
                total_profit=total_profit,
                daily_earnings=daily_earnings,
                active_bots=active_bots,
                success_rate=94.2,  # Mock data
                roi_30_days=287.0   # Mock data
            )
            db.session.add(metrics)
            db.session.commit()
        
        return jsonify(metrics.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bot_bp.route('/dashboard/earnings-chart', methods=['GET'])
def get_earnings_chart():
    """Get daily earnings chart data"""
    try:
        # Mock data for daily earnings chart
        chart_data = [
            {'time': '00:00', 'earnings': 0},
            {'time': '04:00', 'earnings': 8000},
            {'time': '08:00', 'earnings': 15000},
            {'time': '12:00', 'earnings': 28000},
            {'time': '16:00', 'earnings': 38000},
            {'time': '20:00', 'earnings': 45000},
            {'time': '24:00', 'earnings': 47523}
        ]
        
        return jsonify(chart_data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bot_bp.route('/transactions', methods=['GET'])
def get_transactions():
    """Get all transactions"""
    try:
        transactions = Transaction.query.order_by(Transaction.timestamp.desc()).all()
        return jsonify([transaction.to_dict() for transaction in transactions]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bot_bp.route('/payout', methods=['POST'])
def request_payout():
    """Request a payout"""
    try:
        data = request.get_json()
        amount = data.get('amount', 0)
        
        # Create a withdrawal transaction
        transaction = Transaction(
            bot_id=1,  # System transaction
            amount=-amount,  # Negative for withdrawal
            transaction_type='withdrawal',
            description=f'Payout request: €{amount}',
            timestamp=datetime.utcnow()
        )
        
        db.session.add(transaction)
        db.session.commit()
        
        return jsonify({
            'message': 'Payout request submitted successfully',
            'transaction': transaction.to_dict()
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bot_bp.route('/simulate-earnings', methods=['POST'])
def simulate_earnings():
    """Simulate earnings for active bots (for demo purposes)"""
    try:
        active_bots = Bot.query.filter_by(status='Aktiv').all()
        
        for bot in active_bots:
            # Simulate random earnings
            earnings = random.uniform(10, 500)
            bot.today_earnings += earnings
            bot.total_profit += earnings
            
            # Update progress randomly
            bot.progress = min(100, bot.progress + random.randint(1, 5))
            
            # Create transaction record
            transaction = Transaction(
                bot_id=bot.id,
                amount=earnings,
                transaction_type='earning',
                description=f'Automated earning from {bot.name}',
                timestamp=datetime.utcnow()
            )
            db.session.add(transaction)
        
        db.session.commit()
        
        return jsonify({
            'message': 'Earnings simulated successfully',
            'updated_bots': len(active_bots)
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
