#Write a R program to take input from the user (name and age) and display the values.

name<-readline("Hi, What is your name? ")

age<-readline("How old are you?")

both<-paste("So your name is ", name , " and you are" , age) 
print(both)

#Write a R program to get the details of the objects in memory. Hint: how do you list all the local variables?

Film.ReleaseDate <- list("The Watermelon Woman"=1997, "The Godfather"=1972, "Perfect Blue"=1999, "Palm Springs"=2020)

Film.ReleaseDate[5] <- ("Roma"=2018)

Film.ReleaseDate[6] <- ("Piku"=2015)

print(ls())
#Write a R program to create a sequence of numbers from 20 to 50 and find the mean of numbers from 20 to 60 and sum of numbers from 51 to 91.
print(seq(20,50))

sum(seq(20,60))/length(seq(20,60))

sum(seq(51,91))
#Write a R program to create a vector which contains 10 random integer values between -50 and +50

finaltask <- (runif(10, min=-50, max=50))

print(finaltask)