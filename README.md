# Cartwheel POC

Customers can now:

- View existing orders, with data protection checks
- Create new orders and update the relevant 'databases'

Take a look at the bottom half of the below diagram to see typical flow

![Blank diagram (15)](https://github.com/user-attachments/assets/62305fcb-3414-41a2-9e2d-8f306219ccc0)

Here is what one of the final customer journeys look like:

![image](https://github.com/user-attachments/assets/8230d153-22d4-422d-9746-afbeda7ba69c)


## Setup

To setup the python environment, do the below. 
Notes 1: In streamlit hosting, it were several issues with chromadb&sqlite. How its solved, is by deploying the script with the following, that have to be removed in local run. Its the "streamlit_frondend.py" which is the deployment script.
Notes 2: Was a big hassle with setting up secrets. Now it should be fine if adding the secret in a .env file at ./. Do not push that to depoloyment, simply add the secret in a secret manager.

in requirements.txt:
```bash
pysqlite3-binary==0.5.4 
```

in streamlit_frondend.py:
```bash
import pysqlite3
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import sqlite3
```

To run locally: recall removing what is only needed for streamlit deploy

```bash
conda create -p ./.conda python=3.11
pip install -r requirements.txt
```

Then activated the environment with:
```bash
conda activate ./.conda
```

To run the frontend you can type:

```bash
streamlit run streamlit_frontend.py
```

