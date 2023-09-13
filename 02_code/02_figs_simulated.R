
#This is the code for Figs 10, 11 and 13-20

library(plotly)

# Define parameters

d_0 <- 0.698      # Current debt ratio
d_n <-0.60        # Target debt ratio (Modify as needed)
n <- 4            # Number of years to target

# Calculate required d

i <- runif(100, min = 0.06, max = 0.08) # max=10 year average i+1, min=10 years average i-1
g <- runif(100, -0.02, 0.07) #max=10 year average g+1, min=10 years average g-1
alpha <- (i - g)/(1 + g)
part1 <- ((alpha)/(((1+alpha)^(-n))-1))
part2 <- (((1+alpha)^(-n))*d_n - d_0)
options("scipen" = 100, "digits" = 4)
d<- part1 * part2 # Gives corresponding d for every pair of i and g required to hit target in n years

# Set data in a matrix

data.df <- data.frame(i, g, d)
data.matrix <- as.matrix(data.df)

# Define axis features

ax <- list(
  zeroline = FALSE,
  showline = FALSE,
  mirror = "ticks",
  gridcolor = toRGB("black"),
  gridwidth = 2,
  zerolinecolor = toRGB("black"),
  zerolinewidth = 4,
  linecolor = toRGB("black"),
  linewidth = 4
)

# Calculate average of simulated values and store 

ai<- mean(i)
ag<- mean(g)
ad<-mean(d)

# Make mesh plot

plot_ly(x= ~i, y= ~g, z= ~d, type='mesh3d' )%>%
  layout(scene= list(xaxis= ax, yaxis= ax, zaxis= ax))

