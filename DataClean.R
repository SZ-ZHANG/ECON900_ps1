setwd("/Users/shen/Desktop/Homework/parsed_results")

dat_hw <- read.csv("BoardGameGeek.csv",header = TRUE)

names(dat_hw) <- c("Index", "AvgRating", "GameName", "GameRank", "GeekRating", "ListPrice","NumVoters")


change <- lapply(c(2,4,5,7), function(x){
  
  
  dat_hw[,x] <<- gsub("\n", "", dat_hw[,x])
  dat_hw[,x] <<- gsub("\t", "", dat_hw[,x])
  dat_hw[,x] <<- as.numeric(dat_hw[,x])
  
  
})

dat_hw[,6] <- gsub("\n", "", dat_hw[,6])
dat_hw[,6] <- gsub("\t", "", dat_hw[,6])
dat_hw[,6] <- gsub("]", "", dat_hw[,6])
dat_hw[,6] <- gsub("[", "", dat_hw[,6])

chage2 <- lapply(1:dim(dat_hw)[1],function(x){
  
  if (nchar(dat_hw[x,6]) == 0) {
    
    dat_hw[x,6] <<- NA
    
  }else if (nchar(dat_hw[x,6]) == 1) {
    
    dat_hw[x,6] <<- NA
    
  }else if (nchar(dat_hw[x,6]) > 30) {
    
    dat_hw[x,6] <<- NA
  }
  
  
  
  
})



change3 <-  lapply(1:dim(dat_hw)[1],function(x){
  
  if (is.na(dat_hw[x,6]) == FALSE ) {
    
    dat_hw[x,6] <<- strsplit(dat_hw[x,6],"[$]")[[1]][2]
    
  }
  

  
  
})

dat_hw[,6] <- as.numeric(dat_hw[,6])


dat_hw <- dat_hw[which(is.na(dat_hw$GameRank) == FALSE),]

dat_hw_sort <- dat_hw[order(dat_hw$GameRank) , ]


dat_hw_sort$Index <- seq(1,dim(dat_hw_sort)[1],by=1)

#dat_hw_sort <- na.omit(dat_hw_sort)
RankCategory <- replicate(dim(dat_hw_sort)[1],1)


#### Get rid of the missing values
#change4 <-  sapply(1:dim(dat_hw_sort)[1],function(x){
  
#  if (x > 560 &  x < 1120 ) {
    
#    RankCategory[x] <<- 2
    
#  }else if (x > 1120 &  x < 1679 ) {
    
    
#    RankCategory[x] <<- 3
    
#  }else if (x > 1679 &  x < 2239 ) {
    
#    RankCategory[x] <<- 4
    
#  }
  
#})

change4 <-  sapply(1:dim(dat_hw_sort)[1],function(x){
  
  if (x > 1998 &  x < 4001 ) {
    
    RankCategory[x] <<- 2
    
  }else if (x > 4001 &  x < 6003 ) {
  
    
    RankCategory[x] <<- 3
    
    }else if (x > 6003 &  x < 8006 ) {
  
      RankCategory[x] <<- 4
      
    }
  
})

dat_final <- cbind(dat_hw_sort,RankCategory)

dat_final$Index <- seq(1,dim(dat_final)[1],by = 1)
######## Replace NA in ListPrice with the mean value ######
#sum(is.na(dat_final$ListPrice))

dat_final$ListPrice[which(is.na(dat_final$ListPrice) == TRUE)] <- mean(dat_final$ListPrice,na.rm = TRUE)

#dat_final[!complete.cases(dat_final),]



write.csv(dat_final,"BoardGameGeekClean_Miss.csv",row.names = FALSE)






