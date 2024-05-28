from django.shortcuts import render
from django.http import HttpResponse
from playground.models import *
from .forms import *
from api_key import api_key
import requests
import json
# Making charts
import pandas
import datetime
# Send mail
from django.core.mail import send_mail

def send_email(request):
    if request.method == 'POST':
        email_form = ContactForm(request.POST)
        if email_form.is_valid():
            # Check if the same information is trying to be sent
            most_recent_row = Mail.objects.latest('id')
            recent_subject = most_recent_row.subject
            recent_email = most_recent_row.email
            recent_message = most_recent_row.message

            sender_email = email_form.cleaned_data['sender_email']
            sender_subject = email_form.cleaned_data['sender_subject']
            sender_message = email_form.cleaned_data['sender_message']
            
            if sender_email != recent_email and sender_message != recent_message and sender_subject != recent_subject:
              
                a = Mail.objects.create(subject=sender_subject, email=sender_email, message=sender_message)
                # Send email
                send_mail(sender_subject, sender_message, sender_email, ['domdd305@gmail.com'], fail_silently=False)

        else:
            print(email_form.errors)
    else:
        email_form = ContactForm()

def website(request):
    send_email(request)
    return render(request, 'index.html')

def underthehood(request):
    send_email(request)
    return render(request, 'underthehood.html')

def stock_form(request):
    send_email(request)
    if request.method == 'POST':
        symbol_form = SymbolValues(request.POST)
        type_form = StockType(request.POST)
        if symbol_form.is_valid() and type_form.is_valid():
            # Access the value of 'symbol' from the submitted form
            symbol_value = symbol_form.cleaned_data['symbol']
            stock_type = type_form.cleaned_data['stock_type']
            chart_values = stock_output(symbol_value, stock_type)
        else:
            symbol_form = SymbolValues()
            type_form = StockType()
            chart_values = stock_output()
    else:
        symbol_form = SymbolValues()
        type_form = StockType()
        chart_values = stock_output()

    form_response = {'symbol_form': symbol_form, 'type_form': type_form}
    data_response = {}
    keys = ['ticker', 'chart_data']
    data_response = {k: v for k, v in zip(keys, chart_values)}
    response = dict(form_response, **data_response)

    return render(request, 'stock.html', response)

def stock_output(ticker='NVDA', stock_type='open'):
    exist = CoreStock.objects.filter(symbol=ticker).exists()
    if exist == False:
        
        function = 'TIME_SERIES_DAILY'
        response = requests.get(f'https://www.alphavantage.co/query?function={function}&symbol={ticker}&apikey={api_key}')
        data = response.json()['Time Series (Daily)']
        # convert to csv
        f = open("temp_csv.txt", 'w')
        f.write("date,open,high,low,close,volume\n")
        for current_day, values in data.items():
            f.write(f'{current_day}')
            for category, value in values.items():
                f.write(f',{value}')
            f.write('\n')
        f.close()

        file = pandas.read_csv('temp_csv.txt')            

        for row in file.itertuples():    
            a = CoreStock.objects.create(symbol=ticker, date_of_stock = datetime.datetime.strptime(row.date, '%Y-%m-%d'), open_stock = row.open,
                                        high_stock = row.high, low_stock = row.low, close_stock = row.close, volume_stock = row.volume)

    condition = {
        "symbol": f'{ticker}',
    }

    queryset = CoreStock.objects.filter(**condition)

    if stock_type=='open':
        data = [{'x': obj.date_of_stock.strftime("%Y-%m-%d"), 'y': obj.open_stock} for obj in queryset][::-1] # flip the order
    elif stock_type=='low':
        data = [{'x': obj.date_of_stock.strftime("%Y-%m-%d"), 'y': obj.low_stock} for obj in queryset][::-1] # flip the order
    elif stock_type=='high':
        data = [{'x': obj.date_of_stock.strftime("%Y-%m-%d"), 'y': obj.high_stock} for obj in queryset][::-1] # flip the order
    elif stock_type=='close':
        data = [{'x': obj.date_of_stock.strftime("%Y-%m-%d"), 'y': obj.close_stock} for obj in queryset][::-1] # flip the order
    elif stock_type=='volume':
        data = [{'x': obj.date_of_stock.strftime("%Y-%m-%d"), 'y': obj.volume_stock} for obj in queryset][::-1] # flip the order
    return ticker, json.dumps(data)

def data_form(request):
    send_email(request)
    if request.method == 'POST':
        
        symbol_form = SymbolValues(request.POST)
        data_form = DataType(request.POST)
        if symbol_form.is_valid() and data_form.is_valid():
            # Access the value of 'symbol' from the submitted form
            symbol_value = symbol_form.cleaned_data['symbol']
            data_type = data_form.cleaned_data['data_type']
            data_values = data_output(symbol_value, data_type)
        else:
            symbol_form = SymbolValues()
            data_form = DataType()
            data_values = data_output()
            data_type = 'CASH_FLOW' #Default
    else:
        symbol_form = SymbolValues()
        data_form = DataType()
        data_values = data_output()
        data_type = 'CASH_FLOW' #Default

    form_response = {'symbol_form': symbol_form, 'data_form': data_form}
    data_response = {}
    if data_type == 'INCOME_STATEMENT':
        keys = ['data_type','ticker','net_income_data','total_revenue_data','cost_of_revenue_data','operating_income_data','gross_profit_data','operating_expenses_data','depreciation_data']
    if data_type == 'BALANCE_SHEET':
        keys = ['data_type','ticker','total_assets_data','total_current_assets_data','investment_data','current_debt_data','treasury_stock_data','common_stock_data']
    elif data_type == 'CASH_FLOW':
        keys = ['data_type','ticker','operating_cashflow_data','capital_expenditures_data','change_in_inventory_data','profit_loss_data','cashflow_from_investments_data','cashflow_from_financing_data','dividend_payout_data']
    elif data_type == 'EARNINGS':
        keys = ['data_type','ticker','reported_eps_data','estimated_eps_data','surprise_data','surprise_percentage_data']
    data_response = {k: v for k, v in zip(keys, data_values)}

    response = dict(form_response, **data_response)
    return render(request, 'compdata.html', response)

def data_output(ticker='VZ', data_type='CASH_FLOW'):
    if data_type == 'INCOME_STATEMENT':
        exist = IncomeStatement.objects.filter(symbol=ticker).exists()
        function = data_type
        if exist == False:
            
            response = requests.get(f'https://www.alphavantage.co/query?function={function}&symbol={ticker}&apikey={api_key}')
            data = response.json()['annualReports']
            # convert to csv
            f = open("temp_csv.txt", 'w')
            options = ['fiscalDateEnding','reportedCurrency','grossProfit','totalRevenue','costOfRevenue','operatingIncome','operatingExpenses','depreciation','netIncome']
            f.write(f"{','.join(options)}\n")
            
            for entry in data:
                line = ",".join([entry[key] for key in entry.keys() if key in options])
                f.write(line + "\n")

            f.close()

            file = pandas.read_csv('temp_csv.txt')            

            for row in file.itertuples():    
                a = IncomeStatement.objects.create(symbol=ticker, fiscal_Date_Ending = datetime.datetime.strptime(row.fiscalDateEnding, '%Y-%m-%d'), reported_Currency = row.reportedCurrency, gross_Profit = row.grossProfit, total_Revenue = row.totalRevenue, 
                                            cost_Of_Revenue = row.costOfRevenue, operating_Income = row.operatingIncome, operating_Expenses = row.operatingExpenses, Depreciation = row.depreciation, net_Income = row.netIncome)

        condition = {
            "symbol": f'{ticker}',
        }

        queryset = IncomeStatement.objects.filter(**condition)

        function = 'Income Statement'
        net_income_data = [{'x': obj.fiscal_Date_Ending.strftime("%Y-%m-%d"), 'y': obj.net_Income} for obj in queryset][::-1]     
        total_revenue_data = [{'x': obj.fiscal_Date_Ending.strftime("%Y-%m-%d"), 'y': obj.total_Revenue} for obj in queryset][::-1]
        cost_of_revenue_data = [{'x': obj.fiscal_Date_Ending.strftime("%Y-%m-%d"), 'y': obj.cost_Of_Revenue} for obj in queryset][::-1]
        operating_income_data = [{'x': obj.fiscal_Date_Ending.strftime("%Y-%m-%d"), 'y': obj.operating_Income} for obj in queryset][::-1]
        gross_profit_data = [{'x': obj.fiscal_Date_Ending.strftime("%Y-%m-%d"), 'y': obj.gross_Profit} for obj in queryset][::-1]
        operating_expenses_data = [{'x': obj.fiscal_Date_Ending.strftime("%Y-%m-%d"), 'y': obj.operating_Expenses} for obj in queryset][::-1]
        depreciation_data = [{'x': obj.fiscal_Date_Ending.strftime("%Y-%m-%d"), 'y': obj.Depreciation} for obj in queryset][::-1]

        return [function, ticker, json.dumps(net_income_data), json.dumps(total_revenue_data), json.dumps(cost_of_revenue_data), json.dumps(operating_income_data), json.dumps(gross_profit_data), json.dumps(operating_expenses_data), json.dumps(depreciation_data) ]
    elif data_type == 'BALANCE_SHEET':
        exist = BalanceSheet.objects.filter(symbol=ticker).exists()
        function = data_type
        if exist == False:
            
            response = requests.get(f'https://www.alphavantage.co/query?function={function}&symbol={ticker}&apikey={api_key}')
            data = response.json()['annualReports']
            # convert to csv
            f = open("temp_csv.txt", 'w')
            options = ['fiscalDateEnding','reportedCurrency','totalAssets','totalCurrentAssets','investments','currentDebt','treasuryStock','commonStock']
            f.write(f"{','.join(options)}\n")
            
            for entry in data:
                info = [entry[key] for key in entry.keys() if key in options]
                for i in range(len(info)): # Removing None values
                    if info[i] == 'None':
                        info[i] = '0'
                line = ",".join(info)
                f.write(line + "\n")

            f.close()

            file = pandas.read_csv('temp_csv.txt')            

            for row in file.itertuples():    
                a = BalanceSheet.objects.create(symbol=ticker, fiscal_Date_Ending = datetime.datetime.strptime(row.fiscalDateEnding, '%Y-%m-%d'), reported_Currency = row.reportedCurrency, 
                total_Assets = row.totalAssets, total_Current_Assets = row.totalCurrentAssets, Investments = row.investments, current_Debt = row.currentDebt, treasury_Stock = row.treasuryStock, common_Stock = row.commonStock)

        condition = {
            "symbol": f'{ticker}',
        }

        queryset = BalanceSheet.objects.filter(**condition)

        function = 'Balance Sheet'
        total_assets_data = [{'x': obj.fiscal_Date_Ending.strftime("%Y-%m-%d"), 'y': obj.total_Assets} for obj in queryset][::-1]     
        total_current_assets_data = [{'x': obj.fiscal_Date_Ending.strftime("%Y-%m-%d"), 'y': obj.total_Current_Assets} for obj in queryset][::-1]
        investment_data = [{'x': obj.fiscal_Date_Ending.strftime("%Y-%m-%d"), 'y': obj.Investments} for obj in queryset][::-1]
        current_debt_data = [{'x': obj.fiscal_Date_Ending.strftime("%Y-%m-%d"), 'y': obj.current_Debt} for obj in queryset][::-1]
        treasury_stock_data = [{'x': obj.fiscal_Date_Ending.strftime("%Y-%m-%d"), 'y': obj.treasury_Stock} for obj in queryset][::-1]
        common_stock_data = [{'x': obj.fiscal_Date_Ending.strftime("%Y-%m-%d"), 'y': obj.common_Stock} for obj in queryset][::-1]

        return [function, ticker, json.dumps(total_assets_data), json.dumps(total_current_assets_data), json.dumps(investment_data), json.dumps(current_debt_data), json.dumps(treasury_stock_data), json.dumps(common_stock_data)]
    elif data_type == 'CASH_FLOW':
        exist = CashFlow.objects.filter(symbol=ticker).exists()
        function = data_type
        if exist == False:
            
            response = requests.get(f'https://www.alphavantage.co/query?function={function}&symbol={ticker}&apikey={api_key}')
            data = response.json()['annualReports']
            # convert to csv
            f = open("temp_csv.txt", 'w')
            options = ['fiscalDateEnding','operatingCashflow','capitalExpenditures','changeInInventory','profitLoss','cashflowFromInvestment','cashflowFromFinancing','dividendPayout']
            f.write(f"{','.join(options)}\n")
            
            for entry in data:
                info = [entry[key] for key in entry.keys() if key in options]
                for i in range(len(info)): # Removing None values
                    if info[i] == 'None':
                        info[i] = '0'
                line = ",".join(info)
                f.write(line + "\n")

            f.close()

            file = pandas.read_csv('temp_csv.txt')            

            for row in file.itertuples():    
                a = CashFlow.objects.create(symbol=ticker, fiscal_Date_Ending = datetime.datetime.strptime(row.fiscalDateEnding, '%Y-%m-%d'), operating_Cashflow = row.operatingCashflow, capital_Expenditures = row.capitalExpenditures, change_In_Inventory = row.changeInInventory, 
                                            profit_Loss = row.profitLoss, cashflow_From_Investment = row.cashflowFromInvestment, cashflow_From_Financing = row.cashflowFromFinancing, dividend_Payout = row.dividendPayout)

        condition = {
            "symbol": f'{ticker}',
        }

        queryset = CashFlow.objects.filter(**condition)

        function = 'Cash Flow'
        operating_cashflow_data = [{'x': obj.fiscal_Date_Ending.strftime("%Y-%m-%d"), 'y': obj.operating_Cashflow} for obj in queryset][::-1]     
        capital_expenditures_data = [{'x': obj.fiscal_Date_Ending.strftime("%Y-%m-%d"), 'y': obj.capital_Expenditures} for obj in queryset][::-1]
        change_in_inventory_data = [{'x': obj.fiscal_Date_Ending.strftime("%Y-%m-%d"), 'y': obj.change_In_Inventory} for obj in queryset][::-1]
        profit_loss_data = [{'x': obj.fiscal_Date_Ending.strftime("%Y-%m-%d"), 'y': obj.profit_Loss} for obj in queryset][::-1]
        cashflow_from_investment_data = [{'x': obj.fiscal_Date_Ending.strftime("%Y-%m-%d"), 'y': obj.cashflow_From_Investment} for obj in queryset][::-1]
        cashflow_from_financing_data = [{'x': obj.fiscal_Date_Ending.strftime("%Y-%m-%d"), 'y': obj.cashflow_From_Financing} for obj in queryset][::-1]
        dividend_payout_data = [{'x': obj.fiscal_Date_Ending.strftime("%Y-%m-%d"), 'y': obj.dividend_Payout} for obj in queryset][::-1]
        return [function, ticker, json.dumps(operating_cashflow_data), json.dumps(capital_expenditures_data), json.dumps(change_in_inventory_data), json.dumps(profit_loss_data), json.dumps(cashflow_from_investment_data), json.dumps(cashflow_from_financing_data), json.dumps(dividend_payout_data)]
    elif data_type == 'EARNINGS':
        exist = Earnings.objects.filter(symbol=ticker).exists()
        function = data_type
        if exist == False:
            
            response = requests.get(f'https://www.alphavantage.co/query?function={function}&symbol={ticker}&apikey={api_key}')
            data = response.json()['quarterlyEarnings']
            # convert to csv
            f = open("temp_csv.txt", 'w')
            options = ['fiscalDateEnding','reportedEPS','estimatedEPS','surprise','surprisePercentage']
            f.write(f"{','.join(options)}\n")
            
            for entry in data:
                info = [entry[key] for key in entry.keys() if key in options]
                for i in range(len(info)): # Removing None values
                    if info[i] == 'None':
                        info[i] = '0'
                line = ",".join(info)
                f.write(line + "\n")

            f.close()

            file = pandas.read_csv('temp_csv.txt')            

            for row in file.itertuples():    
                a = Earnings.objects.create(symbol=ticker, fiscal_Date_Ending = datetime.datetime.strptime(row.fiscalDateEnding, '%Y-%m-%d'), reported_eps = row.reportedEPS, estimated_eps = row.estimatedEPS, Surprise = row.surprise, surprise_percentage = row.surprisePercentage)

        condition = {
            "symbol": f'{ticker}',
        }

        queryset = Earnings.objects.filter(**condition)

        function = 'Earnings'
        reported_eps_data = [{'x': obj.fiscal_Date_Ending.strftime("%Y-%m-%d"), 'y': obj.reported_eps} for obj in queryset][::-1]     
        estimated_eps_data = [{'x': obj.fiscal_Date_Ending.strftime("%Y-%m-%d"), 'y': obj.estimated_eps} for obj in queryset][::-1]
        surprise_data = [{'x': obj.fiscal_Date_Ending.strftime("%Y-%m-%d"), 'y': obj.Surprise} for obj in queryset][::-1]
        surprise_percentage_data = [{'x': obj.fiscal_Date_Ending.strftime("%Y-%m-%d"), 'y': obj.surprise_percentage} for obj in queryset][::-1]
        return [function, ticker, json.dumps(reported_eps_data), json.dumps(estimated_eps_data), json.dumps(surprise_data), json.dumps(surprise_percentage_data)]

def forex_form(request):
    send_email(request)
    if request.method == 'POST':
        from_currency_form = FromCurrency(request.POST)
        to_currency_form = ToCurrency(request.POST)
        if from_currency_form.is_valid() and to_currency_form.is_valid():
            from_currency = from_currency_form.cleaned_data['from_currency']
            to_currency = to_currency_form.cleaned_data['to_currency']
            data_values = forex_output(from_currency, to_currency)
        else:
            from_currency_form = FromCurrency()
            to_currency_form = ToCurrency()
            data_values = forex_output()
    else:
        from_currency_form = FromCurrency()
        to_currency_form = ToCurrency()
        data_values = forex_output()

    form_response = {'from_currency_form': from_currency_form, 'to_currency_form': to_currency_form}
    
    keys = ['from_currency','to_currency','chart_data']
    data_response = {k: v for k, v in zip(keys, data_values)}

    response = dict(form_response, **data_response)
    return render(request, 'forex.html', response)

def forex_output(from_currency_value='EUR', to_currency_value='USD'):
    #from_currency_value='EUR'
    #to_currency_value='USD'
    ForEX.objects.all().delete()
    exist = ForEX.objects.filter(from_currency=from_currency_value, to_currency = to_currency_value).exists()
    function = 'FX_DAILY'
    if exist == False:
        response = requests.get(f'https://www.alphavantage.co/query?function={function}&from_symbol={from_currency_value}&to_symbol={to_currency_value}&apikey={api_key}')
        data = response.json()['Time Series FX (Daily)']
        # convert to csv
        f = open("temp_csv.txt", 'w')
        f.write("date,open,high,low,close\n")
        for current_day, values in data.items():
            f.write(f'{current_day}')
            for category, value in values.items():
                f.write(f',{value}')
            f.write('\n')
        f.close()

        file = pandas.read_csv('temp_csv.txt')            

        for row in file.itertuples(): 
               
            a = ForEX.objects.create(from_currency = from_currency_value, to_currency = to_currency_value, date_of_currency = datetime.datetime.strptime(row.date, '%Y-%m-%d'), exchange_rate = row.open)

    condition = {
        "from_currency": f'{from_currency_value}',
        "to_currency": f'{to_currency_value}',
    }
    
    queryset = ForEX.objects.filter(**condition)
    data = [{'x': obj.date_of_currency.strftime("%Y-%m-%d"), 'y': obj.exchange_rate} for obj in queryset][::-1]  

    output = [from_currency_value, to_currency_value, json.dumps(data)]

    return output

def econ_indicators_form(request):
    send_email(request)
    if request.method == 'POST':
        econ_indicator_form = EconForm(request.POST)
        if econ_indicator_form.is_valid():
            # Access the value of 'symbol' from the submitted form
            econ_indicator = econ_indicator_form.cleaned_data['econ_indicator']
            chart_values = econ_output(econ_indicator)
        else:
            econ_indicator_form = EconForm()
            chart_values = econ_output()
    else:
        econ_indicator_form = EconForm()
        chart_values = econ_output()

    form_response = {'economic_indicator_form': econ_indicator_form}
    data_response = {}
    keys = ['label_value', 'indicator', 'chart_data']
    data_response = {k: v for k, v in zip(keys, chart_values)}
    response = dict(form_response, **data_response)

    return render(request, 'econindicators.html', response)

def econ_output(econ_indicator='INFLATION'):
    exist = EconomicIndicators.objects.filter(indicator=econ_indicator).exists()
    if exist == False:
       
        function = econ_indicator
        response = requests.get(f'https://www.alphavantage.co/query?function={function}&apikey={api_key}')
        data = response.json()['data']
        # convert to csv
        f = open("temp_csv.txt", 'w')
        f.write("date,value\n")
        for dataset in data:
            f.write(f"{dataset['date']},{dataset['value']}\n")
        f.close()

        file = pandas.read_csv('temp_csv.txt')            

        for row in file.itertuples():    
            a = EconomicIndicators.objects.create(indicator=econ_indicator, date_of_indicator = datetime.datetime.strptime(row.date, '%Y-%m-%d'), value = row.value )

    condition = {
        "indicator": f'{econ_indicator}',
    }

    queryset = EconomicIndicators.objects.filter(**condition)

    data = [{'x': obj.date_of_indicator.strftime("%Y-%m-%d"), 'y': obj.value} for obj in queryset][::-1] # flip the order

    if econ_indicator=='INFLATION':
        label_value = 'Percentage'
        indicator = 'Inflation'
    elif econ_indicator=='REAL_GDP':
        label_value = 'In billions of dollars'
        indicator = 'Real GDP'
    elif econ_indicator=='REAL_GDP_PER_CAPITA':
        label_value = 'Chained 2012 dollars'
        indicator = 'Real GDP per capita'
    elif econ_indicator=='FEDERAL_FUNDS_RATE':
        label_value = 'Percantage'
        indicator = 'Federal funds rate'
    elif econ_indicator=='CPI':
        label_value = 'Based on 1982'
        indicator = 'CPI'
    elif econ_indicator=='UNEMPLOYMENT':
        label_value='Percentage'
        indicator='Unemployment rate'

    return label_value, indicator, json.dumps(data)

def commodities_form(request):
    send_email(request)
    if request.method == 'POST':
        commodities_form = CommoditiesForm(request.POST)
        if commodities_form.is_valid():
            # Access the value of 'symbol' from the submitted form
            commodity = commodities_form.cleaned_data['commodity']
            chart_values = commodity_output(commodity)
        else:
            commodities_form = CommoditiesForm()
            chart_values = commodity_output()
    else:
        commodities_form = CommoditiesForm()
        chart_values = commodity_output()

    form_response = {'commodity_form': commodities_form}
    data_response = {}
    keys = ['commodity', 'chart_data']
    data_response = {k: v for k, v in zip(keys, chart_values)}

    response = dict(form_response, **data_response)

    return render(request, 'commodities.html', response)
    
def commodity_output(commodity_value='NATURAL_GAS'):
    exist = Commodities.objects.filter(commodity=commodity_value).exists()
    if exist == False:
       
        function = commodity_value
        response = requests.get(f'https://www.alphavantage.co/query?function={function}&apikey={api_key}')
        data = response.json()['data']
        # convert to csv
        f = open("temp_csv.txt", 'w')
        f.write("date,value\n")
        for dataset in data:
            if dataset['value'] == '.':
                pass
            else:
                f.write(f"{dataset['date']},{dataset['value']}\n")
        f.close()

        file = pandas.read_csv('temp_csv.txt')            

        for row in file.itertuples():    
            a = Commodities.objects.create(commodity=commodity_value, date_of_commodity = datetime.datetime.strptime(row.date, '%Y-%m-%d'), value = row.value )
    condition = {
        "commodity": f'{commodity_value}',
    }

    queryset = Commodities.objects.filter(**condition)

    data = [{'x': obj.date_of_commodity.strftime("%Y-%m-%d"), 'y': obj.value} for obj in queryset][::-1] # flip the order
    
    choices = [('WTI','Crude Oil WTI'),('NATURAL_GAS','Natural Gas'),('COPPER','Copper'),('ALUMINUM','Aluminum'),('WHEAT','Wheat'),('CORN','Corn'),('COTTON','Cotton'),('SUGAR','Sugar'),('COFFEE','Coffee')]
    for i in range(len(choices)):
        if choices[i][0] == commodity_value:
            commodity_value = choices[i][1]
            break

    return commodity_value, json.dumps(data)

def overview_form(request):
    send_email(request)
    if request.method == 'POST':
        symbol_form = SymbolValues(request.POST)
        if symbol_form.is_valid():
            # Access the value of 'symbol' from the submitted form
            symbol = symbol_form.cleaned_data['symbol']
            web_data = overview_output(symbol)
        else:
            symbol_form = SymbolValues(request.POST)
            web_data = overview_output()
    else:
        symbol_form = SymbolValues(request.POST)
        web_data = overview_output()

    response = {'symbol_form': symbol_form}
    web_data.update(response)

    return render(request, 'overview.html', web_data)

def overview_output(symbol='NVDA'):
    response = requests.get(f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={api_key}')
    data = response.json()

    return data
