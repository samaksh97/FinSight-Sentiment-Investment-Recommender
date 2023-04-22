FinSight: Your Vision for Financial Insights

FinSight is a web based portfolio balancer that uses NLP and sentiment analysis to analyze 10K and 10Q Fiscal Reports to generate an optimal master list of securities for trading. Then, that list is filtered through a risk assessment quiz that the user completes to understand the risk profile. Finally, that filtered list of securities is balanced into an investible portfolio using portfolio balancing techniques.

How to setup and run:
1. Clone Repository

2. Open Tableau Project file: Project Viz.twbx

3. From the data_sources folder in the repository, do the following:

a. Add newEval.csv and dva_stock_prices_u.csv as data source dependencies to "sample" data source in Tableau 
b. Add this Google Sheets as data source dependency to "Form Responses 1" data source in Tableau (https://docs.google.com/spreadsheets/d/1nS8WRaVB5S2aaxMiFpVHxSrEE12lx6TGs_WyAkcUSzU/edit?resourcekey#gid=333614162)

4. Setup Jupytab by doing the following:
  a. Install conda and create a virtual environment with Python=3.7
  b. Install Jupyter Kernel Gateway following these instructions: https://github.com/jupyter-server/kernel_gateway
  c. Install JupyTab following these instructions here: https://github.com/CFMTech/Jupytab#installation
  d. We have provided the config.ini and tester.ipynb (portfolio balancer code) in the repository
  e. Using your terminal, navigate to the config.ini file directory
  d. Then run: jupytab --config=config.ini
  e. Once the jupytab server is started, you will get a link in the terminal that looks like (please open): http://sangeetas-mbp.lan:8888 to verify that your Jupytab instance is live
  f. Open Tableau Data Sources and add a new Web Data Connector data source with the link generated above
  g. Feel free to preview the data table and hit refresh to bring in the data
  
5. Your Tableau Dashboard and Visualization is ready for exploration!


Folder Name Legend:

1. Visualization Data: A python notebook that generates dva_stock_prices_u.csv output that is used in Tableau Input
2. Sentiment Analysis: A python notebook that calculates headlines as positive, negative or neutral
3. Financial News Data: 
4. Documents: Misc. documents
5. data_sources: Data source dependenies for Tableau (Project Viz.twbx)
