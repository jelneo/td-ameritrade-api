from enum import Enum


class Direction(Enum):
    """Represents the direction options for the
    `Movers` service.

    ### Usage
    ----
        >>> from td.enums import Directions
        >>> Directions.Up.value
    """

    Up = 'up'
    Down = 'down'


class Change(Enum):
    """Represents the change options for the
    `Movers` service.

    ### Usage
    ----
        >>> from td.enums import Change
        >>> Change.Percent.value
    """

    Percent = 'percent'
    Value = 'value'


class TransactionTypes(Enum):
    """Represents the types of transaction you
    can query from TD Ameritrade using the `Accounts`
    services.

    ### Usage
    ----
        >>> from td.enums import TransactionTypes
        >>> TransactionTypes.Trade.value
    """

    All = 'ALL'
    Trade = 'TRADE'
    BuyOnly = 'BUY_ONLY'
    SellOnly = 'SELL_ONLY'
    CashInOrCashOut = 'CASH_IN_OR_CASH_OUT'
    Checking = 'CHECKING'
    Dividend = 'DIVIDEND'
    Interest = 'INTEREST'
    Other = 'OTHER'
    AdvisorFees = 'ADVISOR_FEES'


class Markets(Enum):
    """Represents the different markets you can request
    hours for the `MarketHours` service.

    ### Usage
    ----
        >>> from td.enums import Markets
        >>> Markets.Bond.Value
    """

    Bond = 'BOND'
    Equity = 'EQUITY'
    Option = 'OPTION'
    Forex = 'FOREX'
    Futures = 'FUTURES'


class Projections(Enum):
    """Represents the different search types you can use for
    the `Instruments` service.

    ### Usage
    ----
        >>> from td.enums import Projections
        >>> Projections.Bond.Value
    """

    SymbolSearch = 'symbol-search'
    SymbolRegex = 'symbol-regex'
    DescriptionSearch = 'desc-search'
    DescriptionRegex = 'desc-regex'
    Fundamental = 'fundamental'


class DefaultOrderLegInstruction(Enum):
    """Represents the different Default Order Leg Instructions
    for the `UserInfo` service.

    ### Usage
    ----
        >>> from td.enums import DefaultOrderLegInstruction
        >>> DefaultOrderLegInstruction.Sell.Value
    """

    Buy = 'BUY'
    Sell = 'SELL'
    BuyToCover = 'BUY_TO_COVER'
    SellShort = 'SELL_SHORT'
    NoneSpecified = 'NONE'


class DefaultOrderType(Enum):
    """Represents the different Default Order Type
    for the `UserInfo` service.

    ### Usage
    ----
        >>> from td.enums import DefaultOrderType
        >>> DefaultOrderType.Market.Value
    """

    Market = 'MARKET'
    Limit = 'LIMIT'
    Stop = 'STOP'
    StopLimit = 'STOP_LIMIT'
    TrailingStop = 'TRAILING_STOP'
    MarketOnClose = 'MARKET_ON_CLOSE'
    NoneSpecified = 'NONE'


class DefaultOrderPriceLinkType(Enum):
    """Represents the different Default Order Price Link Type
    for the `UserInfo` service.

    ### Usage
    ----
        >>> from td.enums import DefaultOrderPriceLinkType
        >>> DefaultOrderPriceLinkType.Value.Value
    """

    Value = 'VALUE'
    Percent = 'PERCENT'
    NoneSpecified = 'NONE'


class DefaultOrderDuration(Enum):
    """Represents the different Default Order Duration
    for the `UserInfo` service.

    ### Usage
    ----
        >>> from td.enums import DefaultOrderDuration
        >>> DefaultOrderDuration.Day.Value
    """

    Day = 'DAY'
    GoodTillCancel = 'GOOD_TILL_CANCEL'
    NoneSpecified = 'NONE'


class DefaultOrderMarketSession(Enum):
    """Represents the different Default Order Market Session
    for the `UserInfo` service.

    ### Usage
    ----
        >>> from td.enums import DefaultOrderMarketSession
        >>> DefaultOrderMarketSession.Day.Value
    """

    Am = 'AM'
    Pm = 'PM'
    Normal = 'NORMAL'
    Seamless = 'SEAMLESS'
    NoneSpecified = 'NONE'


class TaxLotMethod(Enum):
    """Represents the different Tax Lot Methods
    for the `UserInfo` service.

    ### Usage
    ----
        >>> from td.enums import MutualFundTaxLotMethod
        >>> MutualFundTaxLotMethod.Day.Value
    """

    Fifo = 'FIFO'
    Lifo = 'LIFO'
    HighCost = 'HIGH_COST'
    LowCost = 'LOW_COST'
    MinimumTax = 'MINIMUM_TAX'
    AverageCost = 'AVERAGE_COST'
    NoneSpecified = 'NONE'


class DefaultAdvancedToolLaunch(Enum):
    """Represents the different Default Advanced Tool
    Lauch for the `UserInfo` service.

    ### Usage
    ----
        >>> from td.enums import DefaultAdvancedToolLaunch
        >>> DefaultAdvancedToolLaunch.Tos.Value
    """

    Ta = 'Ta'
    No = 'N'
    Yes = 'Y'
    Tos = 'TOS'
    Cc2 = 'CC2'
    NoneSpecified = 'NONE'


class AuthTokenTimeout(Enum):
    """Represents the different Auth Token Timeout
    properties for the `UserInfo` service.

    ### Usage
    ----
        >>> from td.enums import AuthTokenTimeout
        >>> AuthTokenTimeout.FiftyFiveMinutes.Value
    """

    FiftyFiveMinutes = 'FIFTY_FIVE_MINUTES'
    TwoHours = 'TWO_HOURS'
    FourHours = 'FOUR_HOURS'
    EightHours = 'EIGHT_HOURS'


class FrequencyType(Enum):
    """Represents the different chart frequencies
    for the `PriceHistory` service.

    ### Usage
    ----
        >>> from td.enums import PriceFrequency
        >>> PriceFrequency.Daily.Value
    """

    Minute = 'minute'
    Daily = 'daily'
    Weekly = 'weekly'
    Monthly = 'monthly'


class PeriodType(Enum):
    """Represents the different chart periods
    for the `PriceHistory` service.

    ### Usage
    ----
        >>> from td.enums import PriceFrequency
        >>> PeriodType.Daily.Value
    """

    Day = 'day'
    Month = 'month'
    Year = 'year'
    YearToDate = 'ytd'


class StrategyType(Enum):
    """Represents the different strategy types
    when querying the `OptionChain` service.

    ### Usage
    ----
        >>> from td.enums import StrategyType
        >>> StrategyType.Analytical.Value
    """

    Analytical = 'ANALYTICAL'
    Butterfly = 'BUTTERFLY'
    Calendar = 'CALENDAR'
    Collar = 'COLLAR'
    Condor = 'CONDOR'
    Covered = 'COVERED'
    Diagonal = 'DIAGONAL'
    Roll = 'ROLL'
    Single = 'SINGLE'
    Straddle = 'STRADDLE'
    Strangle = 'STRANGLE'
    Vertical = 'VERTICAL'


class OptionaRange(Enum):
    """Represents the different option range types
    when querying the `OptionChain` service.

    ### Usage
    ----
        >>> from td.enums import OptionaRange
        >>> OptionaRange.InTheMoney.Value
    """

    All = 'ALL'
    InTheMoney = 'ITM'
    NearTheMoney = 'NTM'
    OutTheMoney = 'OTM'
    StrikesAboveMarket = 'SAK'
    StrikesBelowMarket = 'SBK'
    StrikesNearMarket = 'SNK'


class ExpirationMonth(Enum):
    """Represents the different option expiration months
    when querying the `OptionChain` service.

    ### Usage
    ----
        >>> from td.enums import ExpirationMonth
        >>> ExpirationMonth.Janurary.Value
    """

    All = 'ALL'
    Janurary = 'JAN'
    Feburary = 'FEB'
    March = 'MAR'
    April = 'April'
    May = 'MAY'
    June = 'JUN'
    July = 'JUL'
    August = 'AUG'
    September = 'SEP'
    October = 'OCT'
    November = 'NOV'
    December = 'DEC'


class ContractType(Enum):
    """Represents the different option contract types
    when querying the `OptionChain` service.

    ### Usage
    ----
        >>> from td.enums import ContractType
        >>> ContractType.Call.Value
    """

    All = 'ALL'
    Call = 'CALL'
    Put = 'PUT'


class OptionType(Enum):
    """Represents the different option types
    when querying the `OptionChain` service.

    ### Usage
    ----
        >>> from td.enums import OptionType
        >>> OptionType.Call.Value
    """

    All = 'ALL'
    StandardContracts = 'S'
    NonStandardContracts = 'NS'
