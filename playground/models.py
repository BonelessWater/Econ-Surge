from django.db import models

currency_values = [
    ("AED",	"United Arab Emirates Dirham"),
    ("AFN",	"Afghan Afghani"),
    ("ALL",	"Albanian Lek"),
    ("AMD",	"Armenian Dram"),
    ("ANG",	"Netherlands Antillean Guilder"),
    ("AOA",	"Angolan Kwanza"),
    ("ARS",	"Argentine Peso"),
    ("AUD",	"Australian Dollar"),
    ("AWG",	"Aruban Florin"),
    ("AZN",	"Azerbaijani Manat"),
    ("BAM",	"Bosnia-Herzegovina Convertible Mark"),
    ("BBD",	"Barbadian Dollar"),
    ("BDT",	"Bangladeshi Taka"),
    ("BGN",	"Bulgarian Lev"),
    ("BHD",	"Bahraini Dinar"),
    ("BIF",	"Burundian Franc"),
    ("BMD",	"Bermudan Dollar"),
    ("BND",	"Brunei Dollar"),
    ("BOB",	"Bolivian Boliviano"),
    ("BRL",	"Brazilian Real"),
    ("BSD",	"Bahamian Dollar"),
    ("BTN",	"Bhutanese Ngultrum"),
    ("BWP",	"Botswanan Pula"),
    ("BZD",	"Belize Dollar"),
    ("CAD",	"Canadian Dollar"),
    ("CDF",	"Congolese Franc"),
    ("CHF",	"Swiss Franc"),
    ("CLF",	"Chilean Unit of Account UF"),
    ("CLP",	"Chilean Peso"),
    ("CNH",	"Chinese Yuan Offshore"),
    ("CNY",	"Chinese Yuan"),
    ("COP",	"Colombian Peso"),
    ("CUP",	"Cuban Peso"),
    ("CVE",	"Cape Verdean Escudo"),
    ("CZK",	"Czech Republic Koruna"),
    ("DJF",	"Djiboutian Franc"),
    ("DKK",	"Danish Krone"),
    ("DOP",	"Dominican Peso"),
    ("DZD",	"Algerian Dinar"),
    ("EGP",	"Egyptian Pound"),
    ("ERN",	"Eritrean Nakfa"),
    ("ETB",	"Ethiopian Birr"),
    ("EUR",	"Euro"),
    ("FJD",	"Fijian Dollar"),
    ("FKP",	"Falkland Islands Pound"),
    ("GBP",	"British Pound Sterling"),
    ("GEL",	"Georgian Lari"),
    ("GHS",	"Ghanaian Cedi"),
    ("GIP",	"Gibraltar Pound"),
    ("GMD",	"Gambian Dalasi"),
    ("GNF",	"Guinean Franc"),
    ("GTQ",	"Guatemalan Quetzal"),
    ("GYD",	"Guyanaese Dollar"),
    ("HKD",	"Hong Kong Dollar"),
    ("HNL",	"Honduran Lempira"),
    ("HRK",	"Croatian Kuna"),
    ("HTG",	"Haitian Gourde"),
    ("HUF",	"Hungarian Forint"),
    ("ICP",	"Internet Computer"),
    ("IDR",	"Indonesian Rupiah"),
    ("ILS",	"Israeli New Sheqel"),
    ("INR",	"Indian Rupee"),
    ("IQD",	"Iraqi Dinar"),
    ("IRR",	"Iranian Rial"),
    ("ISK",	"Icelandic Krona"),
    ("JEP",	"Jersey Pound"),
    ("JMD",	"Jamaican Dollar"),
    ("JOD",	"Jordanian Dinar"),
    ("JPY",	"Japanese Yen"),
    ("KES",	"Kenyan Shilling"),
    ("KGS",	"Kyrgystani Som"),
    ("KHR",	"Cambodian Riel"),
    ("KMF",	"Comorian Franc"),
    ("KPW",	"North Korean Won"),
    ("KRW",	"South Korean Won"),
    ("KWD",	"Kuwaiti Dinar"),
    ("KYD",	"Cayman Islands Dollar"),
    ("KZT",	"Kazakhstani Tenge"),
    ("LAK",	"Laotian Kip"),
    ("LBP",	"Lebanese Pound"),
    ("LKR",	"Sri Lankan Rupee"),
    ("LRD",	"Liberian Dollar"),
    ("LSL",	"Lesotho Loti"),
    ("LYD",	"Libyan Dinar"),
    ("MAD",	"Moroccan Dirham"),
    ("MDL",	"Moldovan Leu"),
    ("MGA",	"Malagasy Ariary"),
    ("MKD",	"Macedonian Denar"),
    ("MMK",	"Myanma Kyat"),
    ("MNT",	"Mongolian Tugrik"),
    ("MOP",	"Macanese Pataca"),
    ("MRO",	"Mauritanian Ouguiya (pre-2018)"),
    ("MRU",	"Mauritanian Ouguiya"),
    ("MUR",	"Mauritian Rupee"),
    ("MVR",	"Maldivian Rufiyaa"),
    ("MWK",	"Malawian Kwacha"),
    ("MXN",	"Mexican Peso"),
    ("MYR",	"Malaysian Ringgit"),
    ("MZN",	"Mozambican Metical"),
    ("NAD",	"Namibian Dollar"),
    ("NGN",	"Nigerian Naira"),
    ("NOK",	"Norwegian Krone"),
    ("NPR",	"Nepalese Rupee"),
    ("NZD",	"New Zealand Dollar"),
    ("OMR",	"Omani Rial"),
    ("PAB",	"Panamanian Balboa"),
    ("PEN",	"Peruvian Nuevo Sol"),
    ("PGK",	"Papua New Guinean Kina"),
    ("PHP",	"Philippine Peso"),
    ("PKR",	"Pakistani Rupee"),
    ("PLN",	"Polish Zloty"),
    ("PYG",	"Paraguayan Guarani"),
    ("QAR",	"Qatari Rial"),
    ("RON",	"Romanian Leu"),
    ("RSD",	"Serbian Dinar"),
    ("RUB",	"Russian Ruble"),
    ("RUR",	"Old Russian Ruble"),
    ("RWF",	"Rwandan Franc"),
    ("SAR",	"Saudi Riyal"),
    ("SBD","	Solomon Islands Dollar"),
    ("SCR",	"Seychellois Rupee"),
    ("SDG",	"Sudanese Pound"),
    ("SDR",	"Special Drawing Rights"),
    ("SEK",	"Swedish Krona"),
    ("SGD",	"Singapore Dollar"),
    ("SHP",	"Saint Helena Pound"),
    ("SLL",	"Sierra Leonean Leone"),
    ("SOS",	"Somali Shilling"),
    ("SRD",	"Surinamese Dollar"),
    ("SYP",	"Syrian Pound"),
    ("SZL",	"Swazi Lilangeni"),
    ("THB",	"Thai Baht"),
    ("TJS",	"Tajikistani Somoni"),
    ("TMT",	"Turkmenistani Manat"),
    ("TND",	"Tunisian Dinar"),
    ("TOP",	"Tongan Pa'anga"),
    ("TRY",	"Turkish Lira"),
    ("TTD",	"Trinidad and Tobago Dollar"),
    ("TWD",	"New Taiwan Dollar"),
    ("TZS",	"Tanzanian Shilling"),
    ("UAH",	"Ukrainian Hryvnia"),
    ("UGX",	"Ugandan Shilling"),
    ("USD",	"United States Dollar"),
    ("UYU",	"Uruguayan Peso"),
    ("UZS",	"Uzbekistan Som"),
    ("VND",	"Vietnamese Dong"),
    ("VUV",	"Vanuatu Vatu"),
    ("WST",	"Samoan Tala"),
    ("XAF",	"CFA Franc BEAC"),
    ("XCD",	"East Caribbean Dollar"),
    ("XDR",	"Special Drawing Rights"),
    ("XOF",	"CFA Franc BCEAO"),
    ("XPF",	"CFP Franc"),
    ("YER",	"Yemeni Rial"),
    ("ZAR",	"South African Rand"),
    ("ZMW",	"Zambian Kwacha"),
    ("ZWL",	"Zimbabwean Dollar"),
]
symbol_values = [
    ("VZ", "Verizon Communications"), ("KO", "The Coca-Cola Company"), ("NFLX", "Netflix"), ("ADBE", "Adobe Inc."), ("CSCO", "Cisco Systems"), ("XOM", "Exxon Mobil Corporation"), ("CMG", "Chipotle Mexican Grill"), ("SBUX", "Starbucks Corporation"), ("PFE", "Pfizer Inc."), ("CRM", "Salesforce"), 
    ("WMT", "Walmart Inc."), ("HD", "The Home Depot"), ("GE", "General Electric Company"), ("PEP", "PepsiCo, Inc."), ("T", "AT&T Inc."), ("FDX", "FedEx Corporation"), ("INTC", "Intel Corporation"), ("MU", "Micron Technology, Inc."), ("GM", "General Motors Company"), ("COST", "Costco Wholesale Corporation"), 
    ("TWTR", "Twitter, Inc."), ("MS", "Morgan Stanley"), ("CAT", "Caterpillar Inc."), ("MMM", "3M Company"), ("UPS", "United Parcel Service"), ("BKNG", "Booking Holdings Inc."), ("MCD", "McDonald's Corporation"), ("ABT", "Abbott Laboratories"), ("BMY", "Bristol Myers Squibb"), ("WBA", "Walgreens Boots Alliance, Inc."),
    ("IBM", "International Business Machines Corporation"), ("NVDA", "NVIDIA Corporation"), ("AAPL", "Apple Inc."), ("MSFT", "Microsoft Corporation"), ("AMZN", "Amazon.com, Inc."), ("GOOGL", "Alphabet Inc."), ("FB", "Meta Platforms, Inc."), ("TSLA", "Tesla, Inc."), ("JPM", "JPMorgan Chase & Co."), ("JNJ", "Johnson & Johnson"), 
    ("V", "Visa Inc."), ("PG", "Procter & Gamble Company"), ("HD", "The Home Depot, Inc."), ("UNH", "UnitedHealth Group Incorporated"), ("MA", "Mastercard Incorporated"), ("BAC", "Bank of America Corp."), ("DIS", "The Walt Disney Company"), ("PYPL", "PayPal Holdings, Inc."), ("INTC", "Intel Corporation"), ("CMCSA", "Comcast Corporation"), 
    ("VZ", "Verizon Communications Inc."), ("KO", "The Coca-Cola Company"), ("NFLX", "Netflix, Inc."), ("ADBE", "Adobe Inc."), ("CSCO", "Cisco Systems, Inc."), ("XOM", "Exxon Mobil Corporation"), ("CMG", "Chipotle Mexican Grill, Inc."), ("SBUX", "Starbucks Corporation"), ("PFE", "Pfizer Inc."), ("CRM", "salesforce.com, inc."), 
    ("WMT", "Walmart Inc."), ("HD", "The Home Depot, Inc."), ("GE", "General Electric Company"), ("PEP", "PepsiCo, Inc."), ("T", "AT&T Inc."), ("FDX", "FedEx Corporation"), ("INTC", "Intel Corporation"), ("MU", "Micron Technology, Inc."), ("GM", "General Motors Company"), ("COST", "Costco Wholesale Corporation"), 
    ("TWTR", "Twitter, Inc."), ("MS", "Morgan Stanley"), ("CAT", "Caterpillar Inc."), ("MMM", "3M Company"), ("UPS", "United Parcel Service, Inc."), ("BKNG", "Booking Holdings Inc."), ("MCD", "McDonald's Corporation"), ("ABT", "Abbott Laboratories"), ("BMY", "Bristol Myers Squibb Company"), ("WBA", "Walgreens Boots Alliance, Inc."),
    ("NKE", "NIKE, Inc."), ("MO", "Altria Group, Inc."), ("BLK", "BlackRock, Inc."), ("IBM", "International Business Machines Corporation"), ("NVDA", "NVIDIA Corporation"), ("AAPL", "Apple Inc."), ("MSFT", "Microsoft Corporation"), ("AMZN", "Amazon.com, Inc."), ("GOOGL", "Alphabet Inc."), ("FB", "Meta Platforms, Inc."), 
    ("TSLA", "Tesla, Inc."), ("JPM", "JPMorgan Chase & Co."), ("JNJ", "Johnson & Johnson"), ("V", "Visa Inc."), ("PG", "Procter & Gamble Company"), ("HD", "The Home Depot, Inc."), ("UNH", "UnitedHealth Group Incorporated"), ("MA", "Mastercard Incorporated"), ("BAC", "Bank of America Corp."), ("DIS", "The Walt Disney Company"), 
    ("PYPL", "PayPal Holdings, Inc."), ("INTC", "Intel Corporation"), ("CMCSA", "Comcast Corporation"), ("VZ", "Verizon Communications Inc."), ("KO", "The Coca-Cola Company"), ("NFLX", "Netflix, Inc."), ("ADBE", "Adobe Inc."), ("CSCO", "Cisco Systems, Inc."), ("XOM", "Exxon Mobil Corporation"), ("CMG", "Chipotle Mexican Grill, Inc."), 
    ("SBUX", "Starbucks Corporation"), ("PFE", "Pfizer Inc."), ("CRM", "salesforce.com, inc."), ("WMT", "Walmart Inc."), ("HD", "The Home Depot, Inc."), ("GE", "General Electric Company"), ("PEP", "PepsiCo, Inc."), ("T", "AT&T Inc."), ("FDX", "FedEx Corporation"), ("INTC", "Intel Corporation"), ("MU", "Micron Technology, Inc."), 
    ("GM", "General Motors Company"), ("COST", "Costco Wholesale Corporation"), ("TWTR", "Twitter, Inc."), ("MS", "Morgan Stanley"), ("CAT", "Caterpillar Inc."), ("MMM", "3M Company"), ("UPS", "United Parcel Service, Inc."), ("BKNG", "Booking Holdings Inc."), ("MCD", "McDonald's Corporation"), ("ABT", "Abbott Laboratories"), 
    ("BMY", "Bristol Myers Squibb Company"), ("WBA", "Walgreens Boots Alliance, Inc."), ("NKE", "NIKE, Inc."), ("MO", "Altria Group, Inc."), ("BLK", "BlackRock, Inc.")
]
class CoreStock(models.Model):
    symbol = models.CharField(max_length=5, choices=symbol_values, blank=True, null=True)
    date_of_stock = models.DateField(blank=True, null=True)
    open_stock = models.FloatField(blank=True, null=True)
    high_stock = models.FloatField(blank=True, null=True)  
    low_stock = models.FloatField(blank=True, null=True)
    close_stock = models.FloatField(blank=True, null=True)
    volume_stock = models.IntegerField(blank=True, null=True)

class IncomeStatement(models.Model):
    symbol = models.CharField(max_length=5, choices=symbol_values, blank=True, null=True)
    fiscal_Date_Ending = models.DateField(blank=True, null=True)
    reported_Currency = models.CharField(max_length=4, blank=True, null=True)
    gross_Profit = models.IntegerField(blank=True, null=True)
    total_Revenue = models.IntegerField(blank=True, null=True)
    cost_Of_Revenue = models.IntegerField(blank=True, null=True)
    operating_Income = models.IntegerField(blank=True, null=True)
    operating_Expenses = models.IntegerField(blank=True, null=True)
    Depreciation = models.IntegerField(blank=True, null=True)
    net_Income = models.IntegerField(blank=True, null=True)
    
class BalanceSheet(models.Model):
    symbol = models.CharField(max_length=5, choices=symbol_values, blank=True, null=True)
    reported_Currency = models.CharField(max_length=4, blank=True, null=True)
    fiscal_Date_Ending = models.DateField(blank=True, null=True)
    total_Assets = models.IntegerField(blank=True, null=True)
    total_Current_Assets = models.IntegerField(blank=True, null=True)
    Investments = models.IntegerField(blank=True, null=True)
    current_Debt = models.IntegerField(blank=True, null=True)
    treasury_Stock = models.IntegerField(blank=True, null=True)
    common_Stock = models.IntegerField(blank=True, null=True)

class CashFlow(models.Model):
    symbol = models.CharField(max_length=5, choices=symbol_values, blank=True, null=True)
    fiscal_Date_Ending = models.DateField(blank=True, null=True)
    operating_Cashflow = models.IntegerField(blank=True, null=True)
    capital_Expenditures = models.IntegerField(blank=True, null=True)
    change_In_Inventory = models.IntegerField(blank=True, null=True)
    profit_Loss = models.IntegerField(blank=True, null=True)
    cashflow_From_Investment = models.IntegerField(blank=True, null=True)
    cashflow_From_Financing = models.IntegerField(blank=True, null=True)
    dividend_Payout = models.IntegerField(blank=True, null=True)

class Earnings(models.Model):
    symbol = models.CharField(max_length=5, choices=symbol_values, blank=True, null=True)
    fiscal_Date_Ending = models.DateField(blank=True, null=True)
    reported_eps = models.FloatField(blank=True, null=True)
    estimated_eps = models.FloatField(blank=True, null=True)
    Surprise = models.FloatField(blank=True, null=True)
    surprise_percentage = models.FloatField(blank=True, null=True)

class FundData(models.Model):
    symbol = models.CharField(max_length=5, choices=symbol_values, blank=True, null=True)
    
    # function OVERVIEW
    description = models.CharField(max_length=1500, blank=True, null=True)
    market_capitalization = models.IntegerField(blank=True, null=True)
    ebitda = models.IntegerField(blank=True, null=True)
    pe_ratio = models.IntegerField(blank=True, null=True)
    peg_ratio = models.IntegerField(blank=True, null=True)
    book_value = models.IntegerField(blank=True, null=True)
    dividend_per_share = models.FloatField(blank=True, null=True)
    dividend_yield = models.FloatField(blank=True, null=True)
    eps = models.FloatField(blank=True, null=True)
    profit_margin = models.FloatField(blank=True, null=True)
    return_on_assets_TTM = models.FloatField(blank=True, null=True)
    return_on_equity_TTM = models.FloatField(blank=True, null=True)

# currency is a CharField()
class ForEX(models.Model):
    date_of_currency = models.DateField(blank=True, null=True)  
    from_currency = models.CharField(max_length=4, choices=currency_values, blank=True, null=True)
    to_currency = models.CharField(max_length=4, choices=currency_values, blank=True, null=True)
    exchange_rate = models.FloatField(blank=True, null=True)

# These values are only for the United States
class EconomicIndicators(models.Model):
    indicator = models.CharField(max_length=15, blank=True, null=True)
    date_of_indicator = models.DateField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

class Commodities(models.Model):
    commodity = models.CharField(max_length=15, blank=True, null=True)
    date_of_commodity = models.DateField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

class Mail(models.Model):
    subject = models.CharField(max_length=75, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    message = models.CharField(max_length=1000, blank=True, null=True)
