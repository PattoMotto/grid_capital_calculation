# PARAMETERS
GRID_TOP            = 3_000.00
GRID_BOTTOM         = 1_500.00
PRICE_TARGET        = 1_500.00
CURRENT_PRICE       = GRID_TOP
GRID_GAP            = 5.00
LOT_SIZE            = 0.01

DIGITS              = 2
PIP_VALUE_PER_LOT   = 10.00

PIP_VALUE_PER_TRADE = PIP_VALUE_PER_LOT * LOT_SIZE
PROFIT_PER_GAP      = PIP_VALUE_PER_TRADE * GRID_GAP * pow(10, DIGITS - 1)

def drawdown_calculation(target_price: float):
    current_level = max(GRID_BOTTOM, target_price)

    total_pip = 0
    drawdown_in_usc = 0
    while current_level < GRID_TOP:
        entry_price = min(CURRENT_PRICE, current_level)
        total_pip += (entry_price - target_price)
        current_level += GRID_GAP

    drawdown_in_usc = total_pip * pow(10, DIGITS - 1) * PIP_VALUE_PER_TRADE
    drawdown_in_usd = drawdown_in_usc * 0.01

    print("Drawdown at price $ {price:,.2f} is $ {drawdown:,.2f}".format(price = target_price, drawdown = drawdown_in_usd))

drawdown_calculation(0)
drawdown_calculation(PRICE_TARGET)