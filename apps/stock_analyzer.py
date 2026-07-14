"""
Stock Market Analysis Application
Comprehensive stock data analysis and visualization tool
"""

import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import json
from typing import Dict, List, Optional

class StockAnalyzer:
    """Stock Market Analysis Tool"""

    def __init__(self, api_key: str = None):
        """Initialize stock analyzer"""
        self.api_key = api_key
        self.base_url = "https://www.alphavantage.co/query"
        self.history = []
        self.daily_data = []

    def get_stock_data(self, symbol: str, function: str = "TIME_SERIES_DAILY",
                      interval: str = "daily") -> Dict:
        """Get stock data from Alpha Vantage API"""
        params = {
            "function": function,
            "symbol": symbol,
            "outputsize": "full",
            "apikey": self.api_key
        }

        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()

            if "Error Message" in data:
                print(f"Error: {data['Error Message']}")
                return {}

            if "Time Series (Daily)" in data:
                return data["Time Series (Daily)"]
            else:
                print(f"Unexpected data format: {list(data.keys())}")
                return {}

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return {}

    def calculate_rsi(self, prices: List[float], period: int = 14) -> float:
        """Calculate Relative Strength Index"""
        if len(prices) < period + 1:
            return 0

        gains = []
        losses = []

        for i in range(1, len(prices)):
            change = prices[i] - prices[i-1]
            if change > 0:
                gains.append(change)
            else:
                losses.append(abs(change))

        avg_gain = sum(gains) / period
        avg_loss = sum(losses) / period

        if avg_loss == 0:
            return 100

        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    def calculate_sma(self, prices: List[float], period: int) -> float:
        """Calculate Simple Moving Average"""
        if len(prices) < period:
            return 0
        return sum(prices[-period:]) / period

    def calculate_ema(self, prices: List[float], period: int) -> float:
        """Calculate Exponential Moving Average"""
        if len(prices) < period:
            return prices[0] if prices else 0

        multiplier = 2 / (period + 1)
        ema = prices[period-1]

        for price in prices[period:]:
            ema = (price * multiplier) + (ema * (1 - multiplier))

        return ema

    def analyze_stock(self, symbol: str, days: int = 90) -> Dict:
        """Comprehensive stock analysis"""
        print(f"🔍 Analyzing {symbol}...")
        print("-" * 60)

        # Get stock data
        data = self.get_stock_data(symbol)
        if not data:
            return {}

        # Convert to DataFrame
        dates = []
        prices = []

        for date, info in sorted(data.items()):
            dates.append(datetime.strptime(date, "%Y-%m-%d"))
            prices.append(float(info['4. close']))

        # Calculate indicators
        current_price = prices[-1]
        price_7d_ago = prices[-7]
        price_30d_ago = prices[-30]
        price_90d_ago = prices[-90]

        price_change_7d = ((current_price - price_7d_ago) / price_7d_ago) * 100
        price_change_30d = ((current_price - price_30d_ago) / price_30d_ago) * 100
        price_change_90d = ((current_price - price_90d_ago) / price_90d_ago) * 100

        sma_20 = self.calculate_sma(prices, 20)
        sma_50 = self.calculate_sma(prices, 50)
        sma_200 = self.calculate_sma(prices, 200)

        ema_12 = self.calculate_ema(prices, 12)
        ema_26 = self.calculate_ema(prices, 26)

        high_52w = max(prices[-252:]) if len(prices) >= 252 else max(prices)
        low_52w = min(prices[-252:]) if len(prices) >= 252 else min(prices)
        range_52w = ((current_price - low_52w) / low_52w) * 100

        # Generate analysis
        analysis = {
            "symbol": symbol,
            "current_price": current_price,
            "price_change_7d": price_change_7d,
            "price_change_30d": price_change_30d,
            "price_change_90d": price_change_90d,
            "sma_20": sma_20,
            "sma_50": sma_50,
            "sma_200": sma_200,
            "ema_12": ema_12,
            "ema_26": ema_26,
            "high_52w": high_52w,
            "low_52w": low_52w,
            "range_52w": range_52w,
            "date_range": [dates[0].strftime("%Y-%m-%d"), dates[-1].strftime("%Y-%m-%d")]
        }

        # Generate insights
        insights = []

        # Price movement
        if price_change_7d > 5:
            insights.append(f"📈 Strong bullish 7-day performance ({price_change_7d:.2f}%)")
        elif price_change_7d < -5:
            insights.append(f"📉 Strong bearish 7-day performance ({price_change_7d:.2f}%)")
        else:
            insights.append(f"📊 Neutral 7-day performance ({price_change_7d:.2f}%)")

        # 30-day trend
        if price_change_30d > 10:
            insights.append("✅ Positive 30-day trend")
        elif price_change_30d < -10:
            insights.append("⚠️ Negative 30-day trend")
        else:
            insights.append("➡️ Stable 30-day trend")

        # Moving average analysis
        if current_price > sma_20 and current_price > sma_50:
            insights.append("✅ Above both SMA 20 and SMA 50")
        elif current_price < sma_20 and current_price < sma_50:
            insights.append("❌ Below both SMA 20 and SMA 50")
        else:
            insights.append("⏳ Between SMA 20 and SMA 50")

        # 52-week range
        if range_52w > 30:
            insights.append(f"🔥 Strong relative strength ({range_52w:.2f}% above 52-week low)")
        elif range_52w < -30:
            insights.append(f"💔 Weak relative strength ({range_52w:.2f}% below 52-week high)")
        else:
            insights.append("⚖️ Moderate 52-week range position")

        analysis["insights"] = insights
        analysis["trend"] = self._determine_trend(prices)
        analysis["support_levels"] = self._calculate_support_resistance(prices)
        analysis["volatility"] = self._calculate_volatility(prices)

        return analysis

    def _determine_trend(self, prices: List[float]) -> str:
        """Determine price trend"""
        if len(prices) < 20:
            return "Insufficient data"

        recent = prices[-10:]
        if sum(recent[i] > recent[i-1] for i in range(1, len(recent))) > 7:
            return "Strong Uptrend"
        elif sum(recent[i] > recent[i-1] for i in range(1, len(recent))) > 4:
            return "Mild Uptrend"
        elif sum(recent[i] > recent[i-1] for i in range(1, len(recent))) < 3:
            return "Strong Downtrend"
        else:
            return "Sideways"

    def _calculate_support_resistance(self, prices: List[float]) -> Dict:
        """Calculate support and resistance levels"""
        if len(prices) < 20:
            return {}

        # Simple analysis using recent highs and lows
        recent_high = max(prices[-20:])
        recent_low = min(prices[-20:])
        avg = sum(prices) / len(prices)

        resistance = recent_high + (recent_high - recent_low) * 0.1
        support = recent_low - (recent_high - recent_low) * 0.1

        return {
            "resistance": resistance,
            "support": support,
            "pivot": (resistance + support) / 2,
            "average": avg
        }

    def _calculate_volatility(self, prices: List[float]) -> float:
        """Calculate volatility (standard deviation)"""
        if len(prices) < 2:
            return 0

        avg = sum(prices) / len(prices)
        variance = sum((p - avg) ** 2 for p in prices) / len(prices)
        return variance ** 0.5

    def create_chart(self, symbol: str, days: int = 90):
        """Create price chart with indicators"""
        data = self.get_stock_data(symbol)

        if not data:
            print(f"❌ No data available for {symbol}")
            return

        # Prepare data
        dates = []
        prices = []
        volumes = []

        for date, info in sorted(data.items()):
            if len(dates) >= days:
                break
            dates.append(date)
            prices.append(float(info['4. close']))
            volumes.append(int(info['5. volume']))

        # Create chart
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

        # Price chart
        ax1.plot(dates, prices, linewidth=2, color='#1f77b4', label='Price')
        ax1.set_ylabel('Price ($)', fontsize=12)
        ax1.set_title(f'{symbol} Stock Price & Volume Analysis', fontsize=14, fontweight='bold')
        ax1.grid(True, linestyle='--', alpha=0.7)
        ax1.legend()

        # Volume chart
        colors = ['#2ecc71' if prices[i] >= prices[i-1] else '#e74c3c']
        ax2.bar(dates, volumes, color=colors, alpha=0.6)
        ax2.set_xlabel('Date', fontsize=12)
        ax2.set_ylabel('Volume', fontsize=12)
        ax2.grid(True, linestyle='--', alpha=0.7)

        # Add indicators
        sma_20 = self.calculate_sma(prices, 20)
        sma_50 = self.calculate_sma(prices, 50)
        sma_200 = self.calculate_sma(prices, 200)

        ax1.axhline(y=sma_20, color='orange', linestyle='--', linewidth=1, label='SMA 20')
        ax1.axhline(y=sma_50, color='purple', linestyle='--', linewidth=1, label='SMA 50')
        ax1.axhline(y=sma_200, color='green', linestyle='--', linewidth=1, label='SMA 200')

        plt.tight_layout()

        # Save
        filename = f"{symbol}_chart.png"
        plt.savefig(filename, dpi=150, bbox_inches='tight')
        plt.close()

        print(f"✅ Chart saved to {filename}")

    def compare_stocks(self, symbols: List[str]):
        """Compare multiple stocks"""
        print("\n" + "="*70)
        print("📊 Stock Comparison Analysis")
        print("="*70)
        print(f"\n{'Symbol':<12} {'Current':<10} {'7d %':<10} {'30d %':<10} {'Trend':<20} {'Volatility':<12}")
        print("-"*70)

        results = {}
        for symbol in symbols:
            analysis = self.analyze_stock(symbol)
            if analysis:
                results[symbol] = {
                    'price': analysis['current_price'],
                    'change_7d': analysis['price_change_7d'],
                    'change_30d': analysis['price_change_30d'],
                    'trend': analysis['trend'],
                    'volatility': analysis['volatility']
                }

                print(f"{symbol:<12} ${analysis['current_price']:<9.2f} "
                      f"{analysis['price_change_7d']:>8.2f}% "
                      f"{analysis['price_change_30d']:>8.2f}% "
                      f"{analysis['trend']:<20} "
                      f"{analysis['volatility']:<11.2f}")

        print("="*70 + "\n")
        return results


class PortfolioManager:
    """Portfolio Management Tool"""

    def __init__(self):
        """Initialize portfolio manager"""
        self.portfolio = {}

    def add_stock(self, symbol: str, shares: int, purchase_price: float):
        """Add stock to portfolio"""
        if symbol not in self.portfolio:
            self.portfolio[symbol] = {'shares': 0, 'avg_price': 0}

        old_total = self.portfolio[symbol]['shares'] * self.portfolio[symbol]['avg_price']
        new_total = shares * purchase_price
        new_avg_price = (old_total + new_total) / (self.portfolio[symbol]['shares'] + shares)

        self.portfolio[symbol]['shares'] += shares
        self.portfolio[symbol]['avg_price'] = new_avg_price

    def remove_stock(self, symbol: str, shares: int):
        """Remove stock from portfolio"""
        if symbol in self.portfolio:
            if self.portfolio[symbol]['shares'] >= shares:
                self.portfolio[symbol]['shares'] -= shares
                if self.portfolio[symbol]['shares'] == 0:
                    del self.portfolio[symbol]
            else:
                print("❌ Not enough shares to sell")

    def get_portfolio_value(self, prices: Dict[str, float]) -> float:
        """Get total portfolio value"""
        total = 0
        for symbol, holdings in self.portfolio.items():
            total += holdings['shares'] * prices.get(symbol, 0)
        return total

    def get_portfolio_performance(self, prices: Dict[str, float]) -> Dict:
        """Get portfolio performance metrics"""
        total_value = self.get_portfolio_value(prices)
        total_cost = 0
        shares = 0

        for symbol, holdings in self.portfolio.items():
            total_cost += holdings['shares'] * holdings['avg_price']
            shares += holdings['shares']

        if total_cost == 0:
            return {}

        total_gain = total_value - total_cost
        total_gain_percent = (total_gain / total_cost) * 100

        return {
            'total_value': total_value,
            'total_cost': total_cost,
            'total_gain': total_gain,
            'total_gain_percent': total_gain_percent,
            'num_stocks': len(self.portfolio),
            'total_shares': shares
        }

    def print_portfolio(self, prices: Dict[str, float]):
        """Print portfolio summary"""
        print("\n" + "="*70)
        print("💼 Portfolio Summary")
        print("="*70)

        if not self.portfolio:
            print("Empty portfolio")
            return

        print(f"\n{'Symbol':<12} {'Shares':<10} {'Avg Price':<15} {'Current':<15} {'Value':<12} {'Gain':<10}")
        print("-"*70)

        portfolio_value = 0
        total_cost = 0

        for symbol, holdings in self.portfolio.items():
            shares = holdings['shares']
            avg_price = holdings['avg_price']
            current_price = prices.get(symbol, avg_price)

            value = shares * current_price
            cost = shares * avg_price
            gain = value - cost
            gain_percent = (gain / cost * 100) if cost != 0 else 0

            print(f"{symbol:<12} {shares:<10} ${avg_price:<14.2f} ${current_price:<14.2f} "
                  f"${value:<11.2f} ${gain:<9.2f} ({gain_percent:>6.2f}%)")

            portfolio_value += value
            total_cost += cost

        print("-"*70)

        performance = self.get_portfolio_performance(prices)
        print(f"Total Value: ${portfolio_value:.2f}")
        print(f"Total Cost: ${total_cost:.2f}")
        print(f"Total Gain: ${performance.get('total_gain', 0):.2f} "
              f"({performance.get('total_gain_percent', 0):.2f}%)")
        print("="*70 + "\n")


# Usage examples
if __name__ == "__main__":
    # Stock Analyzer
    analyzer = StockAnalyzer(api_key="demo")

    # Analyze single stock
    analysis = analyzer.analyze_stock("AAPL", days=90)
    if analysis:
        print(f"\n📊 {analysis['symbol']} Analysis")
        print(f"Current Price: ${analysis['current_price']:.2f}")
        print(f"7-Day Change: {analysis['price_change_7d']:.2f}%")
        print(f"30-Day Change: {analysis['price_change_30d']:.2f}%")
        print(f"Insights: {', '.join(analysis['insights'])}")

    # Create chart
    analyzer.create_chart("AAPL")

    # Compare multiple stocks
    analyzer.compare_stocks(["AAPL", "GOOGL", "MSFT", "AMZN"])

    # Portfolio Manager
    print("\n💼 Portfolio Management Demo")
    print("-" * 40)
    portfolio = PortfolioManager()

    # Simulate some data
    prices = {
        "AAPL": 175.50,
        "GOOGL": 140.20,
        "MSFT": 330.75,
        "AMZN": 138.90
    }

    portfolio.add_stock("AAPL", 100, 150.00)
    portfolio.add_stock("GOOGL", 50, 120.00)
    portfolio.add_stock("MSFT", 25, 300.00)

    portfolio.print_portfolio(prices)

    print("✨ Stock analyzer completed!")
