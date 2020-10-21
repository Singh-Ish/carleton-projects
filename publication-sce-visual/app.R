library(shiny)
library(ggplot2)

#setwd('C:/Users/Ish/Desktop/currentproject/Carleton/carleton-projects/publication-sce/pub-R')
pub <- read.csv('pubEval.csv')


# Define UI for app that draws a histogram ----
ui <- fluidPage(

  # App title ----
  titlePanel("Publication Metrics for SCE Professors"),

  fluidRow(
    column(4,
           selectInput("nm",
                       "Name:",
                       c("All",
                         sort(unique(as.character(pub$name)))))
    ),
    column(4,
           selectInput("yr",
                       "Year:",
                       c("All",
                         sort(unique(as.character(pub$year),ascending=FALSE))))
    )
    #column(4,downloadButton("report", "Download report")
   # )
   
  ),
  br(),
  # Create a new row for the table.
  DT::dataTableOutput("table")
)




# Define server logic required to draw a histogram ----
server <- function(input, output) {


  output$table <- DT::renderDataTable(DT::datatable({
    data <- pub
    
     if (input$nm != "All") {
       data <- data[data$name == input$nm,]
     }
     if (input$yr != "All") {
       data <- data[data$year == input$yr,]
     }
    
    data
  }))
  
  
  # output$report <- downloadHandler(
  #   # For PDF output, change this to "report.pdf"
  #   filename = function() { paste("report", "pdf", sep = ".")},
  #   content = function(file) {
  #    #  # Copy the report file to a temporary directory before processing it, in
  #    #  # case we don't have write permissions to the current working dir (which
  #    #  # can happen when deployed).
  #    # tempReport <- file.path(tempdir(), "report.Rmd")
  #    # file.copy("report.Rmd", tempReport, overwrite = TRUE)
  #    # 
  #    #  # Knit the document, passing in the `params` list, and eval it in a
  #    #    # child of the global environment (this isolates the code in the document
  #    #    # from the code in this app).
  #    # 
  #    #  rmarkdown::render(tempReport, output_file = file,
  #    #    envir = new.env(parent = globalenv())
  #    #  )
      
      
      
      #write.csv(data, file, row.names = FALSE)
      
   
    
    #}
 # )

  
  

}

shinyApp(ui = ui, server = server)