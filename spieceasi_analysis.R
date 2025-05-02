
library(SpiecEasi)
library(dplyr)

setwd("/tscc/projects/ps-allenlab/projdata/vihou/Ecohab22/ASV_data/")
tax16s <- read.csv("/tscc/projects/ps-allenlab/projdata/vihou/Ecohab22/ASV_data/tax16s_prokaryotes.csv", row.names = "Feature.ID")
tax18s <- read.csv("/tscc/projects/ps-allenlab/projdata/vihou/Ecohab22/ASV_data/tax18s_Eukaryotes.csv", row.names = "Feature.ID")

pro_data<-tax16s[0:63]%>%
  as.matrix() %>% # transmogrify data.frame into matrix
  t() 

eu_data<-tax18s[0:63]%>%
  as.matrix() %>% # transmogrify data.frame into matrix
  t()  

pro_se.mb <- spiec.easi(pro_data, method='mb', lambda.min.ratio=1e-2,
                        nlambda=20, pulsar.params=list(rep.num=40, ncores = 16))
saveRDS(pro_se.mb, file = "pro_se_mb_results.rds")

eu_se.mb <- spiec.easi(eu_data, method='mb', lambda.min.ratio=1e-2,
                       nlambda=20, pulsar.params=list(rep.num=40, ncores = 16))
saveRDS(eu_se.mb, file = "eu_se_mb_results.rds")

pro_eu.mb <- spiec.easi(list(pro_data, eu_data), method='mb', nlambda=40,
                      lambda.min.ratio=1e-2, pulsar.params = list(thresh = 0.05, ncores = 16))
saveRDS(pro_eu.mb, file = "pro_eu_se_mb_results.rds")
saveRDS(pro_eu.mb, file = "pro_eu_results.rds")