#Task 1, converting vectors to a matrix 
a <-c(1,2,3,4,5) 
b <-c(6,7,8,9,10) 
c <-c(11,12,13,14,15)
combined_mat <- cbind(a,b,c)
combined_mat
my_matrix <- matrix(combined_mat,nrow=5,ncol=3)
print(my_matrix)
#Converting the matrix into a graph
matplot(my_matrix, type='b',pch=15,col=1:3)

#Task 2 Employee Dataframe
employeeA <- c('Jill Brown', 44, 'Female', 'Accounts Manager', 5)
employeeB <- c('Henry Green',28,'Male','Web Developer',1)
employeeC <- c('Joe Davis',30,'Male','Human Resources',3)
employeeD <- c('Harriet Thoms', 36, 'Female', 'PR',3)
employeeE <- c('Adrienne Hoover', 32,'Female', 'Office Administrator', 6)

frame <- data.frame(employeeA,employeeB,employeeC,employeeD,employeeE)

print(frame)

#Task 3 Graph Plot
install.packages("ggplot2", dependancies=TRUE)

library(ggplot2)
x <- seq(1:20)
y <- x^2
qplot(x,y,geom='point')+ xlab("X axis") + ylab("Y axis") +ggtitle("Task 3, Creating a simple qplot")


#Task 4 Data Visualization of Texas Housing
ggplot2::txhousing

?txhousing
txhousing
#Is there a relationship between listings and number of sales
ggplot(data = txhousing, aes(x = listings, y = sales)) +
  geom_point() +
  geom_smooth(method = "lm")+
  ggtitle("Relationship between number of listings in a City and the Sales in that city")
  

#Is there a relationship between date and value of sales over time
qplot(data=txhousing,x=date,y=volume, geom='line', colour='skyblue4')+ xlab("Date, years") + ylab('Value of Sales in $0000') +ggtitle("Value of Sales over Time")

#Further analysis on the trend between The Year and median sale price

qplot(year, median, data = txhousing, 
      geom = "dotplot", stackdir = "center", binaxis = "y",
      color = city, fill = year)+ggtitle("The city with the median sale prices from highest to lowest")
#Which cities had the highest total sales value
qplot(city, volume, data = txhousing, 
      geom="point",colour="class")+ ggtitle("Relationship between City and the Sales in that city")
