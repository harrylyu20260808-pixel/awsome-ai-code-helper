"""
Portfolio Manager Application
Portfolio tracking and management with multiple investments
"""

import json
from datetime import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict


@dataclass
class Investment:
    """Single investment entry"""
    ticker: str
    shares: float
    avg_price: float
    current_price: float = 0
    purchase_date: str = ""

    @property
    def total_cost(self) -> float:
        return self.shares * self.avg_price

    @property
    def current_value(self) -> float:
        return self.shares * self.current_price

    @property
    def gain(self) -> float:
        return self.current_value - self.total_cost

    @property
    def gain_percent(self) -> float:
        if self.total_cost == 0:
            return 0
        return (self.gain / self.total_cost) * 100


class PortfolioManager:
    """Portfolio management system"""

    def __init__(self, portfolio_file: str = "portfolio.json"):
        """Initialize portfolio manager"""
        self.portfolio: Dict[str, Investment] = {}
        self.portfolio_file = portfolio_file
        self.load_portfolio()

    def add_investment(self, ticker: str, shares: float, avg_price: float,
                     current_price: float = 0, purchase_date: str = ""):
        """Add investment to portfolio"""
        if ticker in self.portfolio:
            existing = self.portfolio[ticker]
            # Update average price
            total_cost = existing.total_cost + (shares * avg_price)
            total_shares = existing.shares + shares
            existing.avg_price = total_cost / total_shares
            existing.shares = total_shares
        else:
            self.portfolio[ticker] = Investment(
                ticker=ticker,
                shares=shares,
                avg_price=avg_price,
                current_price=current_price,
                purchase_date=purchase_date or datetime.now().strftime("%Y-%m-%d")
            )

    def remove_investment(self, ticker: str, shares: float):
        """Remove investment from portfolio"""
        if ticker in self.portfolio:
            investment = self.portfolio[ticker]
            if investment.shares >= shares:
                investment.shares -= shares
                if investment.shares <= 0:
                    del self.portfolio[ticker]
            else:
                print(f"❌ Not enough shares for {ticker}")

    def update_price(self, ticker: str, current_price: float):
        """Update current price of investment"""
        if ticker in self.portfolio:
            self.portfolio[ticker].current_price = current_price

    def get_total_value(self) -> float:
        """Get total portfolio value"""
        return sum(inv.current_value for inv in self.portfolio.values())

    def get_total_cost(self) -> float:
        """Get total cost basis"""
        return sum(inv.total_cost for inv in self.portfolio.values())

    def get_gain(self) -> float:
        """Get total gain/loss"""
        return self.get_total_value() - self.get_total_cost()

    def get_gain_percent(self) -> float:
        """Get total gain/loss percentage"""
        total_cost = self.get_total_cost()
        if total_cost == 0:
            return 0
        return (self.get_gain() / total_cost) * 100

    def get_portfolio_summary(self) -> Dict:
        """Get portfolio summary"""
        return {
            'total_value': self.get_total_value(),
            'total_cost': self.get_total_cost(),
            'gain': self.get_gain(),
            'gain_percent': self.get_gain_percent(),
            'num_investments': len(self.portfolio),
            'most_valuable': max(self.portfolio.values(), key=lambda x: x.current_value) if self.portfolio else None
        }

    def print_portfolio(self):
        """Print portfolio summary"""
        print("\n" + "="*70)
        print("💼 Portfolio Summary")
        print("="*70)

        if not self.portfolio:
            print("Empty portfolio")
            return

        print(f"\n{'Ticker':<10} {'Shares':<10} {'Avg Price':<12} {'Current':<12} "
              f"{'Value':<12} {'Gain':<12} {'%':<10}")
        print("-"*70)

        total_value = 0
        total_cost = 0

        for ticker, investment in self.portfolio.items():
            value = investment.current_value
            cost = investment.total_cost
            gain = investment.gain
            gain_percent = investment.gain_percent

            print(f"{ticker:<10} {investment.shares:<10} ${investment.avg_price:<11.2f} "
                  f"${investment.current_price:<11.2f} ${value:<11.2f} ${gain:<11.2f} "
                  f"{gain_percent:>9.2f}%")

            total_value += value
            total_cost += cost

        print("-"*70)
        summary = self.get_portfolio_summary()
        print(f"Total Value: ${summary['total_value']:.2f}")
        print(f"Total Cost: ${summary['total_cost']:.2f}")
        print(f"Total Gain: ${summary['gain']:.2f} ({summary['gain_percent']:.2f}%)")
        print("="*70 + "\n")

    def save_portfolio(self):
        """Save portfolio to file"""
        data = {
            'last_updated': datetime.now().isoformat(),
            'portfolio': [asdict(inv) for inv in self.portfolio.values()]
        }
        with open(self.portfolio_file, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"✅ Portfolio saved to {self.portfolio_file}")

    def load_portfolio(self):
        """Load portfolio from file"""
        try:
            with open(self.portfolio_file, 'r') as f:
                data = json.load(f)
                for item in data.get('portfolio', []):
                    self.portfolio[item['ticker']] = Investment(**item)
                print(f"✅ Portfolio loaded from {self.portfolio_file}")
        except FileNotFoundError:
            print("⚠️ Portfolio file not found, starting fresh")
        except json.JSONDecodeError:
            print("⚠️ Invalid portfolio file, starting fresh")


class SectorAllocation:
    """Sector allocation analysis"""

    def __init__(self):
        self.sectors = {}

    def add_sector(self, ticker: str, sector: str, value: float):
        """Add sector allocation"""
        if sector not in self.sectors:
            self.sectors[sector] = 0
        self.sectors[sector] += value

    def print_sector_allocation(self):
        """Print sector allocation"""
        print("\n" + "="*70)
        print("📊 Sector Allocation")
        print("="*70)

        total = sum(self.sectors.values())
        if total == 0:
            print("No sector data")
            return

        print(f"\n{'Sector':<20} {'Value':<15} {'Percent':<15}")
        print("-"*70)

        sorted_sectors = sorted(self.sectors.items(), key=lambda x: x[1], reverse=True)

        for sector, value in sorted_sectors:
            percent = (value / total) * 100
            print(f"{sector:<20} ${value:<14.2f} {percent:>14.2f}%")

        print("="*70 + "\n")


# Usage example
if __name__ == "__main__":
    portfolio = PortfolioManager()

    # Simulate adding investments
    print("Adding investments...")
    portfolio.add_investment("AAPL", 100, 150.00, 175.50)
    portfolio.add_investment("GOOGL", 50, 120.00, 140.20)
    portfolio.add_investment("MSFT", 25, 300.00, 330.75)
    portfolio.add_investment("AMZN", 30, 110.00, 138.90)

    portfolio.print_portfolio()

    # Sector allocation
    sector_alloc = SectorAllocation()
    sector_alloc.add_sector("Technology", 52575.00, 1)
    sector_alloc.add_sector("Healthcare", 3140.50, 1)
    sector_alloc.add_sector("Finance", 5167.50, 1)

    sector_alloc.print_sector_allocation()

    # Save portfolio
    portfolio.save_portfolio()

    print("✨ Portfolio manager completed!")
