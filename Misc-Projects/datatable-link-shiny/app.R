library(shiny)
library(ggplot2)

#setwd('C:/Users/Ish/Desktop/currentproject/Carleton/carleton-projects/publication-sce/pub-R')
pub <- read.csv('data.csv')


# Define UI for app that draws a histogram ----
ui <- fluidPage(

  # App title ----
  titlePanel("Publication Metrics for SCE Professors"),

  br(),
  # Create a new row for the table.
  DT::dataTableOutput("table")
)




# Define server logic required to draw a histogram ----
server <- function(input, output) {


  output$table <- DT::renderDataTable(DT::datatable({
    data <- pub
    data
  }, escape = FALSE))
  
  

  
  

}

shinyApp(ui = ui, server = server)