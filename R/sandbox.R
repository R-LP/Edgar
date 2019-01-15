library(finreportr)
library(lubridate)
library(quantmod)
library(stringr)

startyear = 2010
endyear = 2015

temp = GetBalanceSheet("AAPL", startyear)
datas = data.frame(c(unique(temp$Metric), "Stock Price"))
colnames(datas) <- "Metric"

for (year in startyear:endyear){
  sheet = GetBalanceSheet("AAPL", year)
  named_amount = paste("amount", toString(year), sep="")
  colnames(sheet)[colnames(sheet)=="Amount"] <- named_amount
  date_report = sheet[which.max(as.POSIXct(sheet$endDate)), "endDate"]
  sheet = sheet[sheet$endDate >= date_report,]
  features = subset(sheet, select=c("Metric", named_amount))
  
  start = as.Date(date_report) - 30
  getSymbols("AAPL", src = "yahoo", from = start, to = date_report)
  price = mean(AAPL[, "AAPL.Close"])
  pricebind = c("Stock Price", price)
  features = rbind(features, pricebind)
  
  datas = merge(datas, features, all=TRUE)
}





sheet = GetBalanceSheet("AAPL", 2017)
sheetn1 = GetBalanceSheet("AAPL", 2016)
sheetn2 = GetBalanceSheet("AAPL", 2015)
write.csv(sheet, file = "test-sheet.csv")

sheet2017 = sheet[sheet$endDate > ymd(20170101),]
sheet2016 = sheetn1[sheetn1$endDate > ymd(20160101),]
sheet2015 = sheetn2[sheetn2$endDate > ymd(20150101),]

colnames(sheet2017)[colnames(sheet2017)=="Amount"] <- "amount2017"
colnames(sheet2016)[colnames(sheet2016)=="Amount"] <- "amount2016"
colnames(sheet2015)[colnames(sheet2015)=="Amount"] <- "amount2015"
sheets = list(sheet2015, sheet2016, sheet2017)

features2017 = subset(sheet2017, select=c("Metric", "amount2017"))
features2016 = subset(sheet2016, select=c("Metric", "amount2016"))
features2015 = subset(sheet2015, select=c("Metric", "amount2015"))

temp = merge(features2015, features2016)
feat2017 = merge(temp, features2017)

prices = c()
for (sheet in sheets){
  end = as.Date(sheet$endDate[1])
  start = end - 30
  getSymbols("AAPL", src = "yahoo", from = start, to = end)
  price = mean(AAPL[, "AAPL.Close"])
  prices = append(prices, price)
}

tolower(str_replace_all(str_replace_all(datas$Metric[2], "[[:punct:]]", ""), " ", "_"))

test = lapply(
  datas$Metric, function(x) {
    tolower(str_replace_all(str_replace_all(x, "[[:punct:]]", ""), " ", "_"))
    }
  )


pricesbind= c("Stock Price", prices)
feat2017 = rbind(feat2017, pricesbind)


