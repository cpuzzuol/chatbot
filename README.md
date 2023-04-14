`# **ChatGPT + FAR Data**

This is a simple Python script that leverages <a href="https://gpt-index.readthedocs.io/en/latest/index.html">LlamaIndex</a> to interpret rows from the far.dw_grants table. You can write questions, which then get fed into ChatGPT for interpretation based on the database data. ChatGPT will write an answer back based on that data. 

**Installation**
1. I'm using PyCharm for this. Once you pull this repo down, create a virtual python environment.
2. Install the necessary packages:
   1. `pip install python-dotenv mysqlclient pymysql llama_index psycopg2-binary`
3. **You will need to create a .env file in the root directory and fill in the following data:

`OPENAI_API_KEY=` # this is an API key you can get from <a href="https://platform.openai.com/overview">OpenAI</a>. There is a free trial period.

`DB_USER=` # I am using our dev db for all these creds

`DB_PASSWORD=`
   
`DB_HOST=`
   
`DB_SCHEMA=`

You'll see the `/data` directory includes a sample file pulled down from the `far.dw_grants` table. You can tweak the database call to choose more rows.

**Usage**

Run the file `chat.py`. You can also tweak the queries in there. 

