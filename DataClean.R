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


write.csv(dat_hw,"BoardGameGeekClean.csv",row.names = FALSE)






